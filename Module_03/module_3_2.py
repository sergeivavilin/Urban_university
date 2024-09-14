"""
Задача "Рассылка писем":
Часто при разработке и работе с рассылками писем(e-mail) они отправляются от
одного и того же пользователя(администрации или службы поддержки).
Тем не менее должна быть возможность сменить его в редких случаях.
Попробуем реализовать функцию с подробной логикой.

Создайте функцию send_email, которая принимает 2 обычных аргумента:
сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
Внутри функции реализовать следующую логику:
Проверка на корректность e-mail отправителя и получателя.
Проверка на отправку самому себе.
Проверка на отправителя по умолчанию.

Пункты задачи:
Создайте функцию send_email, которая принимает 2 обычных аргумента:
message(сообщение), recipient(получатель)
и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
Если же sender и recipient совпадают, то вывести: "Нельзя отправить письмо самому себе!"
Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение:
"Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!
Письмо отправлено с адреса <sender> на адрес <recipient>."

Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.

"""
def consist_commercial_at(recipient: str, sender: str) -> bool:
    return "@" in (sender and recipient)

def correct_domain(recipient: str, sender: str) -> bool:
    allowed_domain = (".com", ".ru", ".net")
    return recipient.endswith(allowed_domain) and sender.endswith(allowed_domain)

def correct_email(recipient: str, sender: str) -> bool:
    return  consist_commercial_at(recipient, sender) and correct_domain(recipient, sender)

def send_email(message: str, recipient: str, sender: str="university.help@gmail.com"):
    recipient = recipient.lower()
    sender = sender.lower()

    if not correct_email(recipient, sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")


if __name__ == '__main__':
    send_email(
        'Это сообщение для проверки связи',
        'vasyok1337@gmail.com'
    )
    send_email(
        'Вы видите это сообщение как лучший студент курса!',
        'urban.fan@mail.ru',
        sender='urban.info@gmail.com'
    )
    send_email(
        'Пожалуйста, исправьте задание',
        'urban.student@mail.ru',
        sender='urban.teacher@mail.uk'
    )
    send_email(
        'Напоминаю самому себе о вебинаре',
        'urban.teacher@mail.ru',
        sender='urban.teacher@mail.ru'
    )
