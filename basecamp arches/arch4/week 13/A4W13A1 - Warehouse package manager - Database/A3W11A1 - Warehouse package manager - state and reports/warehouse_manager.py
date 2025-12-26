from datetime import date
from warehouse_logger import WarehouseLogger
from package import Package
import os
import sys
import sqlite3
class WarehouseManager:
    def __init__(self):
        self.db_conn = sqlite3.connect(os.path.join(sys.path[0], "warehouse.db"), detect_types=sqlite3.PARSE_DECLTYPES)
        self.db_conn.execute("""
                             CREATE TABLE IF NOT EXISTS packages (
                                 id                TEXT      PRIMARY KEY,
                                 warehouse         TEXT      NOT NULL,
                                 weight            NUMERIC   NOT NULL,
                                 travel_distance   NUMERIC   NOT NULL,
                                 delivery_date     DATE      NOT NULL
                                 );
                                 """)
        self.logger = WarehouseLogger("MANAGER")
        pass
    
    def stores_package_id(self, package_id: str) -> bool:
        """
        return True if the package is stored in any warehouse, False other wise.
        Hint: there is a WarehouseLogger method that you can use for this!
        """
        for package in self.get_all_packages():
            if package.id == package_id:
                return True
        return False
        
    def get_all_packages(self) -> tuple[Package]:
        """
        Returns a tuple of all packages stored in all warehouses.
        Hint: there is a WarehouseLogger method that you can use for this!
        """
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT id, warehouse, weight, travel_distance, delivery_date FROM packages")
        rows = cursor.fetchall()
        packages = []
        for (id_, warehouse, weight, distance, delivery_date) in rows:
            packages.append(Package(id_, weight, distance, delivery_date))
        return tuple(packages)

    def get_total_fee(self) -> float:
        """
        Returns the total fee collected by Packets Now for all warehouses.
        You should use self.get_all_packages() in the method.
        """
        total_fee = 0.0
        packages = self.get_all_packages()
        for package in packages:
            total_fee += package.get_delivery_fee()
        return round(total_fee, 2)
    
    def get_total_fee_by_range(self, from_date: date, to_date: date) -> float:
        """
        Calculates the total fee collected by Packets Now between two dates for all
        warehouses, both inclusive (i.e., from 2025-04-04 to 2025-04-06 means you are
        calculating the total fee collected from packages delivered on 4, 5, and 6 April).
        You should use self.get_all_packages() in the method.
        """
        if to_date < from_date:
            return None
        fee = 0.0
        packages = self.get_all_packages_by_delivery_date()
        for pkg_tuple in packages.values():
            for package in pkg_tuple:
                Date = package.delivery_date
                if isinstance(Date, str):
                    Date = date.fromisoformat(Date)
                if from_date <= Date <= to_date:
                    fee += package.get_delivery_fee()
        return round(fee, 2)
    
    def get_all_packages_by_delivery_date(self) -> dict[date, tuple[Package, ...]]:
        all_packages = self.get_all_packages()
        packages_by_date: dict[date, list[Package]] = {}
        for pkg in all_packages:
            Date = pkg.delivery_date
            
            if isinstance(Date, str):
                Date = date.fromisoformat(Date)
            packages_by_date.setdefault(Date, []).append(pkg)
        return packages_by_date