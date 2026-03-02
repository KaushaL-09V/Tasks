class Calculator:    

    def calculate(self, operation, *numbers):
        
        if len(numbers) < 2:
            return "Error: At least two numbers are required."

        match operation.strip():   
            case "+":
                result = 0
                for num in numbers:
                    result += num
                return result

            case "-":
                result = numbers[0]
                for num in numbers[1:]:
                    result -= num
                return result

            case "*":
                result = 1
                for num in numbers:
                    result *= num
                return result

            case "/":
                result = numbers[0]
                for num in numbers[1:]:
                    if num == 0:
                        return "Error: Division by zero."
                    result /= num
                return result

            case _:
                return "Error: Invalid operation."