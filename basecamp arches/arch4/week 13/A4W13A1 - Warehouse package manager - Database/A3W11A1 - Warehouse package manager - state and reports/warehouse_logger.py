from package import Package
from datetime import date, datetime
import os
import csv
import sys

class WarehouseLogger:
    def __init__(self, id: str):
        self.id = id
        self.path = os.path.dirname(__file__)
        self.save_file = os.path.join(self.path, "warehouse_log.txt")
        
    
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
    
    def generate_most_profitable_packages_file(self, packages: tuple[Package, ...], num_packages: int = 10) -> bool:
        if not isinstance(num_packages, int) or num_packages <= 0:
            return False
        try:
            sorted_packages = sorted(
                packages,
                key=lambda pkg: pkg.get_delivery_fee(),
                reverse=True
            )
            top_package = sorted_packages[:num_packages]
            full_path = os.path.join(sys.path[0], "most_profitable_packages.csv")
            with open(full_path, "w", encoding="utf-8", newline="") as csv_file:
                writer = csv.writer(csv_file, delimiter=";")
                writer.writerow(["package_id", "date", "fee"])
                
                for pkg in top_package:
                    writer.writerow([
                        pkg.id,
                        pkg.delivery_date.strftime("%Y-%m-%d"),
                        f"{pkg.get_delivery_fee():.2f}"
                    ])
            return True
        except Exception:
            return False