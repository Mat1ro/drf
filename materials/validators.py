from urllib.parse import urlparse

from rest_framework.exceptions import ValidationError


def validate_youtube_url(value):
    parsed_url = urlparse(value)
    domain = parsed_url.netloc.lower()

    if not 'youtube.com' in domain:
        raise ValidationError("Допустимы только ссылки на youtube.com")
    return value
