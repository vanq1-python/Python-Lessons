def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if sender.count('@') == 0 or recipient.count('@') == 0:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    ends = ['.com', '.ru', '.net']
    for i in ends:
        if sender.endswith(i):
            break
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    for j in ends:
        if recipient.endswith(j):
            break
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')