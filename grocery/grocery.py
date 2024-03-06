def main():
    items = get_items("")
    for item in items:
        print(items.count(item), item)
        if items.count(item) > 1:
            items.remove(item)
def get_items(prompt):
    item_list = []
    try:
        while True:
            item = input(prompt).upper()
            item_list.append(item)
            item_list.sort()
    except EOFError:
        return item_list

main()
