from dataclasses import dataclass
from typing import List

@dataclass
class ClassBuilder:
    class_name: str
    class_attributes: List[str]

    def build_attributes(self) -> dict[str, None]:
        return {attr: None for attr in self.class_attributes}

    def create_class(self) -> object:
        def print_class(self):
            print(f"Class Name: {self.__class__.__name__}")
            print("Attributes:")
            for attr, value in vars(self).items():
                print(f"  - {attr}: {value}")

        def __init__(self, *args):
            if len(args) != len(self.__class__.class_attributes):
                raise ValueError(f"Expected {len(self.__class__.class_attributes)} arguments, got {len(args)}")
            for attr, value in zip(self.__class__.class_attributes, args):
                setattr(self, attr, value)

        attributes = self.build_attributes()

        attributes["__init__"] = __init__
        attributes["print_class"] = print_class

        attributes["class_attributes"] = self.class_attributes

        return type(self.class_name, (object,), attributes)


# TEST

class_name = "Student"
class_attributes = ["firstname", "lastname", "age", "apprentice", "grades"]

builder = ClassBuilder(class_name, class_attributes)

Student = builder.create_class()

person_instance = Student("Thierry", "H.", 30, True, [12, 10, 12])

person_instance.print_class()