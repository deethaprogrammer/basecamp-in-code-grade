from warehouse import Warehouse
from package import Package


def test_register_package_test():
    warehouse = Warehouse(capacity=2)
    package = Package("P1", 1.0, 100.0, "2025-11-11")
    assert warehouse.register_package(package) is True
    assert warehouse.get_package("P1") == package

def test_warehouse_full():
    warehouse = Warehouse(capacity=0)
    package = Package("P1", 1.0, 100.0, "2025-11-11")
    warehouse.register_package(package)
    assert warehouse.register_package(package) is False

test_register_package_test()
test_warehouse_full()

#import pytest