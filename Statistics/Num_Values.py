from Calculator.Addition import addition


def num_values(num_value_list):
    num_value = len(num_value_list)
    total = 0
    for num in num_value:
        total = addition(total, num)

    return num_value
