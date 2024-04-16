import pytest
import sys
from pathlib import Path

path = Path(__file__).parent.parent.resolve()
# print(path)
sys.path.append(str(path))

from main import solution, vote, turtle_hare
from yandex import create_folder, create_headers, delete_folder


@pytest.mark.parametrize(
    "a, b, c, expected",
    (
            (1, 8, 15, (-3.0, -5.0)),
            (-4, 28, -49, (3.5,)),
            (1, 1, 1, "корней нет"),
            (0, 0, 0, ValueError),  # Проверка отработки raise в случае нулевого коэффициента
            (1, 0, 0, (4.0,))  # Проверка отработки неверного expected
    )
)
def test_solution(a, b, c, expected):
    if isinstance(expected, type) and issubclass(expected, ValueError):
        with pytest.raises(expected):
            solution(a, b, c)
    else:
        assert solution(a, b, c) == expected


@pytest.mark.parametrize(
    "votes, expected",
    (
            ([1, 1, 1, 2, 3], 1),
            ([1, 2, 3, 2, 2], 2),
            (2, ValueError),  # Проверка отработки raise в случае неверного типа данных
            ([], ValueError),  # Проверка отработки raise в случае пустого списка
            ([2, 3, 3, 2, 2], 1)  # Проверка отработки неверного expected
    ))
def test_vote(votes, expected):
    if isinstance(expected, type) and issubclass(expected, ValueError):
        with pytest.raises(expected):
            vote(votes)
    else:
        assert vote(votes) == expected


@pytest.mark.parametrize(
    "hare_distances, turtle_distances, expected",
    (
            ([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3], "черепаха"),
            ([8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3], "заяц"),
            ([8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3], "одинаково")
    )
)
def test_turtle_hare(hare_distances, turtle_distances, expected):
    assert turtle_hare(hare_distances, turtle_distances) == expected


class TestYandexDisk:

    def setup_method(self):
        self.url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = create_headers()
        self.folder_name = "test_folder"

    def teardown_method(self):
        delete_folder(self.folder_name)

    def test_create_folder_code_201(self):
        response = create_folder(self.folder_name)
        assert response.status_code == 201
    