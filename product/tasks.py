from django.core.mail import send_mail
import movi
from movi.film._celery import app


@movi.film._celery.app.task()
def notify_user_task(email):
    send_mail(
        'вы создали новый запрос',
        'Спасибо за испоьзование нашего сайта',
        'test@gmail.com',
        [email, ]
    )
    return 'Success'
