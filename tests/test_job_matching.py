import os
import sys
import pandas as pd


# Add the project root folder to Python's path
project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, project_root)


from job_matcher import calculate_match_scores


# Load test cases
test_file = os.path.join(
    project_root,
    "tests",
    "test_cases.csv"
)

test_cases = pd.read_csv(test_file)


passed_tests = 0
total_tests = len(test_cases)


for _, row in test_cases.iterrows():

    resume_text = row["Resume Skills"]
    expected_role = row["Expected Top Role"]

    results = calculate_match_scores(resume_text)

    actual_role = results[0]["Job Role"]

    print("-----------------------------------")
    print(f"Resume Skills: {resume_text}")
    print(f"Expected Role: {expected_role}")
    print(f"Actual Role:   {actual_role}")

    if actual_role == expected_role:

        print("Result: PASS")
        passed_tests += 1

    else:

        print("Result: FAIL")


print("\n===================================")
print("TEST SUMMARY")
print("===================================")

print(f"Passed: {passed_tests}/{total_tests}")

accuracy = (
    passed_tests / total_tests
) * 100

print(f"Accuracy: {accuracy:.0f}%")