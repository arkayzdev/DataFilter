import csv
import json
from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Any, Dict


class FileUtils(ABC):
    @classmethod
    @abstractmethod
    def read_file(cls, file_path: str) -> Dict[str, Any]:
        pass

    @classmethod
    @abstractmethod
    def save_file(cls, objects: list[object]) -> Dict[str, Any]:
        pass


@dataclass
class CsvUtils(FileUtils):
    @classmethod
    def read_file(cls, file_path: str, delimiter: str = ",") -> Dict[str, Any]:
        with open(file_path, "r") as file:
            reader = list(csv.reader(file, delimiter=delimiter))
            return {"attributes": reader[0], "data": reader[1:]}


@dataclass
class JsonUtils(FileUtils):
    @classmethod
    def read_file(cls, file_path: str) -> Dict[str, Any]:
        with open(file_path, "r") as file:
            reader = json.load(file)
            if "data" not in reader:
                raise ValueError("Missing keys in JSON file: 'data'")
            return {
                "attributes": list(reader["data"][0].keys()),
                "data": [list(item.values()) for item in reader["data"]],
            }
