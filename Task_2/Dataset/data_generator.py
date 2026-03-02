import pandas as pd
import numpy as np
import random

operations = ["+", "-", "*", "/"]

data = []

for _ in range(1000):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(operations)

    if operation == "+":
        output = num1 + num2
    elif operation == "-":
        output = num1 - num2
    elif operation == "*":
        output = num1 * num2
    elif operation == "/":
        output = num1 / num2

    data.append([num1, num2, operation, output])

df = pd.DataFrame(data, columns=["num1", "num2", "operation", "output"])
df.to_csv("./Dataset/calculator_data.csv", index=False)

print("Dataset created successfully!")