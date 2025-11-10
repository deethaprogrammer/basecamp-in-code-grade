from warehouse import Warehouse
from package import Package
menu = """
[R] Register a new package
[U] Update a package's destination
[C] Cancel package delivery
[V] View all packages in the warehouse
[Q] Quit
"""
# Write your application logic here
if __name__ == "__main__":
    warehouse = Warehouse()
    while True:
        menu_id = input(menu + "\n>").lower()
        if menu_id == 'q':
            quit()
        elif menu_id == 'r':
            Register_val = input("Enter all attributes in one line seperated by comma\n>")
            if len(Register_val.split(',')) == 4:
                id_, weight, travel, deliver = Register_val.split(',')
                package = Package(id_, weight, travel, deliver)
                if warehouse.register_package(package):
                    print(str(package.get_details()))
                else:
                    print("Could not register new package.")
            else:
                print("Could not register new package.")
        elif menu_id == 'u':
            ID, New_distance = input("ID:\n>").split(',')
            warehouse.update_destination(ID, New_distance)
            pass
        elif menu_id == 'c':
            pass
        elif menu_id == 'v':
            Packages = warehouse.get_packages()
            for p in Packages:
                print(p.get_details())