import shutil
from pathlib import Path

from config.settings import ERROR_DIR, IMPORTED_DIR, INPUT_DIR
from app.domain.interfaces.file_manager import FileManager


class LocalFileManager(FileManager):
    def ensure_directories(self) -> None:
        INPUT_DIR.mkdir(parents=True, exist_ok=True)
        IMPORTED_DIR.mkdir(parents=True, exist_ok=True)
        ERROR_DIR.mkdir(parents=True, exist_ok=True)

    def list_pdf_files(self, directory: Path) -> list[Path]:
        return [file for file in directory.iterdir() if file.is_file() and file.suffix.lower() == ".pdf"]

    def move_to_imported(self, file_path: Path) -> None:
        destination = IMPORTED_DIR / file_path.name
        shutil.move(str(file_path), str(destination))

    def move_to_error(self, file_path: Path) -> None:
        destination = ERROR_DIR / file_path.name
        shutil.move(str(file_path), str(destination))