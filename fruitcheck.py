def is_fruit(fruit_check):
    fruit_list = ["banana", "apple", "pear", "peach"]
    fruit_check = fruit_check.strip(". ")
    is_a_fruit = fruit_check in fruit_list
    return is_a_fruit


def add(a, b):
    return a + b


if __name__ == "__main__":
    print(is_fruit("lettuce"))
    print(is_fruit("apple"))
