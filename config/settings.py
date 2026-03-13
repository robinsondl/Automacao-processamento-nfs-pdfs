from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_DIR = DATA_DIR / "input"
IMPORTED_DIR = DATA_DIR / "imported"
ERROR_DIR = DATA_DIR / "error"

EXCEL_FILE = BASE_DIR / "Nfs Consolidadas.xlsx"

WORKSHEET_NAME = "Nfs Consolidadas"
TABLE_NAME = "TabelaNfs"

EXPECTED_COLUMNS = [
    "CÓD. PROD.",
    "DESCRIÇÃO DO PRODUTO/SERVIÇO",
    "NCM/SH",
    "CST",
    "CFOP",
    "UN",
    "QTDE.",
    "VL. UNIT.",
    "VL. TOTAL",
    "Bc. ICMS",
    "VL. ICMS",
    "VL. IPI",
    "Al. ICMS",
    "Al. IPI",
    "Numero NF",
]