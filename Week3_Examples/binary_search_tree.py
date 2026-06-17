def linear_search(names, target, index=0, comparisons=0):

    if index >= len(names):
        return False, comparisons

    comparisons += 1

    if names[index] == target:
        return True, comparisons

    return linear_search(names, target, index + 1, comparisons)

def binary_search(names, target, low, high, comparisons=0):

    if low > high:
        return False, comparisons

    middle = (low + high) // 2

    comparisons += 1

    if names[middle] == target:
        return True, comparisons

    elif target < names[middle]:
        return binary_search(
            names,
            target,
            low,
            middle - 1,
            comparisons
        )

    else:
        return binary_search(
            names,
            target,
            middle + 1,
            high,
            comparisons
        )

if __name__ == "__main__":

    names = [
        "Alice",
        "Charlie",
        "Dave",
        "Frieda",
        "Kallie",
        "Moe",
        "Paul",
        "Sarah",
        "Xavier"
    ]

    #
    # Example 1: Name is present
    #

    target = "Moe"

    found, comparisons = linear_search(names, target)

    print("Linear Search")
    print("Found:", found)
    print("Comparisons:", comparisons)
    print()

    found, comparisons = binary_search(
        names,
        target,
        0,
        len(names) - 1
    )

    print("Binary Search")
    print("Found:", found)
    print("Comparisons:", comparisons)
    print()

    #
    # Example 2: Name is absent
    #

    target = "Raoul"

    found, comparisons = linear_search(names, target)

    print("Linear Search")
    print("Found:", found)
    print("Comparisons:", comparisons)
    print()

    found, comparisons = binary_search(
        names,
        target,
        0,
        len(names) - 1
    )

    print("Binary Search")
    print("Found:", found)
    print("Comparisons:", comparisons)