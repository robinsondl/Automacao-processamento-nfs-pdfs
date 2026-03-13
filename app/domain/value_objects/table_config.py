from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class TableConfig:
    worksheet_name: str
    table_name: str
    expected_columns: List[str]