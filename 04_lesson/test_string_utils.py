import pytest
from string_utils import StringUtils


class TestStringUtils:
    utils = StringUtils()


    # --- Тесты capitalize ---
    @pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),            # Позитивный
        ("hello world", "Hello world"),  # Позитивный (фраза)
        ("123", "123"),                  # Позитивный (цифры)
        ("", ""),                        # Негативный (пустая строка)
        (" ", " ")                       # Негативный (пробел)
    ])
    def test_capitalize_positive(self, input_str, expected):
        assert self.utils.capitalize(input_str) == expected


    # --- Тесты trim ---
    @pytest.mark.parametrize("input_str, expected", [
        ("   skypro", "skypro"),        # Позитивный (несколько пробелов)
        (" skypro", "skypro"),          # Позитивный (один пробел)
        ("skypro   ", "skypro   "),      # Позитивный (пробелы в конце не трогаем)
        ("   sky pro", "sky pro"),      # Позитивный (пробел внутри сохраняется)
        ("", ""),                       # Негативный (пустая строка)
    ])
    def test_trim_positive(self, input_str, expected):
        assert self.utils.trim(input_str) == expected


    # --- Тесты contains ---
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),          # Позитивный
        ("SkyPro", "P", True),          # Позитивный
        ("SkyPro", "U", False),         # Позитивный (отсутствие)
        ("", "a", False),               # Негативный (поиск в пустой строке)
    ])
    def test_contains(self, string, symbol, expected):
        assert self.utils.contains(string, symbol) == expected


    # --- Тесты delete_symbol ---
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),       # Позитивный (один символ)
        ("SkyPro", "Pro", "Sky"),       # Позитивный (подстрока)
        ("banana", "a", "bnn"),         # Позитивный (все вхождения)
        ("SkyPro", "z", "SkyPro"),      # Позитивный (символа нет)
        ("", "a", ""),                  # Негативный (пустая строка)
    ])
    def test_delete_symbol(self, string, symbol, expected):
        assert self.utils.delete_symbol(string, symbol) == expected






