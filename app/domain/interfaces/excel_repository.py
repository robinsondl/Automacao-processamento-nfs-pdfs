from abc import ABC, abstractmethod
from typing import List, Set

from app.domain.entities.nf_item import NfItem


class ExcelRepository(ABC):
    @abstractmethod
    def get_existing_nfs(self) -> Set[str]:
        pass

    @abstractmethod
    def insert_items(self, items: List[NfItem]) -> int:
        pass