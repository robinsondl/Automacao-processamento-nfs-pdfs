from abc import ABC, abstractmethod
from pathlib import Path
from typing import List


class FileManager(ABC):
    @abstractmethod
    def list_pdf_files(self, directory: Path) -> List[Path]:
        pass

    @abstractmethod
    def ensure_directories(self) -> None:
        pass

    @abstractmethod
    def move_to_imported(self, file_path: Path) -> None:
        pass

    @abstractmethod
    def move_to_error(self, file_path: Path) -> None:
        pass