import json
def main():
    numbers = json.loads(input())
    countDict = dict()
    for x in numbers:
        for y in range(1, 10):
            if int(x) % int(y) == 0:
                countDict[int(y)] = countDict.get(int(y), 0) + 1
    print(countDict)


if __name__ == "__main__":
    main()
