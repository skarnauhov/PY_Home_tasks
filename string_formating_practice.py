team1_num = 5
team2_num = 6
score_1 = 20
score_2 = 25
team1_time = 2200
team2_time = 1800
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print('%s. использование %%' % 1)
print("В команде Мастера кода участников: %s!" % team1_num)
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))
print('%s' %'')
print('{}. использование format'.format(2))
print("Команда Волшебники данных решила задач: {}!".format(score_2))
print("Волшебники данных решили задачи за {} сек.!".format(team2_time))
print('{}'.format(''))
print(f'{1+2}. использование f-строк')
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} или {score_2 + score_1} '
      f'задач, в среднем по {time_avg} '
      f'или {(team1_time + team2_time) / (score_1 + score_1)} секунды на задачу!.')