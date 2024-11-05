from datetime import datetime


def parse_date(date_str):
    formats = [
        ("%A, %B %d, %Y", "The Moscow Times"),
        ("%A, %d.%m.%y", "The Guardian"),
        ("%A, %d %B %Y", "Daily News")
    ]

    for fmt, newspaper in formats:
        try:
            date_obj = datetime.strptime(date_str, fmt)
            print(f"{newspaper}: {date_obj}")
            return date_obj
        except ValueError:
            continue
    print("Неверный формат даты. Попробуйте еще раз.")
    return None


def main():
    print("Введите дату (или 'exit' для выхода):")
    while True:
        user_input = input("Дата: ")
        if user_input.lower() == "exit":
            print("Программа завершена.")
            break
        parse_date(user_input)


if __name__ == "__main__":
    main()