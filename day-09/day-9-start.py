programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again"}



print(programming_dictionary["Bug"])

#adding new engry
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

empty_dictionary = {}

#wipe an existiong dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#edit an item in dictionary
programming_dictionary["Bug"] = "edited"
print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


