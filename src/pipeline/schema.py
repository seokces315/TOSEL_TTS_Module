# Extracts passage, question text, and choices from the given schema
def extract_from_schema(question_list):
    # Holds the extracted items
    item_list = list()

    for question in question_list:
        # Builds a simplified item containing passages, the main questions, and its choices
        item = dict()

        materials = question.get("materials")
        if materials:
            item["passages"] = [material["content"]["text"] for material in materials]

        item["question"] = question["ask"]["text"]
        item["choices"] = [choice["content"]["text"] for choice in question["choices"]]

        item_list.append(item)

    return item_list
