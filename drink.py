# Drink class - represents individual drinks

class Drink:
    # Individual drink with ID, name, and price
    
    def __init__(self, drink_id: str, name: str, price: float):
        # Create new drink
        self.drink_id = drink_id
        self.name = name
        self.price = price
    
    def __str__(self):
        # String representation for display
        return f"{self.drink_id}: {self.name} - ${self.price:.2f}"
    
    def __repr__(self):
        # Detailed representation for debugging
        return f"Drink(id='{self.drink_id}', name='{self.name}', price={self.price})"
    
    def get_price(self) -> float:
        # Get drink price
        return self.price
    
    def get_name(self) -> str:
        # Get drink name
        return self.name
    
    def get_id(self) -> str:
        # Get drink ID
        return self.drink_id
