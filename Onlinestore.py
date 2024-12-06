inventory = [
    {"id": 1, "name": "Macbook", "price": 999.99},
    {"id": 2, "name": "iPhone", "price": 599.99},
    {"id": 3, "name": "Airpod", "price": 89.99}
]

# Shopping cart
cart = []

def display_products():
    """Display available products."""
    print("\nAvailable Products:")
    for product in inventory:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}")

def add_to_cart():
    """Add items to the shopping cart."""
    try:
        product_id = int(input("Enter the Product ID to add to the cart: "))
        quantity = int(input("Enter the quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        product = next((item for item in inventory if item['id'] == product_id), None)

        if product:
            cart_item = next((item for item in cart if item['id'] == product_id), None)
            if cart_item:
                cart_item['quantity'] += quantity
            else:
                cart.append({"id": product_id, "name": product['name'], "price": product['price'], "quantity": quantity})
            print(f"Added {quantity} x {product['name']} to the cart.")
        else:
            print("Invalid Product ID.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

def view_cart():
    """View the contents of the shopping cart."""
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\nYour Shopping Cart:")
    total = 0
    for item in cart:
        item_total = item['quantity'] * item['price']
        total += item_total
        print(f"Name: {item['name']}, Quantity: {item['quantity']}, Total: ${item_total:.2f}")
    print(f"Overall Total: ${total:.2f}")

def remove_from_cart():
    """Remove items from the shopping cart."""
    try:
        product_id = int(input("Enter the Product ID to remove from the cart: "))
        cart_item = next((item for item in cart if item['id'] == product_id), None)

        if cart_item:
            cart.remove(cart_item)
            print(f"Removed {cart_item['name']} from the cart.")
        else:
            print("Item not found in the cart.")

    except ValueError:
        print("Invalid input. Please enter a numeric Product ID.")

def complete_purchase():
    """Complete the purchase."""
    if not cart:
        print("\nYour cart is empty. Add items to proceed.")
        return

    total = sum(item['quantity'] * item['price'] for item in cart)
    print(f"\nTotal Price: ${total:.2f}")
    confirm = input("Do you want to proceed with the purchase? (yes/no): ").strip().lower()

    if confirm == 'yes':
        print("Purchase successful! Thank you for shopping.")
        cart.clear()
    else:
        print("Purchase canceled.")

def login():
    """User login simulation."""
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "AV" and password == "coolguy":
        print("Login successful! Welcome to the store.")
        return True
    else:
        print("Invalid username or password.")
        return False

def menu():
    """Display the menu and handle user actions."""
    while True:
        print("\nMenu:")
        print("1. View products")
        print("2. Add items to your cart")
        print("3. View your cart")
        print("4. Remove items from your cart")
        print("5. Complete purchase")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                display_products()
            elif choice == 2:
                add_to_cart()
            elif choice == 3:
                view_cart()
            elif choice == 4:
                remove_from_cart()
            elif choice == 5:
                complete_purchase()
            elif choice == 6:
                print("Thank you for visiting! Goodbye.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    if login():
        menu()
