def adress_check(adress):
    a = '@'
    mandatory_list = ['.com', '.ru', '.net']
    adr_ok = False
    for i in mandatory_list:
        if a in adress and adress.endswith(i):
            adr_ok = True
            break
    return adr_ok


def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if adress_check(recipient) and adress_check(sender):
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса university.help@gmail.com на адрес {recipient}.')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
