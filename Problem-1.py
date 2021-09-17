class Calculator:
    def calculate(a, b, operator):
        return eval(str(a) + operator + str(b))
def main():
    a = float(input())
    b = float(input())
    op = input()
    result = Calculator.calculate(a, b, op)

    print(result)


if __name__ == "__main__":
    main()