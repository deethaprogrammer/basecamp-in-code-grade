from warehouse_logger import WarehouseLogger
from package import Package
from warehouse_manager import WarehouseManager
from datetime import date
import pytest

def test_stores_package_id():
    logger = WarehouseLogger("Beurs")
    logger.save_file = "test_log.txt"
    
    with open(logger.save_file, "w") as f:
        f.write("")
    
    package1 = Package("p001", 2.0, 100.0, date(2025, 11, 18))
    package2 = Package("p002", 3.0, 200.0, date(2025, 11, 20))
    logger.log_action("register", package1)
    logger.log_action("register", package2)
    
    manager = WarehouseManager()
    manager.logger.save_file = "test_log.txt"
    
    assert manager.stores_package_id("p001") is True
    assert manager.stores_package_id("p999") is False
    
def test_get_all_packages():
    manager = WarehouseManager()
    manager.logger.save_file = "test_log.txt"
    packages = manager.get_all_packages()
    assert isinstance(packages, tuple)
    assert len(packages) == 2

def test_get_total_fee():
    manager = WarehouseManager()
    manager.logger.save_file = "test_log.txt"
    total = manager.get_total_fee()
    assert total == round(sum(p.get_delivery_fee() for p in manager.get_all_packages()), 2)
    
def test_get_total_fee_by_range():
    manager = WarehouseManager()
    manager.logger.save_file = "test_log.txt"
    fee = manager.get_total_fee_by_range(date(2025, 11, 19), date(2025, 11, 20))
    expected = sum(p.get_delivery_fee() for p in manager.get_all_packages() if p.delivery_date in [date(2025, 11, 19), date(2025, 11, 20)])
    assert fee == round(expected, 2)
    
def test_wrong_date():
    manager = WarehouseManager()
    manager.logger.save_file = "test_log.txt"
    assert manager.get_total_fee_by_range(date(2025, 11, 11), date(2025, 10, 11)) is None
    
if __name__ == "__main__":
    test_stores_package_id()
    test_get_all_packages()
    test_get_total_fee()
    test_get_total_fee_by_range()
    test_wrong_date()
    print("All manual tests passed.")
