listScore = [7, 5, 3, 3, 2, int(input('Введите Ваш рейтинг: '))]

listScore.sort(reverse=True)
print(*listScore, sep=', ', end='.')
