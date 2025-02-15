import os
import sys

from src.cli import CLI


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

        match choice:
            case "1":
                file_path = input("Enter file path: ")
                if os.path.isfile(file_path):
                    cli.load_data(file_path)
                else:
                    print("File not found, please retry.")
            case "2":
                cli.show_stats()
            case "3":
                cli.filter_data()
            case "4":
                cli.sort_data()
            case "5":
                try:
                    folder_path = input("Enter folder path (for example data/sample): ")
                    if not os.path.exists(folder_path):
                        print("Folder not found, creating folder...")
                        os.makedirs(folder_path)
                    filename = input("Enter filename: ")
                    file_type = input("Enter file type (csv, json, xml, yaml): ")
                    cli.save_data(f"{folder_path}/{filename}", file_type)
                except Exception as e:
                    print(f"Error saving data ({e}), please retry.")
            case "6":
                cli.display_data()
            case "7":
                print("Exiting...")
                sys.exit()
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
