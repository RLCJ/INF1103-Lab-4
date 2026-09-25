def calculate_tax(amount):
    tax = amount * 0.10
    return tax                                          # Calculate 10% tax


def process_delivery(current_total, new_value):     
    return current_total + new_value                    # Calculates and returns the updated total inventory

                                                    
def get_valid_input():                                  # Handle user input and validate it
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
        return "quit"

    # Input validation using .isdigit()
    if not user_input.isdigit():
        if user_input.startswith("-") and user_input[1:].isdigit():
            print("Error: Stock quantity cannot be negative. Please try again.")
        else:
            print("Error: Invalid entry. Please enter a positive whole number.")
        return None

    return int(user_input)


def generate_report(total_units, failed_attempts):
    print("\n" + "=" * 30)
    print("DELIVERY SUMMARY")
    print("=" * 30)
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")          # Prints the final summary report


def main():
    total_inventory = 0
    failed_entries = 0
    total_tax_collected = 0.0                                               # Initialize inventory and counters to zero


    # 2. Continuous loop
    while True:
        delivery_amount = get_valid_input()

        # Handle exit signal
        if delivery_amount == "quit":
            break

        # Handle invalid inputs
        if delivery_amount is None:
            failed_entries += 1
            continue

        # 3. Handle valid delivery
        total_inventory = process_delivery(total_inventory, delivery_amount)
        delivery_tax = calculate_tax(delivery_amount)
        total_tax_collected += delivery_tax

        print(f"Accepted: +{delivery_amount} units | Tax: ${delivery_tax:.2f} | Current Total: {total_inventory}")
        # displays 2 decimal places for tax collected


    generate_report(total_inventory, failed_entries)


if __name__ == "__main__":
    main()