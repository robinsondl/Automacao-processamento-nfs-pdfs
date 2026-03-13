from app.application.use_cases.process_nfs import ProcessNfsUseCase
from app.domain.services.nf_parser_service import NfParserService
from app.infrastructure.excel.openpyxl_nf_repository import OpenpyxlNfRepository
from app.infrastructure.files.local_file_manager import LocalFileManager
from app.infrastructure.pdf.pdfplumber_reader import PdfPlumberReader


def run() -> None:
    parser_service = NfParserService()
    pdf_repository = PdfPlumberReader(parser_service)
    excel_repository = OpenpyxlNfRepository()
    file_manager = LocalFileManager()

    use_case = ProcessNfsUseCase(
        pdf_repository=pdf_repository,
        excel_repository=excel_repository,
        file_manager=file_manager,
    )

    results = use_case.execute()

    if not results:
        print("Nenhum PDF encontrado para processamento.")
        return

    for result in results:
        print(
            f"[{result.status}] "
            f"Arquivo: {result.file_name} | "
            f"NF: {result.numero_nf or '-'} | "
            f"Linhas: {result.inserted_rows} | "
            f"Mensagem: {result.message}"
        )