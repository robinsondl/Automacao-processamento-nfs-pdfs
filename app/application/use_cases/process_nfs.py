from pathlib import Path
from typing import List

from config.settings import INPUT_DIR
from app.application.dto.process_result import ProcessResult
from app.domain.interfaces.excel_repository import ExcelRepository
from app.domain.interfaces.file_manager import FileManager
from app.domain.interfaces.pdf_repository import PdfRepository


class ProcessNfsUseCase:
    def __init__(
        self,
        pdf_repository: PdfRepository,
        excel_repository: ExcelRepository,
        file_manager: FileManager,
    ) -> None:
        self.pdf_repository = pdf_repository
        self.excel_repository = excel_repository
        self.file_manager = file_manager

    def execute(self) -> List[ProcessResult]:
        self.file_manager.ensure_directories()
        existing_nfs = self.excel_repository.get_existing_nfs()
        pdf_files = self.file_manager.list_pdf_files(INPUT_DIR)

        results: List[ProcessResult] = []

        for pdf_file in pdf_files:
            try:
                nf_document = self.pdf_repository.extract_nf_document(pdf_file)

                if not nf_document.numero_nf:
                    self.file_manager.move_to_error(pdf_file)
                    results.append(
                        ProcessResult(
                            file_name=pdf_file.name,
                            numero_nf="",
                            inserted_rows=0,
                            status="ERROR",
                            message="Não foi possível identificar o número da NF.",
                        )
                    )
                    continue

                if nf_document.numero_nf in existing_nfs:
                    self.file_manager.move_to_imported(pdf_file)
                    results.append(
                        ProcessResult(
                            file_name=pdf_file.name,
                            numero_nf=nf_document.numero_nf,
                            inserted_rows=0,
                            status="SKIPPED",
                            message="NF já existe na planilha.",
                        )
                    )
                    continue

                inserted_rows = self.excel_repository.insert_items(nf_document.itens)

                if inserted_rows > 0:
                    existing_nfs.add(nf_document.numero_nf)
                    self.file_manager.move_to_imported(pdf_file)
                    results.append(
                        ProcessResult(
                            file_name=pdf_file.name,
                            numero_nf=nf_document.numero_nf,
                            inserted_rows=inserted_rows,
                            status="SUCCESS",
                            message="NF processada com sucesso.",
                        )
                    )
                else:
                    self.file_manager.move_to_error(pdf_file)
                    results.append(
                        ProcessResult(
                            file_name=pdf_file.name,
                            numero_nf=nf_document.numero_nf,
                            inserted_rows=0,
                            status="WARNING",
                            message="Nenhum item válido encontrado.",
                        )
                    )

            except Exception as exc:
                self.file_manager.move_to_error(pdf_file)
                results.append(
                    ProcessResult(
                        file_name=pdf_file.name,
                        numero_nf="",
                        inserted_rows=0,
                        status="ERROR",
                        message=f"Erro ao processar arquivo: {exc}",
                    )
                )

        return results