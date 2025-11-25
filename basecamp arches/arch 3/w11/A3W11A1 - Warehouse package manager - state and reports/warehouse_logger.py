from package import Package
from datetime import date, datetime
import os
import csv
import json
import sys

class WarehouseLogger:
    def __init__(self, id: str):
        self.id = id
        self.path = os.path.dirname(__file__)
        self.save_file = os.path.join(self.path, "warehouse_log.txt")
        self.state_file = f"{self.id}_state.json"
        pass
    
    def update_state(self, packages: dict[str, Package]) -> None:
        full_path = os.path.join(sys.path[0], self.state_file)
        
        package_dict = []
        for package in packages.values():
            package_dict.append(package.convert_to_dict())
        
        with open(full_path, "w", encoding="utf-8") as file:
            json.dump(package_dict, file, indent=4)
    
    def parse_package_from_state_file(self, json_object: dict) -> Package:
        return Package(
            id=json_object["id"],
            weight=float(json_object["weight"]),
            travel_distance=float(json_object["travel_distance"]),
            delivery_date=datetime.strptime(json_object["delivery_date"], "%Y-%m-%d").date()
        )
    
    def get_packages_from_state_file(self, state_file: str | None = None) -> dict[str, Package]:
        if state_file is None:
            state_file = f"{self.id}_state.json"
        full_path = os.path.join(sys.path[0], state_file)
        packages: dict[str, Package] = {}
        
        try:
            with open(full_path, "r", encoding="utf-8") as read:
                data = json.load(read)
                for obj in data:
                    pkg = self.parse_package_from_state_file(obj)
                    if isinstance(pkg.delivery_date, str):
                        pkg.delivery_date = date.fromisoformat(pkg.delivery_date)
                    packages[pkg.id] = pkg
                return packages
        except FileNotFoundError as fnf:
            return {}
        return packages
    def get_packages_from_all_state_files(self) -> dict[str, Package]:
        Packages: dict[str, Package] = {}
        
        for filename in os.listdir(self.path):
            if filename.endswith("_state.json"):
                warehouse_packages = self.get_packages_from_state_file(filename)
                if warehouse_packages is None:
                    warehouse_packages = {}
                Packages.update(warehouse_packages)
        return Packages
    
    def generate_summary_per_date_file(self, packages: dict[date, tuple[Package, ...]]) -> None:
        """
        Generates a CSV file with summary_per_date.csv as filename and with date, num_packages, fee as columns, separated by semicolons.
        """
        full_path = os.path.join(sys.path[0], 'summary_per_date.csv')
        with open(full_path, "w", encoding="utf-8") as csvfile:
            writer= csv.writer(csvfile, delimiter=";")
            writer.writerow(["date", "num_packages", "fee"])
            
            for delivery_date, pkg_tuple in packages.items():
                num_packages = len(pkg_tuple)
                total_fee = sum(pkg.get_delivery_fee() for pkg in pkg_tuple)
                writer.writerow([delivery_date.strftime("%Y-%m-%d"), num_packages, f"{total_fee:.2f}"])