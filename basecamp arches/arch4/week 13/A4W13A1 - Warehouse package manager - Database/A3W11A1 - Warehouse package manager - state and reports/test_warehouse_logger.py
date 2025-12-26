from warehouse_logger import WarehouseLogger
from package import Package
from datetime import date
import csv
import pytest
import os

def test_generate_most_profitable_packages_file(tmp_path, monkeypatch):
    monkeypatch.setattr("sys.path", [str(tmp_path)])

    logger = WarehouseLogger("TEST")

    d = date(2025, 1, 1)
    low = Package("L", 1, 1, d)
    mid = Package("M", 5, 5, d)
    high = Package("H", 20, 20, d)

    packages = (low, mid, high)

    assert logger.generate_most_profitable_packages_file(packages, 2)

    csv_path = tmp_path / "most_profitable_packages.csv"
    assert csv_path.exists()

    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f, delimiter=";"))
        
    assert rows[1][0] == "H"
    assert rows[2][0] == "M"
