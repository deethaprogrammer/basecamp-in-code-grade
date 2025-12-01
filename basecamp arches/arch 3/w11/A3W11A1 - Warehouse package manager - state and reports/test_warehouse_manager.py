from warehouse_logger import WarehouseLogger
from package import Package
from warehouse_manager import WarehouseManager
from datetime import date
import pytest

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
    test_get_total_fee()
    test_get_total_fee_by_range()
    test_wrong_date()
    print("All manual tests passed.")
