# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# y = str(thisdict["year"])
# print("Ford " + x + " " + y)


# z = thisdict.keys()
# print(z)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"
car["weight"] = "1000kg"

print(x) #after the change

c = car["weight"]
print(c)
