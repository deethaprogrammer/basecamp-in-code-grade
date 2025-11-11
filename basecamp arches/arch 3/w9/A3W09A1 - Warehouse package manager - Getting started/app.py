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
                    print(package.get_details())
                else:
                    print("Could not register new package.")
            else:
                print("Could not register new package.")
        elif menu_id == 'u':
            update = input("update ID,Distance:\n>")
            update_logic = update.split(",")
            if len(update_logic) != 2:
                print("wrong input in order to update you need to use\n'id,new_traveldistance'")
            else:
                ID_, New_distance = update.split(",")
                if not warehouse.update_destination(ID_, New_distance):
                    print("Could not update the package.")
                else:
                    print(package.get_details())
        elif menu_id == 'c':
            cancel_id = input("enter the ID that you want to cancel\n>")
            ID_ = warehouse.cancel_package(cancel_id)
            if ID_ == None:
                print("Could not cancel the package.")
            else:
                print(ID_.get_details())
        elif menu_id == 'v':
            Packages = warehouse.get_packages()
            if len(Packages) > 0:
                for p in Packages:
                    print(p.get_details())
            else:
                print("This warehouse is empty.")