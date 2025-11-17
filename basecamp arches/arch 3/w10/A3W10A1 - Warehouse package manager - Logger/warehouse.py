from package import Package
from warehouse_logger import WarehouseLogger
from warehouse_manager import WarehouseManager
class Warehouse:
    def __init__(self, id: str = None, capacity: int = 10):
        """
        The constructor that receives the capacity, and sets packages to an empty dictionary.
        """
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
            
        else:
            self.packages[package.id] = package
            self.logger.log_action("register", package)
            return True
    
    def update_destination(self, package_id: str, new_distance: float) -> bool:
        """
        Receives a package ID and the distance to the new destination. Returns True on success, False otherwise.
        
        need to do:
            You should check if the package is stored in the warehouse.
            You should use the update_destination() method from the Package instance you want to update.
        """
        package = self.get_package(package_id)
        if package is None:
            return False
        
        package.update_destination(new_distance)
        
        if self.packages[package_id].travel_distance == new_distance:
            self.logger.log_action("update", package)
            return True
        return False
        
        
    def cancel_package(self, package_id: str) -> Package | None:
        """
        Receives the ID of the package to cancel.
        Returns the package instance that was cancelled on success, None otherwise.
        """
        data_package = self.get_package(package_id)
        if data_package != None:
            self.packages.pop(package_id)
            self.logger.log_action("cancel", data_package)
            return data_package
        else:
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
        if self.id != None:
            self.packages = self.logger.get_all_packages_from_log_file(only_current_warehouse=True)
