'''Ваша задача заключается в том, чтобы создать функцию, которая отправлят приветственный email пользователю.
Функция получает два параметра: email и имя пользователя.
Темой письма должно быть "Welcome", а текст письма просто "Hi {name}" ({name} должно быть заменено на имя пользователя).'''

import sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = 'Your API KEY'
SUBJECT = 'Welcome'
BODY = 'Hi {}'
sg = sendgrid.SendGridAPIClient(API_KEY)


def send_email(email, name):
    message = Mail(
        from_email='from_email@example.com',
        to_emails=email,
        subject='Welcome',
        plain_text_content=BODY.format(name))

    try:
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('a.lyabah@checkio.org', 'oduvan')
    send_email('somebody@gmail.com', 'Some Body')
    send_email("admin@checkio.org", "Alex")
    print('Done')
