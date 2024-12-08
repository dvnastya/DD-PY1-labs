# TODO Напишите функцию find_common_participants
def find_common_participants(group1: str, group2: str, delimiter: str = ','):
    participants1 = {participant.strip() for participant in group1.split(delimiter)}
    participants2 = {participant.strip() for participant in group2.split(delimiter)}
    result_participants = participants1.intersection(participants2)  # общие участнки
    return sorted(list(result_participants))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants_list = find_common_participants(participants_first_group, participants_second_group, delimiter='|')

print("Общие участники:", common_participants_list)

