class MyClass:
    def fun(self, arr):
        min_idx = 0
        length = len(arr)
        for i in range(1, length):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[min_idx], arr[-1] = arr[-1], arr[min_idx]


if __name__ == "__main__":
    arr = list(map(int, input().split(',')))

    print("交换前数组：", end="")
    print(",".join(map(str, arr)))

    obj = MyClass()
    obj.fun(arr)

    print("交换后数组：", end="")
    print(",".join(map(str, arr)))