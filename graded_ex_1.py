# Dictionary of products
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

# Function to display product categories
def display_categories():
    print("Available categories:")
    for idx, category in enumerate(products.keys(), 1):
        print(f"{idx}. {category}")

# Function to display products in a selected category
def display_products(products_list):
    for idx, (product, price) in enumerate(products_list, 1):
        print(f"{idx}. {product} - ${price}")

# Function to display products sorted by price
def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))
    return sorted_products

# Function to add product to the shopping cart
def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

# Function to display the shopping cart
def display_cart(cart):
    print("Your shopping cart:")
    for product, price, quantity in cart:
        print(f"{product} - ${price} x {quantity} = ${price * quantity}")

# Function to generate receipt
def generate_receipt(name, email, cart, total_cost, address):
    print("\nReceipt:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Purchased items:")
    for product, price, quantity in cart:
        print(f"{product} - ${price} x {quantity} = ${price * quantity}")
    print(f"Total cost: ${total_cost}")
    print(f"Delivery address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

# Function to validate the user's name
def validate_name(name):
    if len(name.split()) == 2 and all(part.isalpha() for part in name.split()):
        return True
    return False

# Function to validate the email address
def validate_email(email):
    return "@" in email

# Main function
def main():
    cart = []
    total_cost = 0

    # Validate user name
    while True:
        name = input("Enter your full name (First Last): ")
        if validate_name(name):
            break
        print("Invalid name. Please enter a valid name with only alphabets (First and Last).")

    # Validate email
    while True:
        email = input("Enter your email address: ")
        if validate_email(email):
            break
        print("Invalid email. Please include '@' in your email address.")

    while True:
        display_categories()
        try:
            category_choice = int(input("Select a category by number: "))
            if 1 <= category_choice <= len(products):
                category_name = list(products.keys())[category_choice - 1]
                print(f"\nYou selected {category_name}. Here are the available products:")
                while True:
                    display_products(products[category_name])
                    print("\nOptions:")
                    print("1. Select a product to buy")
                    print("2. Sort products by price")
                    print("3. Go back to categories")
                    print("4. Finish shopping")
                    user_choice = input("Enter your choice (1-4): ")

                    if user_choice == "1":
                        product_choice = int(input("Enter the product number: ")) - 1
                        if 0 <= product_choice < len(products[category_name]):
                            quantity = int(input("Enter the quantity: "))
                            add_to_cart(cart, products[category_name][product_choice], quantity)
                            total_cost += products[category_name][product_choice][1] * quantity
                            print("Product added to cart.")
                        else:
                            print("Invalid product selection.")
                    elif user_choice == "2":
                        sort_order = int(input("Sort by: 1. Ascending 2. Descending: "))
                        sorted_products = display_sorted_products(products[category_name], sort_order)
                        display_products(sorted_products)
                    elif user_choice == "3":
                        break
                    elif user_choice == "4":
                        if cart:
                            display_cart(cart)
                            print(f"Total cost: ${total_cost}")
                            address = input("Enter delivery address: ")
                            generate_receipt(name, email, cart, total_cost, address)
                        else:
                            print("Thank you for using our portal. Hope you buy something next time!")
                        return
                    else:
                        print("Invalid option, please try again.")
            else:
                print("Invalid category selection.")
        except ValueError:
            print("Please enter a valid number.")

# Entry point
if __name__ == "__main__":
    main()
