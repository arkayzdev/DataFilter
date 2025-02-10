from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ClassBuilder:
    @classmethod
    def build_attributes(
        cls, attributes_name: List[str]
    ) -> dict[Optional[str], Optional[object]]:
        return {attr: None for attr in attributes_name}

    @classmethod
    def create_class(cls, class_name: str, attributes_name: List[str]) -> object:
        def print_class(self, oneline: bool = False):
            if oneline:
                print(f"{self.__class__.__name__}: {vars(self)}")
                return
            print(f"Class Name: {self.__class__.__name__}")
            print("Attributes:")
            for attr, value in vars(self).items():
                print(f"  - {attr}: {value}")

        def __init__(self, *args):
            if len(args) != len(self.__class__.attributes):
                raise ValueError(
                    f"Expected {len(self.__class__.attributes)} arguments,"
                    f"got {len(args)}"
                )
            for attr, value in zip(self.__class__.attributes, args):
                setattr(self, attr, value)

        new_class = cls.build_attributes(attributes_name=attributes_name)

        new_class["__init__"] = __init__
        new_class["print_class"] = print_class
        new_class["attributes"] = attributes_name

        return type(class_name, (object,), new_class)
