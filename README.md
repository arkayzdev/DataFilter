# 📍 Data Filter (Python Project 3IABD2)

## 🔮 Stack

![Static Badge](https://img.shields.io/badge/Python-grey?style=for-the-badge&logo=Python)

## 🌐 Project Overview - Global

The goal of this project is to create a program that allows loading, saving, filtering, sorting, and displaying data from files in CSV, JSON, XML, or YAML formats.

### File Structure

```txt
DataFilter/
├── data/
├── src/
├   ├─ utils/
├       ├── file_utils.py
├       ├── filter_utils.py
├       ├── sort_utils.py
├       ├── stats_utils.py
├   ├── cli.py
├── main.py
├── README.md
```

## 🚀 Getting Started

System Requirements:

- Python 3.10.9+
- Package managers : pip

## 💻 Installation

### From source

> Clone the repository (if you have already the repository in your computer, skip this step)

```bash
$ git clone https://github.com/yourusername/DataFilter.git
$ cd DataFilter
```

> Install Python Dependencies

```bash
$ cd script-bs
$ python -m venv env
$ env/bin/activate  # On Windows, use `env\Scripts\activate`
$ pip install --no-deps -r requirements.txt
```

> Pre-commit Hooks

```bash
# Install the pre-commit hooks
$ pre-commit install

#Run pre-commit on all files
$ pre-commit run --all-files
```

> Run the script

```bash
$ python main.py

# -> And now you should have a menu in the bash.
```

## 🤖 Usage

### 1. Load data

> You choose the file path, then it will load the data from the file (csv, json, xml, yaml).

### 2. Show statistics

> If a file is loaded, you can get statistics of it, including means, min, max, the list of values for each attributes ...

### 3. Filter data

> If a file is loaded, you can filter the data. eggs contains "a" / >= 5 ...

### 4. Sort data

> If a file is loaded, you can sort the data ascending or descending according to the selected attribute.

### 5. Save data

> You choose the file path, then it will save the data in the file format (csv, json, xml, yaml).

### 6. Display data

> It will show the data of the file, and the updated version of any action you have done on it.

### 7. Exit

> Quit the program.

## 🚶‍♂️ Author

- [@Huang-Frederic](https://github.com/Huang-Frederic)
- [@Zhuang-Franck](https://github.com/arkayzdev)
