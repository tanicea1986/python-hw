muffins = 10
cupcakes = 10

while True:
    order = input("Enter order (muffin/cupcake) or '0' to stop: ").strip().lower()
    
    if order == "0":
        break
    elif order == "muffin":
        if muffins > 0:
            muffins -= 1
        else:
            print("Out of stock")
    elif order == "cupcake":
        if cupcakes > 0:
            cupcakes -= 1
        else:
            print("Out of stock")
    else:
        print("Invalid input. Please enter 'muffin', 'cupcake', or '0' to stop.")

print(f"muffins: {muffins} cupcakes: {cupcakes}")


