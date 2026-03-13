from abc import ABC, abstractmethod
from pathlib import Path

from app.domain.entities.nf_document import NfDocument


class PdfRepository(ABC):
    @abstractmethod
    def extract_nf_document(self, pdf_path: Path) -> NfDocument:
        pass