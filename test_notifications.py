import asyncio
import unittest
from unittest.mock import patch
from io import StringIO
from notifications import send_notification, run_notifications


class TestNotifications(unittest.TestCase):
    """Тесты для системы уведомлений."""

    def test_empty_users_list(self):
        """Тест: пустой список пользователей не вызывает ошибок."""
        async def test_empty():
            await run_notifications([])

        try:
            asyncio.run(test_empty())
            result = True
        except Exception:
            result = False

        self.assertTrue(result)

    def test_single_user_notification(self):
        """Тест: отправка уведомления одному пользователю."""
        captured_output = StringIO()

        async def test_single():
            with patch('sys.stdout', new=captured_output):
                await send_notification("TestUser", 0.1)

        asyncio.run(test_single())
        output = captured_output.getvalue()

        self.assertIn("Начинаю отправку уведомления для TestUser...", output)
        self.assertIn("Уведомление для TestUser отправлено!", output)

    async def async_test_multiple_users(self):
        """Асинхронный тест для нескольких пользователей."""
        users = [
            ("User1", 0.1),
            ("User2", 0.2),
        ]

        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            await run_notifications(users)

        output = captured_output.getvalue()

        # Проверяем, что все уведомления начались
        self.assertIn("Начинаю отправку уведомления для User1...", output)
        self.assertIn("Начинаю отправку уведомления для User2...", output)

        # Проверяем, что все уведомления завершились
        self.assertIn("Уведомление для User1 отправлено!", output)
        self.assertIn("Уведомление для User2 отправлено!", output)

    def test_multiple_users(self):
        """Тест: отправка уведомлений нескольким пользователям."""
        asyncio.run(self.async_test_multiple_users())

    def test_gather_usage(self):
        """Тест: убеждаемся, что используется asyncio.gather."""
        source_code = open("notifications.py", "r", encoding="utf-8").read()
        self.assertIn("asyncio.gather", source_code)

    def test_create_task_usage(self):
        """Тест: убеждаемся, что используется asyncio.create_task."""
        source_code = open("notifications.py", "r", encoding="utf-8").read()
        self.assertIn("asyncio.create_task", source_code)


if __name__ == "__main__":
    unittest.main()