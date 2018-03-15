def deep_flatten(arg):
    result = []
    for i in arg:
        if isinstance(i, list):
            result.extend(deep_flatten(i))
        else:
            result.append(i)
    return result

assert deep_flatten([1, [2], [[3], 4], 5]) == [1,2,3,4,5]