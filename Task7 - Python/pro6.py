def find_sum(list, target):
    n = len(list)
    for firstindex in range(n - 1):
        for secondindex in range(firstindex + 1, n):
            for thirdindex in range(firstindex + 2, n):
                if list[firstindex] + list[secondindex] + list[thirdindex] == target:
                  print(f"we can get our target number by suming indices {firstindex} and {secondindex} and {thirdindex}")


find_sum([1,3,5,6,9], 9)