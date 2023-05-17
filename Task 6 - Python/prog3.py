def solve(x, target):
    n = len(x)
    for first_index in range(n - 1):
        for second_index in range(first_index + 1, n):
            if x[first_index] + x[second_index] == target:
                print(f"you can get your number by adding these indexes {first_index} and {second_index}")

solve([1,2,3,4,5, 6], 9)