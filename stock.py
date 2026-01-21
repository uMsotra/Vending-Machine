# Stock class - manages drink inventory

from typing import Dict, List
from drink import Drink


class Stock:
    # Manages drink quantities and availability
    
    def __init__(self):
        # Start with empty inventory
        self.inventory: Dict[str, Drink] = {}
        self.quantities: Dict[str, int] = {}
    
    def add_drink(self, drink: Drink, quantity: int = 10) -> None:
        # Add drink to inventory
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        self.inventory[drink.get_id()] = drink
        self.quantities[drink.get_id()] = quantity
    
    def get_drink(self, drink_id: str) -> Drink:
        # Get drink by ID
        if drink_id not in self.inventory:
            raise KeyError(f"Drink '{drink_id}' not found in inventory")
        return self.inventory[drink_id]
    
    def get_quantity(self, drink_id: str) -> int:
        # Get drink quantity
        return self.quantities.get(drink_id, 0)
    
    def is_available(self, drink_id: str) -> bool:
        # Check if drink is in stock
        return self.get_quantity(drink_id) > 0
    
    def dispense_drink(self, drink_id: str) -> bool:
        # Remove one drink from stock
        if self.is_available(drink_id):
            self.quantities[drink_id] -= 1
            return True
        return False
    
    def get_available_drinks(self) -> List[Drink]:
        # Get all drinks that are in stock
        return [
            self.inventory[drink_id] 
            for drink_id in self.inventory 
            if self.is_available(drink_id)
        ]
    
    def get_all_drinks(self) -> List[Drink]:
        # Get all drinks in inventory
        return list(self.inventory.values())
    
    def restock_drink(self, drink_id: str, additional_quantity: int) -> None:
        # Add more quantity to existing drink
        if drink_id not in self.inventory:
            raise KeyError(f"Drink '{drink_id}' not found in inventory")
        if additional_quantity <= 0:
            raise ValueError("Additional quantity must be positive")
        
        self.quantities[drink_id] += additional_quantity
    
    def get_stock_summary(self) -> Dict[str, int]:
        # Get summary of all stock levels
        return {
            self.inventory[drink_id].get_name(): self.quantities[drink_id]
            for drink_id in self.inventory
        }
