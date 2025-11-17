from warehouse import Warehouse
from package import Package
from datetime import datetime, date
from warehouse import WarehouseManager
menu = """
[R] Register a new package
[U] Update a package's destination
[C] Cancel package delivery
[V] View all packages in the warehouse
[F] Get total fee between two dates
[Q] Quit
"""
# Write your application logic here
if __name__ == "__main__":
    manager = WarehouseManager()
    warehouse = Warehouse("schiedam")
    while True:
        warehouse.restore_state()
        menu_id = input(menu + "\n>").lower()
        if menu_id == 'q':
            quit()
        elif menu_id == 'r':
            Register_val = input("Enter all attributes in one line seperated by comma\n>")
            if len(Register_val.split(',')) == 4:
                id_, weight, travel, deliver = Register_val.split(',')
                try:
                    weight = float(weight)
                    travel = float(travel)
                    deliver = datetime.strptime(deliver.strip(), "%Y-%m-%d").date()
                    package = Package(id_, weight, travel, deliver)
                    if warehouse.register_package(package):
                        print(package.get_details())
                    else:
                        print("Could not register new package.")
                except ValueError:
                    print("wrong input\nenter like this: id,weight,travel_distance,delivery_date  all , seperated and weight in kg and travel distance in km the delivery date is in year-month-day")
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
                    updated_package = warehouse.get_package(ID_)
                    print(updated_package.get_details())
        elif menu_id == 'c':
            cancel_id = input("enter the ID that you want to cancel\n>")
            cancceled = warehouse.cancel_package(cancel_id)
            if cancceled is None:
                print("Could not cancel the package.")
            else:
                print(cancceled.get_details())
        elif menu_id == 'v':
            Packages = warehouse.get_packages()
            if len(Packages) > 0:
                for p in Packages:
                    print(p.get_details())
            else:
                print("This warehouse is empty.")
        elif menu_id == 'f':
            between = input("between wich date's input it like: yyyy-mm-dd,yyyy-mm-dd so use the , as a seperator\n>")
            from_date, to_date = between.strip().split(',')
            from_date = datetime.strptime(from_date.strip(), "%Y-%m-%d").date()
            to_date = datetime.strptime(to_date.strip(), "%Y-%m-%d").date()
            fee = manager.get_total_fee_by_range(from_date, to_date)
            if fee == None:
                print("Could not calculate the total fee.")
            else:
                print(f"Collected fees: {fee:.2f} EUR")