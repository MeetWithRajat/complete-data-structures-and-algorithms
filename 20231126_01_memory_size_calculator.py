import sys
import gc

empty_dict = {}
size_of_empty_dict = sys.getsizeof(empty_dict)
print(f"Size of empty dictionary: {size_of_empty_dict} bytes")

empty_dict["Name"] = "Rajat"
empty_dict["Title"] = "Roy"

size_of_empty_dict = sys.getsizeof(empty_dict)
print(f"Size of dictionary after: {size_of_empty_dict} bytes")

print(empty_dict.items())
print(empty_dict.values())
print(empty_dict.keys())
print("\n\n")

dict1 = {"Name": "Rajat", "Tite": "Roy"}
dict2 = {"Name": "Rajat", "Tite": "Roy"}

size_of_dict1 = sys.getsizeof(dict1)
print(f"Size of dictionary 1: {size_of_dict1} bytes")
size_of_dict2 = sys.getsizeof(dict2)
print(f"Size of dictionary 2: {size_of_dict2} bytes")

del dict1
dict2.clear()

# gc.collect()
try:
    size_of_dict1 = sys.getsizeof(dict1)
except Exception:
    size_of_dict1 = None
print(f"Size of dictionary 1: {size_of_dict1} bytes")
size_of_dict2 = sys.getsizeof(dict2)
print(f"Size of dictionary 2: {size_of_dict2} bytes")
