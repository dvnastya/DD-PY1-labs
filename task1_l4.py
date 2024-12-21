import json
# TODO решите задачу


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    total_sum = 0.0

    for entry in data:
        if 'score' in entry and 'weight' in entry:
            total_sum += entry['score'] * entry['weight']

    return round(total_sum, 3)


print(task())

