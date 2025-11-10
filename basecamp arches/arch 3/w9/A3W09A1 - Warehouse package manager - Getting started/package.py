from datetime import date


class Package:
    def __init__(self, id: str, weight: float, travel_distance: float, delivery_date: date):
        self.id = id
        self.weight = weight
        self.travel_distance = travel_distance
        self.delivery_date = delivery_date
        pass
    
    def get_delivery_fee(self) -> float:
        """
        calculate delivery fee using:
        price = 0.50 + 0.08 * kg + 0.06 * km 
        round to 2 decimals
        """
        price = 0.50 + 0.08 * self.weight + 0.06 * self.travel_distance
        price = round(price, 2)
        return price
    
    def get_details(self) -> str:
        """
        returns as:
        Package(id={id}, weight={weight}, ...)
        """
        return Package(id={self.id}, weight={self.weight}, travel_distance={self.travel_distance}, delivery_date={self.delivery_date})
    
    def update_destination(self, ID, new_distance: float) -> None:
        """
        Receives the distance to the new destination.
        """