from warehouse_manager import WarehouseManager
manager = WarehouseManager()
all_ = manager.get_all_packages_by_delivery_date()
for file in all_:
    print(all_[file])