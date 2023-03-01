def capitalize_first(arr):
    result = []
    if len(arr) == 1:
        return arr[0].capitalize()
    else:
        result.append(capitalize_first(arr[1:]))
        return result


print(capitalize_first(['car', 'taco', 'banana']))
