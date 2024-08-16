from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags


def send_template_email(subject: str, template: str, to: list, from_email: str | None = None,
                        context: dict | None = None):
    html_message = render_to_string(template, context=context)
    plain_message = strip_tags(html_message)

    if from_email is None:
        from_email = settings.EMAIL_HOST_USER

    message = EmailMultiAlternatives(
        subject=subject,
        body=plain_message,
        from_email=from_email,
        to=to,
    )

    message.attach_alternative(html_message, "text/html")
    message.send()


def simple_send_mail(subject: str, message: str, to: list, from_email: str | None = None):
    if from_email is None:
        from_email = settings.EMAIL_HOST_USER

    send_mail(subject, message, from_email, [to])
