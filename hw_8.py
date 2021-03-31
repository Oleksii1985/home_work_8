# Task 1
school = {"1a": 20, "1b": 22, "2a": 18, "2b": 15, "2c": 19, "3a": 14, "3b": 16}
school["1a"] = 23
school["3c"] = 20
del school["2b"]
total_people = sum(school.values())
print(school)
print(total_people)

# Task 2
a_dict = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth"}
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key
print(new_dict)
