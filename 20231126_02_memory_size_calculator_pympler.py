from pympler import asizeof

dict1 = {"Name": "Rajat", "Tite": "Roy"}
dict2 = {"Name": "Rajat", "Tite": "Roy"}

size_of_dict1 = asizeof.asizeof(dict1)
print(f"Size of dictionary 1: {size_of_dict1} bytes")
size_of_dict2 = asizeof.asizeof(dict2)
print(f"Size of dictionary 2: {size_of_dict2} bytes")

del dict1
dict2.clear()

# gc.collect()
try:
    size_of_dict1 = asizeof.asizeof(dict1)
except Exception:
    size_of_dict1 = None
print(f"Size of dictionary 1: {size_of_dict1} bytes")
size_of_dict2 = asizeof.asizeof(dict2)
print(f"Size of dictionary 2: {size_of_dict2} bytes")
