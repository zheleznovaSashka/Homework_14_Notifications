import asyncio
from notifications import send_notification, run_notifications


async def add_user_interactive():
    """Интерактивное добавление пользователя."""
    print("ДОБАВЛЕНИЕ НОВОГО ПОЛЬЗОВАТЕЛЯ")

    name = input("Введите имя пользователя: ").strip()
    if not name:
        print("Имя не может быть пустым!")
        return None

    while True:
        try:
            delay = float(input("Введите задержку в секундах (0.1-10): "))
            if 0.1 <= delay <= 10:
                return (name, delay)
            else:
                print("Задержка должна быть от 0.1 до 10 секунд!")
        except ValueError:
            print("Пожалуйста, введите число!")


async def interactive_mode():
    """Интерактивный режим работы."""
    users = []

    print("АСИНХРОННАЯ СИСТЕМА УВЕДОМЛЕНИЙ")

    print("\nДавайте добавим пользователей для отправки уведомлений.\n")

    while True:
        print("\n1. Добавить пользователя")
        print("2. Запустить отправку уведомлений")
        print("3. Показать список пользователей")
        print("0. Выход")

        choice = input("\nВыберите действие: ").strip()

        if choice == '1':
            user = await add_user_interactive()
            if user:
                users.append(user)
                print(f"Пользователь '{user[0]}' добавлен с задержкой {user[1]} сек.")

        elif choice == '2':
            if not users:
                print("Список пользователей пуст! Сначала добавьте пользователей.")
            else:
                print("\nЗАПУСК ОТПРАВКИ УВЕДОМЛЕНИЙ...\n")
                await run_notifications(users)
                print("\nВсе уведомления отправлены!")

        elif choice == '3':
            if not users:
                print("Список пользователей пуст.")
            else:
                print("\nСПИСОК ПОЛЬЗОВАТЕЛЕЙ:")
                for i, (name, delay) in enumerate(users, 1):
                    print(f"  {i}. {name} (задержка: {delay} сек.)")

        elif choice == '0':
            print("\nДо свидания!")
            break

        else:
            print("Неверный выбор!")


def main():
    """Основная функция."""
    print("\nВыберите режим работы:")
    print("1. Демонстрационный режим (стандартный список)")
    print("2. Интерактивный режим (свой список)")
    print("0. Выход")

    choice = input("\nВаш выбор: ").strip()

    if choice == '1':
        # Стандартный список пользователей
        users = [
            ("Alice", 2),
            ("Bob", 3),
            ("Charlie", 1),
            ("Diana", 4)
        ]
        print("\nЗАПУСК ОТПРАВКИ УВЕДОМЛЕНИЙ\n")
        asyncio.run(run_notifications(users))

    elif choice == '2':
        asyncio.run(interactive_mode())

    elif choice == '0':
        print("\nДо свидания!")

    else:
        print("Неверный выбор!")


if __name__ == "__main__":
    main()