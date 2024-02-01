def remove_duplicates(arr: list) -> dict:
    names_prices_map = {}
    for item in arr:
        names_prices_map[item['name']] = item['price']
    return names_prices_map


def capitalize_all_words(text: str) -> str:
    return ' '.join(word.capitalize() for word in text.split())


def create_strings_for_printing(name_price_map: dict, count: int) -> list:
    strings = []
    i = 0
    for item in name_price_map:
        if i >= count:
            break

        name = capitalize_all_words(item)
        price = str(name_price_map[item])
        result = f"{name} | {price}$"
        strings.append(result)

        i += 1

    return strings


def process_array(original_arr: list, count: int):
    name_price_map = remove_duplicates(original_arr)
    strings_for_printing = create_strings_for_printing(name_price_map, count)
    for text in strings_for_printing:
        print(text)


ary = [
    {'name': 'coffee', 'price': 1.7},
    {'name': 'pizza', 'price': 10.5},
    {'name': 'burger', 'price': 13.7},
    {'name': 'cola', 'price': 10.9},
    {'name': 'package', 'price': 0.3},
    {'name': 'Apple pie', 'price': 22.9},
    {'name': 'Choco pie', 'price': 28.4},
    {'name': 'cola', 'price': 10.9},
    {'name': 'package', 'price': 0.3}
]

process_array(ary, 3)

assert len(ary) == 9
assert len(remove_duplicates(ary)) == 7

assert capitalize_all_words('Apple pie') == 'Apple Pie'
assert capitalize_all_words('choco pie') == 'Choco Pie'

assert len(create_strings_for_printing({'coffee': 1.7, 'Apple pie': 22.9}, 2)) == 2
assert (create_strings_for_printing({'Apple pie': 22.9, 'Choco pie': 28.4}, 2) ==
        ['Apple Pie | 22.9$', 'Choco Pie | 28.4$'])
