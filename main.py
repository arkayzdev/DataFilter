from src.models.class_builder import ClassBuilder

# TEST

class_name = "Student"
attributes = ["firstname", "lastname", "age", "apprentice", "grades"]

Student: object = ClassBuilder.create_class(class_name, attributes)

a = ["Thierry", "H.", 30, True, [12, 10, 12]]
person_instance = Student(*a)

person_instance.print_class()
