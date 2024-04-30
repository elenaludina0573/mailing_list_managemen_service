from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client (models.Model):
    email = models.EmailField(max_length=100, verbose_name='электронная почта клиента')
    first_name = models.CharField(max_length=100, **NULLABLE, verbose_name='имя клиента')
    last_name = models.CharField(max_length=100,**NULLABLE,  verbose_name='фамилия клиента')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий клиента')
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message (models.Model):
    subject = models.CharField(max_length=150, verbose_name='тема сообщения')
    text = models.TextField(**NULLABLE, verbose_name='текст сообщения')
    picture = models.ImageField(upload_to='service/', **NULLABLE, verbose_name='картинка сообщения')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing (models.Model):
    time_sending = models.DateTimeField(verbose_name='дата и время отправки')
    time_end = models.DateTimeField(verbose_name='дата и время окончания')
    periodicity_chose = [
        ('once a week', 'один раз в неделю'),
        ('everyday', 'каждый день'),
        ('once a month', 'один раз в месяц'),
    ]
    periodicity = models.CharField(max_length=100, choices=periodicity_chose, verbose_name='периодичность')
    status_chose = [
        ('created', 'создана'),
        ('launched', 'запущена'),
        ('completed', 'завершена'),
    ]
    status = models.CharField(max_length=100, choices=status_chose, verbose_name='статус')
    clients = models.ManyToManyField(Client, verbose_name='клиенты')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, **NULLABLE, verbose_name='сообщение')

    def __str__(self):
        return f'{self.time_sending}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Attempt (models.Model):
    time_attempt = models.DateTimeField(auto_now_add=True, verbose_name='время попытки')
    status_chose = [
        ('successful', 'успешно'),
        ('unsuccessful', 'не успешно'),
    ]
    status = models.CharField(max_length=100, choices=status_chose, verbose_name='статус попытки')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')
    answer = models.TextField(**NULLABLE, verbose_name='ответ сервера')

    def __str__(self):
        return f'{self.time_attempt} {self.status}'

    class Meta:
        verbose_name = 'попытка'
        verbose_name_plural = 'попытки'
