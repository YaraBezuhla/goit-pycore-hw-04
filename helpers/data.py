from pathlib import Path


def load_data(path: Path) -> list[str] | None:
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.readlines()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None


def clean_data(raw_data: list[str]) -> list[str]:
    return [line.strip() for line in raw_data if line.strip()]


def parse_lines(path: Path, expected_format: str) -> list[str] | None:
    raw = load_data(path)
    if raw is None:
        return None
    cleaned = clean_data(raw)
    if not cleaned:
        print(f"File is empty. Expected format: {expected_format}")
        return None
    return cleaned
