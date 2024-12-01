import datetime
import os

# Adjust the path to point to the correct location of your text file
FURNITURE_FILE = 'C:/Users/shiri/OneDrive/Desktop/Python/coursework-demo/furniture_data.txt'
INVOICE_FOLDER = 'C:/Users/shiri/OneDrive/Desktop/Python/coursework-demo/invoices/'

# Ensure the invoice directory exists
os.makedirs(INVOICE_FOLDER, exist_ok=True)

def read_furniture_data():
    furniture = []
    with open(FURNITURE_FILE, 'r') as file:
        for line in file:
            data = line.strip().split()
            if len(data) >= 5:
                furniture.append({
                    'id': data[0],
                    'manufacturer': data[1],
                    'product_name': ' '.join(data[2:-2]),
                    'quantity': int(data[-2]),
                    'price': float(data[-1])
                })
    return furniture

def write_furniture_data(furniture):
    with open(FURNITURE_FILE, 'w') as file:
        for item in furniture:
            file.write(f"{item['id']} {item['manufacturer']} {item['product_name']} {item['quantity']} {item['price']}\n")

def display_furniture(furniture):
    print("Available Furniture:")
    for item in furniture:
        print(f"ID: {item['id']}, Manufacturer: {item['manufacturer']}, Product: {item['product_name']}, Quantity: {item['quantity']}, Price: ${item['price']}")

def generate_invoice(invoice_data, is_purchase):
    date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{INVOICE_FOLDER}invoice_{date_time}.txt"
    with open(filename, 'w') as file:
        file.write(f"Date and Time: {date_time}\n")
        file.write(f"Customer/Employee Name: {invoice_data['name']}\n")
        file.write("Items:\n")
        total_amount = 0
        for item in invoice_data['items']:
            file.write(f"ID: {item['id']}, Product: {item['product_name']}, Quantity: {item['quantity']}, Price: ${item['price']}, Total: ${item['quantity'] * item['price']}\n")
            total_amount += item['quantity'] * item['price']
        if is_purchase:
            vat = total_amount * 0.13
            total_amount += vat
            file.write(f"VAT (13%): ${vat}\n")
        if 'shipping_cost' in invoice_data:
            total_amount += invoice_data['shipping_cost']
            file.write(f"Shipping Cost: ${invoice_data['shipping_cost']}\n")
        file.write(f"Total Amount: ${total_amount}\n")
    print(f"Invoice generated: {filename}")

def purchase_furniture(furniture):
    name = input("Enter the customer's name: ")
    items = []
    while True:
        display_furniture(furniture)
        item_id = input("Enter the ID of the furniture to purchase: ")
        quantity = int(input("Enter the quantity to purchase: "))
        for item in furniture:
            if item['id'] == item_id:
                if item['quantity'] >= quantity:
                    item['quantity'] -= quantity
                    items.append({
                        'id': item['id'],
                        'product_name': item['product_name'],
                        'quantity': quantity,
                        'price': item['price']
                    })
                else:
                    print(f"Insufficient stock for {item['product_name']}. Available quantity: {item['quantity']}")
                break
        else:
            print(f"No furniture found with ID: {item_id}")
        more = input("Do you want to purchase more items? (yes/no): ")
        if more.lower() != 'yes':
            break
    shipping_cost = float(input("Enter the shipping cost: "))
    generate_invoice({'name': name, 'items': items, 'shipping_cost': shipping_cost}, True)
    write_furniture_data(furniture)

def order_furniture(furniture):
    name = input("Enter the employee's name: ")
    items = []
    while True:
        item_id = input("Enter the ID of the furniture to order: ")
        quantity = int(input("Enter the quantity to order: "))
        for item in furniture:
            if item['id'] == item_id:
                item['quantity'] += quantity
                items.append({
                    'id': item['id'],
                    'product_name': item['product_name'],
                    'quantity': quantity,
                    'price': item['price']
                })
                break
        else:
            print(f"No furniture found with ID: {item_id}")
        more = input("Do you want to order more items? (yes/no): ")
        if more.lower() != 'yes':
            break
    generate_invoice({'name': name, 'items': items}, False)
    write_furniture_data(furniture)

def main():
    while True:
        furniture = read_furniture_data()
        print("\n1. Display Furniture")
        print("\n2. Purchase Furniture")
        print("\n3. Order Furniture")
        print("\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_furniture(furniture)
        elif choice == '2':
            purchase_furniture(furniture)
        elif choice == '3':
            order_furniture(furniture)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
