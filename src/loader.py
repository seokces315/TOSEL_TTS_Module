import json


# Loads and returns the list of questions
def load_question_list(input_path):
    # Opens the file containing the question list
    with open(input_path, "r", encoding="utf-8") as f:
        # Parses the JSON content into a Python list
        question_list = json.load(f)

    return question_list
