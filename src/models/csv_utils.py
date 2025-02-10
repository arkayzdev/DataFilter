import csv
from dataclasses import dataclass
from typing import Any


@dataclass
class CsvUtils:
    @classmethod
    def read_csv(cls, file_path: str, delimiter: str = ",") -> dict[str, Any]:
        with open(file_path, "r") as file:
            reader = list(csv.reader(file, delimiter=delimiter))
            return {"attributes_name": reader[0], "data": reader[1:]}
