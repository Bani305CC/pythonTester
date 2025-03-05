import streamlit as st
import ast


# Function to test user code
def run_tests(user_code, test_cases):
    function_name = "student_function"

    try:
        # Prepare an execution environment
        exec_globals = {}
        exec(user_code, exec_globals)

        # Check if function exists
        if function_name not in exec_globals:
            return ["❌ Error: Function not defined correctly!"]

        # Run test cases
        results = []
        for test in test_cases:
            try:
                # Convert input string to tuple (supporting multiple arguments)
                inputs = ast.literal_eval(test["input"])
                expected_output = ast.literal_eval(test["expected_output"])

                # Ensure input is a tuple (for multiple arguments)
                if not isinstance(inputs, tuple):
                    inputs = (inputs,)

                # Execute function
                result = exec_globals[function_name](*inputs)

                # Compare result with expected output
                if result == expected_output:
                    results.append(f"✅ Passed: {function_name}{inputs} = {result}")
                else:
                    results.append(f"❌ Failed: {function_name}{inputs} returned {result}, expected {expected_output}")
            except Exception as e:
                results.append(f"⚠️ Error while running test case {test['input']}: {str(e)}")

        return results

    except Exception as e:
        return [f"❌ Error: {str(e)}"]

# Streamlit GUI
st.title("Python Function Tester")

st.write("### Write your function below:")
user_code = st.text_area(
    "Function Code",
    value="def student_function(x):\n\n return result",
    height=200
)

# Default test cases
if "test_cases" not in st.session_state:
    st.session_state.test_cases = [{"input": "4", "expected_output": "16"},
                                   {"input": "1", "expected_output": "1"},
                                   {"input": "-3", "expected_output": "9"}]


# Run tests button
if st.button("Run Tests"):
    results = run_tests(user_code, st.session_state.test_cases)
    st.write("### Results:")
    for res in results:
        st.code(res)
