from pathlib import Path

import pdfplumber

from app.domain.entities.nf_document import NfDocument
from app.domain.interfaces.pdf_repository import PdfRepository
from app.domain.services.nf_parser_service import NfParserService
from app.infrastructure.pdf.regex_patterns import (
    IGNORAR_LINHAS_PREFIX,
    RE_DADOS_TABELA,
    RE_NF,
    RE_STOP_SECTION,
)


class PdfPlumberReader(PdfRepository):
    def __init__(self, parser_service: NfParserService) -> None:
        self.parser_service = parser_service

    def _find_word_top(self, page, pattern_regex):
        words = page.extract_words() or []
        if not words:
            return None

        words_sorted = sorted(words, key=lambda w: (round(w["top"], 1), w["x0"]))

        line_words = []
        last_top = None

        for word in words_sorted:
            current_top = round(word["top"], 1)
            if last_top is None or abs(current_top - last_top) <= 2.0:
                line_words.append(word["text"])
            else:
                if pattern_regex.search(" ".join(line_words)):
                    return last_top
                line_words = [word["text"]]
            last_top = current_top

        if line_words and pattern_regex.search(" ".join(line_words)):
            return last_top

        return None

    def _get_bbox_dados_produtos(self, page):
        top_anchor = self._find_word_top(page, RE_DADOS_TABELA)
        if top_anchor is None:
            return (0, 360, page.width, min(page.height, 780))

        stop_top = self._find_word_top(page, RE_STOP_SECTION)

        top = max(0, top_anchor - 3)
        if stop_top is not None and stop_top > top_anchor + 40:
            bottom = min(page.height, stop_top + 80)
        else:
            bottom = page.height - 1

        return (0, top, page.width, bottom)

    def _extract_table_text(self, page) -> str:
        bbox = self._get_bbox_dados_produtos(page)
        return page.crop(bbox).extract_text() or ""

    def extract_nf_document(self, pdf_path: Path) -> NfDocument:
        numero_nf = ""
        nf_document = NfDocument(numero_nf="")

        buffer_tokens = []
        last_item = None

        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                full_text = page.extract_text() or ""

                for line in full_text.splitlines():
                    match = RE_NF.search(line)
                    if match:
                        numero_nf = match.group(1)
                        nf_document.numero_nf = numero_nf

                table_text = self._extract_table_text(page)
                if not table_text.strip():
                    continue

                lines = [line.strip() for line in table_text.splitlines() if line.strip()]

                for line in lines:
                    if RE_STOP_SECTION.search(line):
                        if buffer_tokens:
                            item = self.parser_service.parse_item_tokens(buffer_tokens, numero_nf)
                            if item:
                                nf_document.add_item(item)
                                last_item = item
                            buffer_tokens = []
                        break

                    if any(line.upper().startswith(prefix) for prefix in IGNORAR_LINHAS_PREFIX):
                        continue

                    parts = line.split()
                    if not parts:
                        continue

                    starts_new_item = self.parser_service.RE_COD_PROD.match(parts[0]) is not None

                    if starts_new_item:
                        if buffer_tokens:
                            item = self.parser_service.parse_item_tokens(buffer_tokens, numero_nf)
                            if item:
                                nf_document.add_item(item)
                                last_item = item
                        buffer_tokens = parts[:]
                    else:
                        if buffer_tokens:
                            buffer_tokens.extend(parts)
                        else:
                            orphan_txt = " ".join(parts).strip()
                            if last_item and self.parser_service.should_append_continuation(orphan_txt):
                                if orphan_txt not in last_item.descricao:
                                    last_item.descricao = f"{last_item.descricao} - {orphan_txt}"

            if buffer_tokens:
                item = self.parser_service.parse_item_tokens(buffer_tokens, numero_nf)
                if item:
                    nf_document.add_item(item)

        return nf_document