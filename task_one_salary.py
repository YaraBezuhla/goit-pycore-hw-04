from pathlib import Path
from helpers import file_path
from helpers.data import parse_lines


def total_salary(path: Path) -> tuple[float, float] | None:
    lines = parse_lines(path, "name,salary")
    if lines is None:
        return None, None
    try:
        salaries = [float(line.split(",")[1]) for line in lines]
    except (ValueError, IndexError):
        print("Invalid file format. Expected: name,salary")
        return None, None
    total = sum(salaries)
    average = total / len(salaries)
    return total, average

path = file_path.get_file_path("salary.txt")
total, average = total_salary(path)
print(f"Total salary: {total},\nAverage salary: {average}")
