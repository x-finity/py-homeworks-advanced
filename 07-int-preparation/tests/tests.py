import pytest
from main import brace_match


@pytest.mark.parametrize(
    "string, expected",
    [
        ("(((([{}]))))", "Сбалансировано"),
        ("[([])((([[[]]])))]{()}", "Сбалансировано"),
        ("{{[()]}}", "Сбалансировано"),
        ("}{}", "Несбалансировано"),
        ("{{[(])]}}", "Несбалансировано"),
        ("[[{())}]]", "Несбалансировано")
    ]
)
def test_brace_match_correct(string, expected):
    assert brace_match(string) == expected
