from .settings import *

# Note: it is recommended to use the "DEBUG" environment variable to override this value in your main settings.py file.
# A future release may remove it from here.
DEBUG = False

# fix ssl mixed content issues
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Django security checklist settings.
# More details here: https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HTTP Strict Transport Security settings
# Without uncommenting the lines below, you will get security warnings when running ./manage.py check --deploy
# https://docs.djangoproject.com/en/3.2/ref/middleware/#http-strict-transport-security

# # Increase this number once you're confident everything works https://stackoverflow.com/a/49168623/8207
# SECURE_HSTS_SECONDS = 60
# # Uncomment these two lines if you are sure that you don't host any subdomains over HTTP.
# # You will get security warnings if you don't do this.
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

USE_HTTPS_IN_ABSOLUTE_URLS = True

ALLOWED_HOSTS = [
    "*",  # update with your production hosts
]


# Your email config goes here.
# see https://github.com/anymail/django-anymail for more details / examples
# To use mailgun, comment out the lines below and make sure your key and domain
# are available in the environment.
# EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

# ANYMAIL = {
#     "MAILGUN_API_KEY": env("MAILGUN_API_KEY", default=None),
#     "MAILGUN_SENDER_DOMAIN": env("MAILGUN_SENDER_DOMAIN", default=None),
# }

SERVER_EMAIL = "noreply@localhost:8000"
DEFAULT_FROM_EMAIL = "victor@orcacorp.com.au"
ADMINS = [
    ("Your Name", "victor@orcacorp.com.au"),
]
