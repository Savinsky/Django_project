#from celery.app import task
#from django.core.mail import send_mail
#from .models import Order


#@task
#def order_created(order_id):
#    """
#    Задача для отправки уведомления по электронной почте при успешном создании заказа.
#    """
#    order = Order.objects.get(id=order_id)
#    subject = 'Заказ номер {}'.format(order_id)
#    message = 'Уважаемый {},\n\nВы успешно оформили заказ.\
#                Ваш заказ под id {}.'.format(order.first_name,
#                                             order.id)
#    mail_sent = send_mail(subject,
#                          message,
#                         'admin@myshop.com',
#                         [order.email])
#   return mail_sent