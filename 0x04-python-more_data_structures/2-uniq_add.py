#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list."""
    unique_sum = sum(set(my_list))
    return unique_sum


# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
