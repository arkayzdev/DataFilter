import sys
from models.file_utils import CsvUtils, JsonUtils, XmlUtils, YamlUtils
from models.stats_utils import StatsUtils
from models.filter_utils import FilterUtils
from models.sort_utils import SortUtils


class CLI:
    def __init__(self):
        self.data = None
        self.attributes = None

    def load_data(self, file_path: str, file_type: str):
        if file_type == "csv":
            self.data = CsvUtils.read_file(file_path)
        elif file_type == "json":
            self.data = JsonUtils.read_file(file_path)
        elif file_type == "xml":
            self.data = XmlUtils.read_file(file_path)
        elif file_type == "yaml":
            self.data = YamlUtils.read_file(file_path)
        else:
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
            "Enter qn operator (==, !=, >, <, >=, <=, contains, starts_with, ends_with): "
        )
        value = input("Enter value to compare: ")
        try:
            condition = FilterUtils.create_condition(field, operator, value)
            self.data["data"] = FilterUtils.filter_data(self.data["data"], condition)
            print("Data filtered successfully.")
        except Exception as e:
            print(f"Error filtering data: {e}")

    def sort_data(self):
        """Sort data based on user input."""
        if not self.data:
            print("No data loaded.")
            return
        print("Available attributes:", self.attributes)
        key = input("Enter field to sort by: ")
        reverse = input("Sort in reverse order? (y/n): ").lower() == "y"
        self.data["data"] = SortUtils.sort_data(self.data["data"], key, reverse)
        print("Data sorted successfully.")

    def save_data(self, file_path: str, file_type: str):
        """Save data to a file."""
        if not self.data:
            print("No data loaded.")
            return
        if file_type == "csv":
            CsvUtils.save_file(file_path, self.data["data"])
        elif file_type == "json":
            JsonUtils.save_file(file_path, self.data["data"])
        elif file_type == "xml":
            XmlUtils.save_file(file_path, self.data["data"])
        elif file_type == "yaml":
            YamlUtils.save_file(file_path, self.data["data"])
        else:
            raise ValueError("Unsupported file type.")
        print(f"Data saved successfully to {file_path}.")

    def display_data(self):
        """Display the current data."""
        if not self.data:
            print("No data loaded.")
            return
        for item in self.data["data"]:
            print(item)


def main():
    cli = CLI()
    while True:
        print("\nMenu:")
        print("1. Load data")
        print("2. Show statistics")
        print("3. Filter data")
        print("4. Sort data")
        print("5. Save data")
        print("6. Display data")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = input("Enter file path: ")
            file_type = input("Enter file type (csv, json, xml, yaml): ")
            cli.load_data(file_path, file_type)
        elif choice == "2":
            cli.show_stats()
        elif choice == "3":
            cli.filter_data()
        elif choice == "4":
            cli.sort_data()
        elif choice == "5":
            file_path = input("Enter file path: ")
            file_type = input("Enter file type (csv, json, xml, yaml): ")
            cli.save_data(file_path, file_type)
        elif choice == "6":
            cli.display_data()
        elif choice == "7":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
