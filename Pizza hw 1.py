import math

pizzaslices = 8
family = 4


person1 = int(input("how many slices of pizza do you eat: "))
person2 = int(input("how many slices of pizza do you eat: "))
person3 = int(input("how many slices of pizza do you eat: "))
person4 = int(input("how many slices of pizza do you eat: "))

#eat = int(input("how many slices of pizza does each family member eat "))


totalslices = person1 + person2 + person3 + person4

#print(totalslices)

wholepizza = math.ceil(totalslices/pizzaslices)

#print("whole pizzas to order", wholepizza)

leftbymodulo = totalslices%pizzaslices
#print(leftbymodulo)

print("total number of pizzas to buy", wholepizza)

print("total slices left", leftbymodulo)
