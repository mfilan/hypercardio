from copy import deepcopy


def drag_delete(combination_index, element_index):
    input_list = [
        ["a", "b", "c"],
        ["z", "b", "c"],
        ["j", "k", "w"],
        ["z", "d", "c"],
        ["f", "g", "d"],
        ["e", "d", "c"],
        ["r", "y", "u"],
        ["a", "t", "c"],
        ["a", "b", "y"],
        ["p", "b", "y"],
    ]

    referential_list = deepcopy(input_list)[combination_index]
    referential_list.pop(element_index)

    del input_list[combination_index]

    copy_list = deepcopy(input_list)

    for _list in copy_list:
        _list.pop(element_index)

    solution = []

    for input_element, _shorter_list in zip(input_list, copy_list):
        if _shorter_list == referential_list:
            solution.append(input_element)

    return solution


if __name__ == '__main__':
    print(drag_delete(0, 1)) #wstępna wersja algorytmu
