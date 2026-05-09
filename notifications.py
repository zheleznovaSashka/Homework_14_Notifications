import asyncio
from typing import List, Tuple


async def send_notification(user: str, delay: float) -> None:
    """
    Асинхронно отправляет уведомление пользователю с указанной задержкой.

    Аргументы:
        user: имя пользователя
        delay: задержка в секундах перед отправкой уведомления

    Возвращает:
        None
    """
    print(f"Начинаю отправку уведомления для {user}...")
    # Имитация времени отправки
    await asyncio.sleep(delay)
    print(f"Уведомление для {user} отправлено!")


async def run_notifications(users: List[Tuple[str, float]]) -> None:
    """
    Запускает конкурентную отправку уведомлений для всех пользователей.

    Аргументы:
        users: список кортежей (имя пользователя, задержка в секундах)

    Возвращает:
        None
    """
    # Если список пуст - выводим сообщение и выходим
    if not users:
        print("Список пользователей пуст. Нет уведомлений для отправки.")
        return

    # Создаём асинхронные задачи для каждого пользователя
    tasks = [asyncio.create_task(send_notification(user, delay)) for user, delay in users]

    # Запускаем все задачи конкурентно
    await asyncio.gather(*tasks)


def main() -> None:
    """Основная функция программы."""
    # Список пользователей и их задержек (в секундах)
    users = [
        ("Alice", 2),
        ("Bob", 3),
        ("Charlie", 1),
        ("Diana", 4)
    ]

    # Запуск асинхронной программы
    asyncio.run(run_notifications(users))


if __name__ == "__main__":
    main()