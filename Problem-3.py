def main():
    a = int(input())

    for i in range(a - (a - 1) % 2):
        print(i * 2 + 1, end=",")


if __name__ == "__main__":
    main()