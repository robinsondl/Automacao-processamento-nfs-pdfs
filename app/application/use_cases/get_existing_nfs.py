from app.domain.interfaces.excel_repository import ExcelRepository


class GetExistingNfsUseCase:
    def __init__(self, excel_repository: ExcelRepository) -> None:
        self.excel_repository = excel_repository

    def execute(self) -> set[str]:
        return self.excel_repository.get_existing_nfs()