def get_summ():
    try:
        num_one = int(input())
        num_two = int(input())
        result = num_one + num_two
        print(result)
    except ValueError:
        print("Это не числа.")
print(get_summ())
