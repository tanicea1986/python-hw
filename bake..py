def bakery_sales():
    muffins = 10
    cupcakes = 10
    
    while True:
        item = input("Enter item bought (muffin/cupcake) or 0 to stop: ").strip().lower()
        
        if item == "0":
            break
        elif item == "muffin":
            if muffins > 0:
                muffins -= 1
            else:
                print("Out of stock")
        elif item == "cupcake":
            if cupcakes > 0:
                cupcakes -= 1
            else:
                print("Out of stock")
        else:
            print("Invalid input")
    
    print(f"muffins: {muffins} cupcakes: {cupcakes}")

# Run the function
bakery_sales()
