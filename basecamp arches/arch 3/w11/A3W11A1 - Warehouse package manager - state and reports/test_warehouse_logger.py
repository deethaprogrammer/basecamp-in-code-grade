from warehouse_logger import WarehouseLogger
from package import Package
from datetime import date
import pytest
import os

def test_update_and_restore_state():
    test_id = "test"
    logger = WarehouseLogger(test_id)
    logger.state_file = f"{test_id}_state.json"
    pkg_1 = Package("p001", 10.0, 150.0, date(2025, 11, 18))
    pkg_2 = Package("p002", 5.0, 50.0, date(2025, 11, 20))
    packages = {
        pkg_1.id: pkg_1,
        pkg_2.id: pkg_2,
    }
    logger.update_state(packages)
    path = os.path.dirname(__file__)
    state_path = os.path.join(path, logger.state_file)
    assert os.path.exists(state_path)
    restored = logger.get_packages_from_state_file(logger.state_file)
    assert "p001" in restored
    assert "p002" in restored
    assert restored["p001"].weight == 10.0
    assert restored["p002"].travel_distance == 50.0