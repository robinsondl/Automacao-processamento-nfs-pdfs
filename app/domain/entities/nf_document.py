from dataclasses import dataclass, field
from typing import List

from app.domain.entities.nf_item import NfItem


@dataclass
class NfDocument:
    numero_nf: str
    itens: List[NfItem] = field(default_factory=list)

    def add_item(self, item: NfItem) -> None:
        self.itens.append(item)

    def total_itens(self) -> int:
        return len(self.itens)