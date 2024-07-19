def generate_invoice():
    print("Welcome to the Invoice Generator")
    
    # Customer information
    customer_name = input("Enter customer name: ")
    customer_address = input("Enter customer address: ")
    
    # Item details
    items = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        item_quantity = int(input(f"Enter quantity for {item_name}: "))
        item_price = float(input(f"Enter price for {item_name}: "))
        items.append({"name": item_name, "quantity": item_quantity, "price": item_price})
    
    # Generate invoice
    print("\n\n----- Invoice -----")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Customer Name: {customer_name}")
    print(f"Customer Address: {customer_address}")
    print("\nItems:")
    total = 0
    for item in items:
        item_total = item["quantity"] * item["price"]
        total += item_total
        print(f"{item['name']} - Quantity: {item['quantity']} - Price: ${item['price']} - Total: ${item_total}")
    
    print(f"\nTotal Amount: ${total}")
    print("-------------------")
    print("Thank you for your business!")

if __name__ == "__main__":
    generate_invoice()