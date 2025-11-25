from warehouse_logger import WarehouseLogger
from package import Package
from datetime import date
import pytest

def test_stores_package_id():
    logger = WarehouseLogger("test")
    logger.save_file = "test_log.txt"
    
    with open(logger.save_file, "w") as f:
        f.write("")
        
    package1 = Package("p001", 10.0, 150.0, date(2025, 11, 18))
    package2 = Package("p002", 5.0, 50.0, date(2025, 11, 20))
    logger.log_action("register", package1)
    logger.log_action("register", package2)
    
    packages = logger.get_all_packages_from_log_file()
    assert "p001" in packages
    assert "p002" in packages
    assert packages["p001"].weight == 10.0
    assert packages["p002"].travel_distance == 50.0
