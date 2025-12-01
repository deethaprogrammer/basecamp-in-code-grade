from warehouse import Warehouse
from package import Package
from datetime import date
import pytest

def test_warehouse_full():
    warehouse = Warehouse(capacity=0)
    package = Package("P1", 1.0, 100.0, date(2025, 11, 11))
    warehouse.register_package(package)
    assert warehouse.register_package(package) is False

test_warehouse_full()

#import pytest