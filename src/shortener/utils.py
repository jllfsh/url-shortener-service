import random
import string


def short_url_generator(size=6, chars=string.ascii_letters + string.digits):
    """
    Simple short URL generator.
    :param size:
    :param chars:
    :return:
    """
    return ''.join(random.choice(chars) for _ in range(size))


def make_short_url(instance, size=6):
    """
    Makes short URL by short_url_generator function and checks if the URL is unique.
    :param instance:
    :param size:
    :return:
    """
    url = short_url_generator(size=size)
    return url if not instance.__class__.objects.filter(short_url=url).exists() else short_url_generator(size=size)
