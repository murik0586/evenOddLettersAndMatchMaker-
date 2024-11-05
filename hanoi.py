from typing import List, Tuple

'''
Прочитать про Ханойскую Башню - понять логику - yes
Каждая функция должна быть отдельно красиво реализована.  - yes
Ввод через консоль - yes(стержни и диски например)  - yes
Вывести решение на экран.
Записать решение в файл «решение.txt» - пришлось попотеть, но это куда проще чем на java.

'''


def hanoi(count_disk, start_kernel, target, auxiliary_kernel, moves):
    # count_disk - количество дисков.
    # start_kernel- начинается перенос дисков c этого стержня
    # target - куда перенести(номер стержня куда нужно перевести диски)
    # auxiliary_kernel - временный стержень, вспомогательный.
    # moves - откуда куда перемещается
    if count_disk > 0:
        hanoi(count_disk - 1, start_kernel, auxiliary_kernel, target, moves)
        moves.append((start_kernel, target))
        hanoi(count_disk - 1, auxiliary_kernel, target, start_kernel, moves)


'''
Если дисков больше нуля , идут следующие шаги:
Сначала рекурсивно переносим n-1 дисков со стержня  start_kernel на стержень auxiliary_kernel используя target как вспомогательный.
Затем перемещает один диск с start_kernel на target и записываем этот шаг в список moves.
переносим n-1 дисков со стержня auxiliary_kernel на стержень target, используя start_kernel как вспомогательный.
За один шаг перемещается только один диск, и при этом каждый меньший диск всегда кладется поверх большего.
'''


def print_moves(moves: List[Tuple[int, int]]):
    for i, (src, tgt) in enumerate(moves, 1):
        print(f"Блин {i}: Стержень {src} -> Стержень {tgt}")


'''print_moves 
вывод на экран всех шагов, которые были записаны в список.
которые были записаны в список moves.
Принимает список moves,каждый элемент — это кортеж, содержащий номера стержней move.
Для каждого шага перемещения выводится строка
'''


def save_moves_to_file(moves: List[Tuple[int, int]], filename="решение.txt"):
    with open(filename, "w") as f:
        for i, (src, tgt) in enumerate(moves, 1):
            f.write(f"Блин {i}: Стержень {src} -> Стержень {tgt}\n")


'''сохраняем все шаги перемещения дисков в файл с именем "решение.txt" - 
хотя мне бы хотелось сделать реализацию, чтобы сохранение шло в разные файлы.
Принимает список moves и имя файла filename.
Для каждого шага перемещения записываем строку в файл
По идее должны получить то, что запись будет аналогичная как у нас в консоли.'''


def main():
    # Ввод начальных условий, для работы с исключениями я решил ограничиться блоком try catch - он аналогичен Котлину.
    try:
        num_rods = int(input("Введите количество стержней: "))
        num_disks = int(input("Введите количество дисков: "))

        if num_rods < 3:
            print("Ошибка: количество стержней должно быть не менее 3.")
            return

        moves = []
        hanoi(num_disks, 1, 3, 2, moves)

        # Вывод на экран
        print("Решение задачи:")
        print_moves(moves)

        # Запись решения в файл
        save_moves_to_file(moves)
        print(f"Решение записано в файл 'решение.txt'")

    except ValueError:
        print("Ошибка: введите числовые значения для количества стержней и дисков, нам не годятся строки!")


'''
Запрашиваем начальные условия — количество стержне и количество дисков.
Проверяем, что введено корректное количество стержней
Создаем пустой список , а в нем  будем хранить все шаги решения.
Вызываем функцию hanoi.
Затем вызывает функцию вывода на экран
В конце вызываем функцию сохранения, чтобы сохранить результат в файл.
Если введем не те данные, программа выводит сообщение исключение и не завершает работу, и можем пробовать снова'''
if __name__ == "__main__":
    main()
