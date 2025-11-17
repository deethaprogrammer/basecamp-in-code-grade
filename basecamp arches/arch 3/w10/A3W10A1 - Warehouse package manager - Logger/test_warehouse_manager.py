from warehouse_manager import WarehouseManager
from datetime import date
test = WarehouseManager()
print(test.get_total_fee_by_range(date(2025, 5, 20), date(2025, 5, 21)))