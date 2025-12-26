from package import Package
from warehouse_logger import WarehouseLogger
from warehouse_manager import WarehouseManager
import sqlite3
import os
import sys
class Warehouse:
    def __init__(self, id: str = None, capacity: int = 10):
        """
        The constructor that receives the capacity, and sets packages to an empty dictionary.
        """
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
        self.id = id
        self.capacity = capacity
        self.packages: dict[str, Package] = {}
        self.logger = WarehouseLogger(self.id)
        self.manager = WarehouseManager()
        self.restore_state()
        pass

    def register_package(self, package: Package) -> bool:
        """
        Receives a package to store in the warehouse. Returns True on success, False otherwise.
        
        need to do:
            You should check if the maximum capacity is reached, and if the package is already stored here.
        """
        if (self.manager.stores_package_id(package.id) == True) or (len(self.packages) >= self.capacity):
            return False
            
        self.packages[package.id] = package
        try:
            self.db_conn.execute("""
                                 INSERT INTO packages (
                                     id,
                                     warehouse,
                                     weight,
                                     travel_distance,
                                     delivery_date) VALUES(?, ?, ?, ?, ?)
                                 """, (package.id, self.id, package.weight, package.travel_distance, package.delivery_date))
            self.db_conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
            
    
    def update_destination(self, package_id: str, New_distance: float) -> bool:
        """
        Receives a package ID and the distance to the new destination. Returns True on success, False otherwise.
        
        need to do:
            You should check if the package is stored in the warehouse.
            You should use the update_destination() method from the Package instance you want to update.
        """
        if package_id in self.packages:
            pkg = self.packages[package_id]
            pkg.update_destination(New_distance)
            self.db_conn.execute("""
                                 UPDATE packages SET travel_distance = ? WHERE id = ?
                                 """, (New_distance, package_id))
            self.db_conn.commit()
            return True
        return False

    def cancel_package(self, package_id: str) -> Package | None:
        """
        Receives the ID of the package to cancel.
        Returns the package instance that was cancelled on success, None otherwise.
        """
        if package_id in self.packages:
            removed = self.packages[package_id]
            del self.packages[package_id]
            self.db_conn.execute("DELETE FROM packages WHERE id= ?", (package_id,))
            self.db_conn.commit()
            return removed
        return None

    def get_package(self, package_id: str) -> Package | None:
        """
        Returns the package instance if it exists, None otherwise.
        """
        if package_id in self.packages.keys():
            return self.packages[package_id]
        else:
            return None
    
    def get_packages(self) -> tuple[Package, ...]:
        """
        Returns a tuple of all the packages stored in the warehouse.
        """
        return tuple(self.packages.values())

    def restore_state(self) -> None:
        """
        apply all transformations (i.e., packages linked to this warehouse get
        added/updated/cancelled) that are logged. when you restore the state,
        you should not log the actions again.
        assume that delivery dates will be in the future, so you will not have to perform
        any chks with the delivery date.
        """
        self.packages.clear()
        cursor = self.db_conn.execute("""
                                      SELECT id, warehouse, weight, travel_distance, delivery_date
                                      FROM packages WHERE warehouse = ?
                                      """, (self.id,))
        rows = cursor.fetchall()

        for (id_, warehouse, weight, distance, delivery_date) in rows:
            self.packages[id_] = Package(id_, weight, distance, delivery_date)
