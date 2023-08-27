from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import PostCategoryRelation
from django.conf import settings
import logging


def send_notification(previewPost, pk, title, subscribers):
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': previewPost,
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )

    logger = logging.getLogger(__name__)
    logger.info(f"Sending notification for post {pk}")

    msg = EmailMultiAlternatives(
        subject=title,
        body=previewPost,
        from_email=settings.DEFAULT_FROM_EMAIL
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategoryRelation)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categoryes.all()
        print(f'{categories = }')

        subscribers: list[str] = []
        print(f'{subscribers = }')

        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]
        print(f'{subscribers = }')

        send_notification(instance.previewPost, instance.pk, instance.title, subscribers)
