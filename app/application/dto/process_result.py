from dataclasses import dataclass


@dataclass
class ProcessResult:
    file_name: str
    numero_nf: str
    inserted_rows: int
    status: str
    message: str