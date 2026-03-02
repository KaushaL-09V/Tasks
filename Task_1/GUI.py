import streamlit as st
from Calc import Calculator

calc = Calculator()

st.title(" Simple Calculator")

st.write("Perform calculations on multiple numbers")

operation = st.selectbox(
    "Select Operation",
    ["+", "-", "*", "/"]
)


numbers_input = st.text_input(
    "Enter numbers separated by space",
    placeholder="Example: 10 20 30"
)

if st.button("Calculate"):

    if numbers_input.strip() == "":
        st.error("Please enter numbers.")
    else:
        try:
            numbers = list(map(float, numbers_input.split()))
            result = calc.calculate(operation, *numbers)

            if isinstance(result, str):
                st.error(result)
            else:
                st.success(f"Result: {result}")

        except ValueError:
            st.error("Please enter valid numbers.")