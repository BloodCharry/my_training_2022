import unittest
from unittest.mock import Mock, MagicMock

from Bowling import BowlingResult


class TestBowlingResult(unittest.TestCase):
    def test_get_score(self):
        # Создайте объект класса BowlingResult
        game_result = "X" * 12
        result = BowlingResult(game_result)
        # Задайте ожидаемый результат
        expected_result = 240
        # Задайте значения self.result
        result.result = ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
        # Вызовите функцию и проверьте, что она возвращает ожидаемый результат
        self.assertEqual(result.get_score(), expected_result)
        # Проверьте, что методы были вызваны с правильными аргументами и в правильном порядке
        self.assertEqual(result.frame, 10)

    def test_check_result(self):
        game_result = 'X 7 / 9 0 X 0 8 8 / 0 6 X X X 8 1'
        result = BowlingResult(game_result)
        # Замените метод self.result на mock-объект
        result.result = Mock(return_value=game_result)
        # Проверьте, что функция вызывает исключение, если тип данных не является str
        result.game_result = 123
        self.assertRaises(TypeError, result.check_result)
        # Проверьте, что функция вызывает исключение, если количество бросков меньше 12 или больше 21
        game_result = "X X X X X X X X X X X X"
        result = BowlingResult(game_result)
        # Здесь мы создали объект-заглушку MagicMock для game_result,
        # а затем установили его как значение атрибута result для экземпляра класса BowlingResult
        result.result = MagicMock(return_value=game_result)
        # Тестовый пример, в котором количество бросков меньше 12 или больше 21
        result.result.__len__.return_value = 10
        with self.assertRaises(ValueError):
            result.check_result()
        result.result.__len__.return_value = 22
        with self.assertRaises(ValueError):
            result.check_result()
        # Тестовый пример, где количество бросков находится между 12 и 21
        result.result.__len__.return_value = 20
        self.assertIsNone(result.check_result())

