from src.utils.file_utils import CsvUtils, JsonUtils, XmlUtils, YamlUtils
from src.utils.stats_utils import StatsUtils
from src.utils.filter_utils import FilterUtils
from src.utils.sort_utils import SortUtils


def format_parser(file_path: str):
    return file_path.split(".")[-1]


class CLI:
    def __init__(self):
        self.data = None
        self.attributes = None

    def load_data(self, file_path: str):
        file_type = format_parser(file_path)
        match file_type:
            case "csv":
                self.data = CsvUtils.read_file(file_path)
            case "json":
                self.data = JsonUtils.read_file(file_path)
            case "xml":
                self.data = XmlUtils.read_file(file_path)
            case "yaml":
                self.data = YamlUtils.read_file(file_path)
            case _:
                raise ValueError("Unsupported file type.")
        self.attributes = self.data["attributes"]
        print(f"Data loaded successfully with attributes: {self.attributes}")

    def show_stats(self):
        if not self.data:
            print("No data loaded.")
            return
        stats = StatsUtils.calculate_stats(self.data["data"])
        for key, values in stats.items():
            print(f"Statistics for {key}:")
            for stat, value in values.items():
                print(f"  - {stat}: {value}")

    def filter_data(self):
        if not self.data:
            print("No data loaded.")
            return
        print("Available attributes:", self.attributes)
        field = input("Enter field to filter by: ")
        operator = input(
            "Enter an operator (==, !=, >, <, >=, <=, contains, starts_with, ends_with): "
        )
        value = input("Enter value to compare: ")
        try:
            condition = FilterUtils.create_condition(field, operator, value)
            self.data["data"] = FilterUtils.filter_data(self.data["data"], condition)
            print("Data filtered successfully.")
        except Exception as e:
            print(f"Error filtering data: {e}")

    def sort_data(self):
        if not self.data:
            print("No data loaded.")
            return
        print("Available attributes:", self.attributes)
        key = input("Enter field to sort by: ")
        reverse = input("Sort in reverse order? (y/n): ").lower() == "y"
        self.data["data"] = SortUtils.sort_data(self.data["data"], key, reverse)
        print("Data sorted successfully.")

    def save_data(self, file_path: str, file_type: str):
        if not self.data:
            print("No data loaded.")
            return
        match file_type:
            case "csv":
                CsvUtils.save_file(file_path, self.data["data"])
            case "json":
                JsonUtils.save_file(file_path, self.data["data"])
            case "xml":
                XmlUtils.save_file(file_path, self.data["data"])
            case "yaml":
                YamlUtils.save_file(file_path, self.data["data"])
            case _:
                raise ValueError("Unsupported file type.")
        print(f"Data saved successfully to {file_path}.{file_type}.")

    def display_data(self):
        if not self.data:
            print("No data loaded.")
            return
        for item in self.data["data"]:
            print(item)
