def capitalize_first(arr):
    result = []
    if len(arr) == 0:
        return result
    else:
        result.append(arr[0].capitalize())
        result += capitalize_first(arr[1:])
        return result


print(capitalize_first(['car', 'taco', 'banana']))
