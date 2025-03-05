import streamlit as st
import math

# Streamlit UI
st.title("Factorial Calculator")

# User input
n = st.number_input("Enter a number:", min_value=0, step=1, format="%d")

if st.button("Calculate Factorial"):
    result = math.factorial(n)
    st.success(f"The factorial of {n} is {result}")
