# Initialize the number of baked goods
muffins = 10
cupcakes = 10

while True:
    item = input("Enter purchase (muffin/cupcake) or '0' to stop: ").strip().lower()
    
    if item == "0":
        break
    elif item == "muffin":
        if muffins > 0:
            muffins -= 1
        else:
            print("Muffins are out of stock")
    elif item == "cupcake":
        if cupcakes > 0:
            cupcakes -= 1
        else:
            print("Cupcakes are out of stock")
    else:
        print("Invalid input. Please enter 'muffin', 'cupcake', or '0'.")

print(f"Remaining stock - Muffins: {muffins}, Cupcakes: {cupcakes}")
