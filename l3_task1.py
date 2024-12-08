# TODO Напишите функцию для поиска индекса товара
def find_index(item_list, item):
    if item in item_list:
        return item_list.index(item)  # Возвращаем индекс первого вхождения
    else:
        return None  # Если элемент не найден, возвращаем None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
