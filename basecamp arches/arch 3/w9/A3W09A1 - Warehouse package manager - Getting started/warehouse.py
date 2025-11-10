from package import Package

class Warehouse:
    def __init__(self, capacity: int = 10):
        """
        The constructor that receives the capacity, and sets packages to an empty dictionary.
        """
        self.capacity = capacity
        self.packages: dict[str, Package] = {}
        pass

    def register_package(self, package: Package) -> bool:
        """
        Receives a package to store in the warehouse. Returns True on success, False otherwise.
        
        need to do:
            You should check if the maximum capacity is reached, and if the package is already stored here.
        """
        if (len(self.packages) >= self.capacity) or (package.id in self.packages):
            return False
        else:
            self.packages[package.id] = package
            return True
    
    def update_destination(self, package_id: str, new_distance: float) -> bool:
        """
        Receives a package ID and the distance to the new destination. Returns True on success, False otherwise.
        
        need to do:
            You should check if the package is stored in the warehouse.
            You should use the update_destination() method from the Package instance you want to update.
        """
        if package_id in self.packages.keys():
            pass
    
    def cancel_package(self, package_id: str) -> Package | None:
        """
        Receives the ID of the package to cancel.
        Returns the package instance that was cancelled on success, None otherwise.
        """
        pass
    
    def get_package(self, package_id: str) -> Package | None:
        """
        Returns the package instance if it exists, None otherwise.
        """
        pass
    
    def get_packages(self) -> tuple[Package, ...]:
        """
        Returns a tuple of all the packages stored in the warehouse.
        """
        return tuple(self.packages.values())
        pass
    
