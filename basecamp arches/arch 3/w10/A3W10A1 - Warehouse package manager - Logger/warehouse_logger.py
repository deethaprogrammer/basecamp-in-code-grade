from package import Package
from datetime import date, datetime
import os

class WarehouseLogger:
    def __init__(self, id: str):
        self.ID = id
        path = os.path.dirname(__file__)
        self.save_file = os.path.join(path, "warehouse_log.txt")
        pass
    
    def log_action(self, action: str, package: Package) -> None:
        valid_actions = ["register", "update", "cancel"]
        if action not in valid_actions:
            raise ValueError("Invalid action type")
        
        with open(self.save_file, "a") as file:
            if action == "register":
                line = f"{self.ID};register;{package.id};{package.weight};{package.travel_distance};{package.delivery_date}"
            elif action == "update":
                line = f"{self.ID};update;{package.id};{package.travel_distance}"
            elif action == "cancel":
                line = f"{self.ID};cancel;{package.id}"
            file.write(line + "\n")
            
    def get_all_packages_from_log_file(self, only_current_warehouse: bool = True) -> dict[str, Package]:
        packages: dict[str, Package] = {}
        
        try:
            with open(self.save_file, "r") as read_file:
                for line in read_file:
                    line = line.strip()
                    if not line:
                        continue
                    
                    parts = line.split(";")
                    warehouse_id, action = parts[0], parts[1]

                    if only_current_warehouse and warehouse_id != self.ID:
                        continue
                        
                    if action == "register":
                        package = self.parse_package_from_register_log_line(line)
                        packages[package.id] = package
                    
                    elif action == "update":
                        package_id = parts[2]
                        new_distance = float(parts[3])
                        if package_id in packages:
                            packages[package_id].update_destination(new_distance)
                    
                    elif action == "cancel":
                        package_id = parts[2]
                        packages.pop(package_id, None)
        except FileNotFoundError:
            pass
        
        return packages
    
    def parse_package_from_register_log_line(self, log_line: str) -> Package:
        parts = log_line.strip().split(";")
        package_id = parts[2]
        package_weight = float(parts[3])
        package_distance = float(parts[4])
        package_delivery_date = datetime.strptime(parts[5], "%Y-%m-%d").date()
        return Package(package_id, package_weight, package_distance, package_delivery_date)