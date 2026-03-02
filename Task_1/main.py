from Calc import Calculator

def main():
    calc = Calculator()

    print("Simple Calculator")
    print("Operations: + ,- ,* / ")

    operation = input("Enter operation: ")

    numbers_input = input("Enter numbers separated by space: ")
    numbers = []

    for num in numbers_input.split():
        numbers.append(float(num))

    result = calc.calculate(operation, *numbers)

    print("Result:", result)

if __name__ == "__main__":
    main()