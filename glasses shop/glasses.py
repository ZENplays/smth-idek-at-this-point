import os

def load_inventory(file_path):
    inventory = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                print(f"Reading line: {line.strip()}")  # Debugging output
                parts = line.strip().split(',')
                print(f"Split parts: {parts}")  # Print parsed parts
                if len(parts) == 5:
                    model, g_type, brand, price, stock = parts
                    try:
                        inventory.append({
                            'model': model.strip(),
                            'type': g_type.strip(),
                            'brand': brand.strip(),
                            'price': float(price.strip()),
                            'stock': int(stock.strip())
                        })
                    except ValueError as e:
                        print(f"❌ Error converting values: {e} (Line: {line.strip()})")
    else:
        print(f"❌ File {file_path} not found.")
    print(f"Final inventory list: {inventory}")  # Debugging output
    return inventory


def save_inventory(file_path, inventory):
    with open(file_path, 'w') as file:
        for item in inventory:
            file.write(f"{item['model']},{item['type']},{item['brand']},{item['price']},{item['stock']}\n")

def display_inventory(inventory):
    if not inventory:
        print("\n❌ No glasses available.")
        return
    print("\nAvailable Glasses:")
    print("Model | Type | Brand | Price | Stock")
    print("-" * 40)
    for item in inventory:
        print(f"{item['model']} | {item['type']} | {item['brand']} | ${item['price']:.2f} | {item['stock']}")

def search_glasses(inventory, key, value):
    results = [item for item in inventory if str(item[key]).lower() == value.lower()]
    return results

def buy_glasses(inventory, model):
    for item in inventory:
        if item['model'].lower() == model.lower():
            if item['stock'] > 0:
                item['stock'] -= 1
                print(f"\n✅ You have purchased {item['model']} ({item['brand']} - {item['type']}) for ${item['price']:.2f}")
                return True
            else:
                print("\n❌ Sorry, this model is out of stock!")
                return False
    print("\n❌ Model not found!")
    return False

def main():
    file_path = r"D:\\UNI FILE\\PYTHON files\\glasses shop\\glasses.txt"
    
    # Force read and print contents for debugging
    with open(file_path, 'r') as file:
    print("📄 File contents (with line numbers):")
    for i, line in enumerate(file, 1):
        print(f"{i}: {line.strip()}")

    
    inventory = load_inventory(file_path)
    if not inventory:
        print("\n❌ Inventory is empty! Check file format.")

    while True:
        print("\n1. View Glasses\n2. Search Glasses\n3. Buy Glasses\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            key = input("Search by (model/type/brand): ").lower()
            value = input("Enter value: ")
            results = search_glasses(inventory, key, value)
            if results:
                display_inventory(results)
            else:
                print("\n❌ No results found.")
        elif choice == '3':
            model = input("Enter the model name of the glasses you want to buy: ")
            if buy_glasses(inventory, model):
                save_inventory(file_path, inventory)  # Save changes after purchase
        elif choice == '4':
            print("\n👋 Thank you for visiting our shop!")
            break
        else:
            print("\n❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
