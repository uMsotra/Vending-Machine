# VendingMachine class - handles all operations

from typing import Optional, Tuple
from drink import Drink
from stock import Stock


class VendingMachine:
    # Main vending machine controller
    
    def __init__(self):
        # Set up machine with stock and zero balance
        self.stock = Stock()
        self.current_balance = 0.0
        self.selected_drink: Optional[Drink] = None
        self._initialize_default_drinks()
    
    def _initialize_default_drinks(self) -> None:
        # Set up starting inventory
        default_drinks = [
            Drink("A1", "Coca Cola", 1.50),
            Drink("A2", "Pepsi", 1.50),
            Drink("A3", "Sprite", 1.25),
            Drink("B1", "Orange Juice", 2.00),
            Drink("B2", "Apple Juice", 2.00),
            Drink("B3", "Water", 1.00),
            Drink("C1", "Energy Drink", 2.50),
            Drink("C2", "Coffee", 1.75),
            Drink("C3", "Tea", 1.50)
        ]
        
        for drink in default_drinks:
            self.stock.add_drink(drink, quantity=10)
    
    def display_menu(self) -> str:
        # Show available drinks and current balance
        menu_lines = ["=== VENDING MACHINE MENU ==="]
        available_drinks = self.stock.get_available_drinks()
        
        if not available_drinks:
            menu_lines.append("Sorry, all drinks are out of stock!")
        else:
            for drink in available_drinks:
                quantity = self.stock.get_quantity(drink.get_id())
                menu_lines.append(f"{drink} (Stock: {quantity})")
        
        menu_lines.append(f"\nCurrent Balance: R{self.current_balance:.2f}")
        menu_lines.append("==========================")
        
        return "\n".join(menu_lines)
    
    def select_drink(self, drink_id: str) -> Tuple[bool, str]:
        # Select a drink for purchase
        try:
            drink = self.stock.get_drink(drink_id)
            
            if not self.stock.is_available(drink_id):
                return False, f"Sorry, {drink.get_name()} is out of stock."
            
            self.selected_drink = drink
            return True, f"Selected: {drink.get_name()} - R{drink.get_price():.2f}"
            
        except KeyError:
            return False, f"Invalid drink selection: {drink_id}"
    
    def insert_money(self, amount: float) -> Tuple[bool, str]:
        # Add money to current balance
        if amount <= 0:
            return False, "Please insert a positive amount."
        
        if amount not in [0.25, 0.50, 1.00, 2.00, 5.00]:
            return False, "Invalid amount. Please insert: R0.25, R0.50, R1.00, R2.00, or R5.00"
        
        self.current_balance += amount
        return True, f"Inserted: R{amount:.2f}. Balance: R{self.current_balance:.2f}"
    
    def check_balance(self) -> Tuple[bool, str]:
        # Check if balance covers selected drink
        if self.selected_drink is None:
            return False, "No drink selected."
        
        if self.current_balance >= self.selected_drink.get_price():
            return True, f"Balance sufficient for {self.selected_drink.get_name()}"
        else:
            needed = self.selected_drink.get_price() - self.current_balance
            return False, f"Insufficient balance. Need R{needed:.2f} more."
    
    def dispense_drink(self) -> Tuple[bool, str, float]:
        # Give drink and return change
        if self.selected_drink is None:
            return False, "No drink selected.", 0.0
        
        drink_id = self.selected_drink.get_id()
        drink_price = self.selected_drink.get_price()
        
        # Check if drink is still available
        if not self.stock.is_available(drink_id):
            return False, f"Sorry, {self.selected_drink.get_name()} is no longer available.", 0.0
        
        # Check if balance is sufficient
        if self.current_balance < drink_price:
            needed = drink_price - self.current_balance
            return False, f"Insufficient balance. Need R{needed:.2f} more.", 0.0
        
        # Dispense the drink
        if self.stock.dispense_drink(drink_id):
            change = self.current_balance - drink_price
            message = f"Enjoy your {self.selected_drink.get_name()}!"
            
            # Reset for next transaction
            self.current_balance = 0.0
            self.selected_drink = None
            
            return True, message, change
        else:
            return False, "Failed to dispense drink. Please try again.", 0.0
    
    def return_change(self) -> Tuple[bool, str, float]:
        # Return all money and reset transaction
        if self.current_balance <= 0:
            return False, "No money to return.", 0.0
        
        returned_amount = self.current_balance
        self.current_balance = 0.0
        self.selected_drink = None
        
        return True, f"Returned R{returned_amount:.2f}", returned_amount
    
    def get_stock_status(self) -> str:
        # Show detailed stock information
        status_lines = ["=== STOCK STATUS ==="]
        stock_summary = self.stock.get_stock_summary()
        
        for drink_name, quantity in stock_summary.items():
            status = "IN STOCK" if quantity > 0 else "OUT OF STOCK"
            status_lines.append(f"{drink_name}: {quantity} units ({status})")
        
        status_lines.append("===================")
        return "\n".join(status_lines)
    
    def reset_transaction(self) -> None:
        # Clear selection and balance
        self.selected_drink = None
        self.current_balance = 0.0
