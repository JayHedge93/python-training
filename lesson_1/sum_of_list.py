def sum_lst(lst: [int]):
    total = 0       # Cost C
    for x in lst:
        total += x  # Cost 2C
    return total    # total cost = (N + 1) * C = N*C?

def sum_lst_recursion(lst, total):
    # Recursion base case
    if len(lst) == 0:
        return total

    print(lst, total)
    current = lst.pop()
    return sum_lst_recursion(lst, total + current)

if __name__ == "__main__":
    lst_A = [i for i in range(10)]
    # print(sum_lst(lst_A))
    print(sum_lst_recursion(total = 0, lst = lst_A))
    # print(sum_lst_recursion(lst_A, 0))