from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import Category
from django.conf import settings
from newspaper.newspaper.settings import DEFAULT_FROM_EMAIL


def send_notification(previewPost, pk, title, subscribers):
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': previewPost,
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body=previewPost,
        from_email=DEFAULT_FROM_EMAIL
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=Category)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categoryes.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notification(instance.previewPost, instance.pk, instance.title, subscribers)
