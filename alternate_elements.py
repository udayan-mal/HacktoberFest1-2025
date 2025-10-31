def get_alternates(arr):
    res = []
    for i in range(0, len(arr), 2):
        res.append(arr[i])
    return res

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    res = get_alternates(arr)
    for x in res:
        print(x, end=" ")
