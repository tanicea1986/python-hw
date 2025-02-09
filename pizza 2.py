# Program for everyone eating the same number of slices
slices_per_person = int(input("Enter number of slices each person eats: "))
total_slices = 4 * slices_per_person
pizzas_needed = total_slices // 8 + (1 if total_slices % 8 > 0 else 0)
leftover_slices = (pizzas_needed * 8) - total_slices

print(f"Pizzas needed: {pizzas_needed}, Leftover slices: {leftover_slices}")

# Program for everyone eating a different number of slices
person1 = int(input("Enter slices for person 1: "))
person2 = int(input("Enter slices for person 2: "))
person3 = int(input("Enter slices for person 3: "))
person4 = int(input("Enter slices for person 4: "))

total_slices = person1 + person2 + person3 + person4
pizzas_needed = total_slices // 8 + (1 if total_slices % 8 > 0 else 0)
leftover_slices = (pizzas_needed * 8) - total_slices

print(f"Pizzas needed: {pizzas_needed}, Leftover slices: {leftover_slices}")
