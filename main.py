# Main program - handles user interface

from vending_machine import VendingMachine


def display_welcome_message():
    # Show welcome screen and instructions
    print("=" * 50)
    print("    WELCOME TO THE VENDING MACHINE SIMULATOR")
    print("=" * 50)
    print("\nAvailable Commands:")
    print("  menu     - Show available drinks")
    print("  select   - Select a drink (e.g., 'select A1')")
    print("  insert   - Insert money (e.g., 'insert 1.00')")
    print("  buy      - Purchase the selected drink")
    print("  balance  - Check current balance")
    print("  return   - Return all money")
    print("  stock    - Show stock status (admin)")
    print("  help     - Show this help message")
    print("  quit     - Exit the program")
    print("\nAccepted money amounts: R0.25, R0.50, R1.00, R2.00, R5.00")
    print("-" * 50)


def handle_select_command(vending_machine: VendingMachine, args: list) -> None:
    # Process drink selection
    if not args:
        print("Usage: select <drink_id>")
        print("Example: select A1")
        return
    
    drink_id = args[0].upper()
    success, message = vending_machine.select_drink(drink_id)
    print(message)


def handle_insert_command(vending_machine: VendingMachine, args: list) -> None:
    # Process money insertion
    if not args:
        print("Usage: insert <amount>")
        print("Example: insert 1.00")
        print("Accepted amounts: R0.25, R0.50, R1.00, R2.00, R5.00")
        return
    
    try:
        amount = float(args[0])
        success, message = vending_machine.insert_money(amount)
        print(message)
    except ValueError:
        print("Invalid amount. Please enter a valid number.")


def handle_buy_command(vending_machine: VendingMachine) -> None:
    # Process drink purchase
    success, message, change = vending_machine.dispense_drink()
    print(message)
    
    if success and change > 0:
        print(f"Change returned: R{change:.2f}")
    elif success and change == 0:
        print("Exact payment - no change needed.")


def handle_balance_command(vending_machine: VendingMachine) -> None:
    # Show balance and selection info
    sufficient, message = vending_machine.check_balance()
    print(message)
    
    if vending_machine.selected_drink:
        print(f"Selected drink: {vending_machine.selected_drink.get_name()}")
        print(f"Price: R{vending_machine.selected_drink.get_price():.2f}")


def handle_return_command(vending_machine: VendingMachine) -> None:
    # Process money return
    success, message, amount = vending_machine.return_change()
    print(message)


def main():
    # Main program loop
    vending_machine = VendingMachine()
    
    display_welcome_message()
    print(vending_machine.display_menu())
    
    while True:
        print("\n" + "-" * 30)
        command = input("Enter command: ").strip().lower()
        
        if not command:
            continue
        
        parts = command.split()
        cmd = parts[0]
        args = parts[1:] if len(parts) > 1 else []
        
        if cmd == "quit" or cmd == "exit":
            print("Thank you for using the Vending Machine Simulator!")
            break
        
        elif cmd == "help":
            display_welcome_message()
        
        elif cmd == "menu":
            print(vending_machine.display_menu())
        
        elif cmd == "select":
            handle_select_command(vending_machine, args)
        
        elif cmd == "insert":
            handle_insert_command(vending_machine, args)
        
        elif cmd == "buy":
            handle_buy_command(vending_machine)
        
        elif cmd == "balance":
            handle_balance_command(vending_machine)
        
        elif cmd == "return":
            handle_return_command(vending_machine)
        
        elif cmd == "stock":
            print(vending_machine.get_stock_status())
        
        else:
            print(f"Unknown command: '{cmd}'")
            print("Type 'help' to see available commands.")


if __name__ == "__main__":
    main()
