# input_dict = {}
# input_dict["Name"] = "Vs code"
# input_dict["Owner"] = ["Microsoft", "Bill Gates"]
# input_dict["age"] = [1,23,3,4,34]
# print(input_dict)

# input_dict.pop("Name") 
# del input_dict["Owner"]
# print(input_dict)
#print(type(input_dict))

# input_dict = {}
# input_dict["Name"] = "Vs code"
# input_dict["Owner"] = ["Microsoft", "Bill Gates"]
# input_dict["age"] = [1,23,3,4,34]
# print(input_dict)

# input_dict.popitem()   #Delete Last key-value pair
# print(input_dict)
# input_dict.update({"Name": "windows"})
# print(input_dict)
# input_dict.clear() #Clear whole dictionary
# print(input_dict)

dict1 = {"Name": "Shivam", "Age":21, "Planet": "Earth", "Country": "India"}

#***** Loop ******

# for x in dict1:
#     # print(x)
#     # print(dict1[x])
#     print(dict1.items())

# for x,y in dict1.items():
#     print(x,y)


# ***** Copy Dictionary *******

copy_dict1 = dict1.copy()
copy_dict1["Planet"] = "Mars"
print(dict1)
print(copy_dict1)

# Note : If we copy directly (copy_dict1 = dict1) then we if make any changes in the copy_dict1 will also reflect into the dict1 because with this method both share the same address. So for copying a dictionary dict.copy() method is used.

