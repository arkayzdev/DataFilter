import copy

from src.utils.file_utils import CsvUtils, JsonUtils, XmlUtils, YamlUtils
from src.utils.stats_utils import StatsUtils
from src.utils.filter_utils import FilterUtils
from src.utils.sort_utils import SortUtils


def format_parser(file_path: str):
    return file_path.split(".")[-1]


class CLI:
    def __init__(self):
        self.data = None
        self.cursor = -1
        self.historical_data = []
        self.attributes = None

    def show_main_menu(self):
        print("\nMenu:")
        print("1. Load data")
        print("2. Show statistics")
        print("3. Filter data")
        print("4. Sort data")
        print("5. Save data")
        print("6. Display data")
        print("7. Exit")

    def show_cli_menu(self):
        print("\nFilter menu:")
        print("1. Apply filter")
        print("2. Undo filter")
        print("3. Redo filter")
        print("4. Return")

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
        self.historical_data = [copy.deepcopy(self.data)]
        self.cursor = 0
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

    def filter_cli(self):
        if not self.data:
            print("No data loaded.")
            return
        while True:
            self.show_cli_menu()
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.filter_data()
                    return
                case "2":
                    undo = self.filter_undo()
                    if undo:
                        return
                case "3":
                    redo = self.filter_redo()
                    if redo:
                        return
                case "4":
                    print("Return to main CLI...")
                    return

    def filter_undo(self) -> bool:
        if self.cursor == 0:
            print("No more filters to undo.")
            return False
        choice = input("Are you sure you want to undo the last filter? (y/n): ")
        if choice.lower() == "y":
            self.cursor -= 1
            self.data = copy.deepcopy(self.historical_data[self.cursor])
            print("Filter undone successfully.")
            return True
        print("Filter not undone.")
        return False

    def filter_redo(self) -> bool:
        if len(self.historical_data) - 1 == self.cursor:
            print("No more filters to redo.")
            return False
        choice = input("Are you sure you want to redo the last filter? (y/n): ")
        if choice.lower() == "y":
            self.cursor += 1
            self.data = copy.deepcopy(self.historical_data[self.cursor])
            print("Filter redone successfully.")
            return True
        print("Filter not redone.")
        return False

    def filter_data(self):
        print("Available attributes:", self.attributes)
        field = input("Enter field to filter by: ")
        operator = input(
            "Enter an operator (==, !=, >, <, >=, <=, contains, starts_with, ends_with): "
        )
        value = input("Enter value to compare: ")
        try:
            condition = FilterUtils.create_condition(field, operator, value)
            self.data["data"] = FilterUtils.filter_data(self.data["data"], condition)
            if len(self.historical_data) - 1 != self.cursor:
                self.historical_data = copy.deepcopy(
                    self.historical_data[: self.cursor + 1]
                )
            self.historical_data.append(copy.deepcopy(self.data))
            self.cursor += 1

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
