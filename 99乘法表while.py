#while循环其实和for循环差不多
def main():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print(f"{j}*{i}={i*j}", end="\t")
            j += 1
        print()
        i += 1
if __name__ == "__main__":
    main()