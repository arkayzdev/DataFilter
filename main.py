from src.models.class_builder import ClassBuilder
from src.models.file_utils import CsvUtils, JsonUtils


# TEST


def test_builder():
    class_name = "Student"
    attributes = ["firstname", "lastname", "age", "apprentice", "grades"]

    Student: object = ClassBuilder.create_class(class_name, attributes)

    a = ["Thierry", "H.", 30, True, [12, 10, 12]]
    person_instance = Student(*a)

    person_instance.print_class()


def test_csv_to_class():
    data = CsvUtils.read_file(file_path="data/test.csv")

    obj_builder = ClassBuilder.create_class(
        class_name="test", attributes_name=data["attributes"]
    )

    for d in data["data"]:
        obj_builder(*d).print_class(oneline=True)


def test_json_to_class():
    data = JsonUtils.read_file(file_path="data/test.json")

    obj_builder = ClassBuilder.create_class(
        class_name="test", attributes_name=data["attributes"]
    )

    for d in data["data"]:
        obj_builder(*d).print_class(oneline=True)


if __name__ == "__main__":
    test_csv_to_class()
    test_json_to_class()
