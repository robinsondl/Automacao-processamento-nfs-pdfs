import re
from typing import List, Optional

from app.domain.entities.nf_item import NfItem


class NfParserService:
    RE_COD_PROD = re.compile(r"^\d{8,}$")
    RE_NCM = re.compile(r"^\d{4}\.\d{2}\.\d{2}$")
    RE_UN = re.compile(r"^(UN|PC)$", re.IGNORECASE)
    RE_NUM = re.compile(r"^[\d.,]+$")
    RE_ORPHAN_CONT = re.compile(r"^\d{3,5}\s+\d{3}\.\d{4}\.\d{2}$")

    FISCAIS_QTD = 12

    def should_append_continuation(self, cont_txt: str) -> bool:
        text = cont_txt.strip()
        if not text:
            return False
        if text.isdigit() and len(text) <= 12:
            return True
        if self.RE_ORPHAN_CONT.match(text):
            return True
        if re.search(r"[A-Za-z].*\d|\d.*[A-Za-z]", text):
            return len(text) <= 90
        if any(ch.isalpha() for ch in text):
            return len(text) <= 90
        return False

    def parse_item_tokens(self, tokens: List[str], numero_nf: str) -> Optional[NfItem]:
        if not tokens or not self.RE_COD_PROD.match(tokens[0]):
            return None

        ncm_pos = None
        for index, token in enumerate(tokens):
            if self.RE_NCM.match(token):
                ncm_pos = index
                break

        if ncm_pos is None:
            return None

        codigo_produto = tokens[0]
        descricao = " ".join(tokens[1:ncm_pos]).strip()

        fiscais = tokens[ncm_pos:ncm_pos + self.FISCAIS_QTD]
        if len(fiscais) < self.FISCAIS_QTD:
            return None

        if not self.RE_UN.match(fiscais[3]):
            return None

        for index in range(4, 12):
            if not self.RE_NUM.match(fiscais[index]):
                return None

        sobra = tokens[ncm_pos + self.FISCAIS_QTD:]
        if sobra:
            sobra_txt = " ".join(sobra).strip()
            if self.should_append_continuation(sobra_txt) and sobra_txt not in descricao:
                descricao = f"{descricao} - {sobra_txt}"

        return NfItem(
            codigo_produto=codigo_produto,
            descricao=descricao,
            ncm_sh=fiscais[0],
            cst=fiscais[1],
            cfop=fiscais[2],
            unidade=fiscais[3],
            quantidade=fiscais[4],
            valor_unitario=fiscais[5],
            valor_total=fiscais[6],
            bc_icms=fiscais[7],
            valor_icms=fiscais[8],
            valor_ipi=fiscais[9],
            aliquota_icms=fiscais[10],
            aliquota_ipi=fiscais[11],
            numero_nf=numero_nf,
        )