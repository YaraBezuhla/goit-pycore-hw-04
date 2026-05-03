from pathlib import Path


def get_file_path(filename: str) -> Path:
    base_dir = Path(__file__).absolute().parent.parent
    return base_dir / "resources" / filename