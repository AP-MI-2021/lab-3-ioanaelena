import math


# cea mai lunga subsecventa : 3. nr de semne alternative
def get_longest_alternating_signs(lst):
    result = []
    aux = []
    for index in range(0, len(lst) - 1):
        first_number = lst[index]
        second_number = lst[index + 1]
        if first_number * second_number < 0:  # alternative sign
            if not aux:
                aux.append(first_number)
            if aux[-1] != first_number:
                aux.append(first_number)
            aux.append(second_number)
            if index + 1 == len(lst) - 1:
                result.append(aux)
        elif aux:
            result.append(aux)
            aux = []

    length_lists = []
    for possible_list in result:
        length_lists.append(len(possible_list))
    if length_lists:
        max_length = length_lists[0]
    interest_index = 0
    for index in range (0, len(length_lists)):
        if length_lists[index] > max_length:
            interest_index = index
    if result:
        return result[interest_index]
    else:
        return "Nu avem semne alternative."


def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([1, 2, 3, -4, -5, 6, 7, -8, 12, 13, 9, 10, 54]) == [7, -8, 12]


# cea mai lunga subsecventa : 17. media nr nu depaseste o valoare citita
def get_longest_average_below(lst, average: float):
    result = []
    aux = []
    sum = 0
    count = 0
    for index in range(0, len(lst)):
        number = lst[index]
        sum += number
        count += 1
        if sum / count <= average:
            aux.append(number)
        else:
            if aux and len(aux) > 1:
                result.append(aux)
            aux = [number]
            sum = number
            count = 1
    if aux not in result and len(aux) >= 2:
        result.append(aux)
    length_lists = []
    for possible_list in result:
        length_lists.append(len(possible_list))
    if length_lists:
        max_length = length_lists[0]
    interest_index = 0
    for index in range(0, len(length_lists)):
        if length_lists[index] > max_length:
            interest_index = index
    if result:
        return result[interest_index]
    else:
        return "Nu avem secvente de numere a caror medie sa fie mai mica de numarul dat."


def test_get_longest_average_below():
    assert get_longest_average_below([2, 5, 8, 1, 3, 4, 6, 7, 9], 4) == [1, 3, 4, 6]


# 1.patrate perfecte:
def get_longest_all_perfect_squares(lst):
    result = []
    aux = []
    for index in range(0, len(lst)):
        element = lst[index]
        if element >= 0:
            if math.sqrt(element) == int(math.sqrt(element)):
                aux.append(element)
                if index == len(lst) - 1:
                    result.append(aux)
            else:
                if aux:
                    result.append(aux)
                aux = []
        elif aux:
            result.append(aux)
            aux = []

    length_lists = []
    for possible_list in result:
        length_lists.append(len(possible_list))
    if length_lists:
        max_length = length_lists[0]
    interest_index = 0
    for index in range(0, len(length_lists)):
        if length_lists[index] > max_length:
            interest_index = index
    if result:
        return result[interest_index]
    else:
        return "Nu avem patrate perfecte in lista data."


def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([0, 1, 4, 16, 5, 7, 49]) == [0, 1, 4, 16]


def interface_for_reading_list_calling_properties_and_printing():
    lista = []
    while True:
        answer = input(
            "\nAlegeti una din optiunile:\n1. Citire\n2. Determinare cea mai lungă subsecvență cu semne alternative.\n"
            "3. Determinare cea mai lungă subsecvență cu a caror medie sa fie mai mica decat un parametru dat.\n"
            "4. Determinare cea mai lungă subsecvență de patrate perfecte.\n"
            "5. Ieșire.\n")
        if answer == "1":
            lista = []
            lungime_sir = input("Dati lungimea listei: ")
            for index in range(0, int(lungime_sir)):
                element = input('Introduceti numarul pentru a-l adauga in lista: ')
                lista.append(int(element))
            print("Lista citita este ", lista)
        if answer == "2":
            if lista!= []:
                print("Cea mai lunga subsecventa este: ", get_longest_alternating_signs(lista))
            else:
                print("Nu s-a citit lista. Intai apasati 1 in meniu.")
        if answer == "3":
            if lista != []:
                average = float(input("Dati media pentru proprietatea 2: "))
                print("Cea mai lunga subsecventa este: ", get_longest_average_below(lista, average))
            else:
                print('Nu s-a citit lista. Intai apasati 1 in meniu.')
        if answer == "4":
            if lista != []:
                print("Cea mai lunga subsecventa este: ", get_longest_all_perfect_squares(lista))
            else:
                print('Nu s-a citit lista. Intai apasati 1 in meniu.')
        if answer == '5':
            break


if __name__ == '__main__':
    interface_for_reading_list_calling_properties_and_printing()