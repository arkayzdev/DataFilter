import csv
import json
import xml.etree.ElementTree as ET
import yaml
from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Any, Dict, List


class FileUtils(ABC):
    @classmethod
    @abstractmethod
    def read_file(cls, file_path: str) -> Dict[str, Any]:
        pass

    @classmethod
    @abstractmethod
    def save_file(cls, file_path: str, data: List[Dict[str, Any]]) -> None:
        pass


@dataclass
class CsvUtils(FileUtils):
    @classmethod
    def read_file(cls, file_path: str, delimiter: str = ",") -> Dict[str, Any]:
        with open(file_path, "r") as file:
            reader = list(csv.reader(file, delimiter=delimiter))
            attributes = reader[0]
            data = []
            for row in reader[1:]:
                data.append({attr: value for attr, value in zip(attributes, row)})
            return {"attributes": attributes, "data": data}

    @classmethod
    def save_file(cls, file_path: str, data: List[Dict[str, Any]]) -> None:
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data[0].keys())
            for item in data:
                writer.writerow(item.values())


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
                "data": reader["data"],
            }

    @classmethod
    def save_file(cls, file_path: str, data: List[Dict[str, Any]]) -> None:
        with open(file_path, "w") as file:
            json.dump({"data": data}, file, indent=4)


@dataclass
class XmlUtils(FileUtils):
    @classmethod
    def read_file(cls, file_path: str) -> Dict[str, Any]:
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = []
        for item in root:
            data.append({child.tag: child.text for child in item})
        return {
            "attributes": list(data[0].keys()),
            "data": data,
        }

    @classmethod
    def save_file(cls, file_path: str, data: List[Dict[str, Any]]) -> None:
        root = ET.Element("root")
        for item in data:
            element = ET.SubElement(root, "item")
            for key, value in item.items():
                child = ET.SubElement(element, key)
                child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(file_path)


@dataclass
class YamlUtils(FileUtils):
    @classmethod
    def read_file(cls, file_path: str) -> Dict[str, Any]:
        with open(file_path, "r") as file:
            reader = yaml.safe_load(file)
            if "data" not in reader:
                raise ValueError("Missing keys in YAML file: 'data'")
            return {
                "attributes": list(reader["data"][0].keys()),
                "data": reader["data"],
            }

    @classmethod
    def save_file(cls, file_path: str, data: List[Dict[str, Any]]) -> None:
        with open(file_path, "w") as file:
            yaml.dump({"data": data}, file)
