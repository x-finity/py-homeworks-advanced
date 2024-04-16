# Задание «Квадратное уравнение»

def solution(a, b, c):
    def discriminant(a, b, c):
        return b ** 2 - 4 * a * c

    if a == 0:
        raise ValueError("Коэффициент А не может быть равен нулю")
    d = discriminant(a, b, c)
    if d < 0:
        return "корней нет"
    elif d == 0:
        x = -b / (2 * a)
        return x,
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2


# Задание «Голосование»
def vote(votes: list) -> int:
    if not isinstance(votes, list):
        raise ValueError("На входе подаются только списки")
    if len(votes) == 0:
        raise ValueError("Список пуст")
    return max(set(votes), key=votes.count)


# Задание «Кто дальше?»
def turtle_hare(hare_distances: list, turtle_distances: list):
    hare_all = sum(hare_distances)  # подсчитайте общую дистанцию зайца
    turtle_all = sum(turtle_distances)  # подсчитайте общую дистанцию черепахи
    # определите, кто из двоих прошел бОльшую дистанцию
    if hare_all > turtle_all:
        result = "заяц"
    elif hare_all < turtle_all:
        result = "черепаха"
    else:
        result = "одинаково"
    return result


if __name__ == '__main__':
    # print(solution(1, 8, 15))
    # print(solution(-4, 28, -49))
    # print(solution(1, 1, 1))
    # print(solution(1, 0, 0))
    # print(vote([1, 1, 1, 2, 3]))
    # print(vote([1, 2, 3, 2, 2]))
    # print(vote(2))
    print(turtle_hare([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3]))
    print(turtle_hare([8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3]))
    print(turtle_hare([8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3]))