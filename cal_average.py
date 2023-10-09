ages = [10, 20, 30, 40]
income = [60, 100, 120, 160]

def calculate_average(list):
    sum = 0
    for i in list:
        sum = sum + i

    return sum/len(list)
print(calculate_average(income))