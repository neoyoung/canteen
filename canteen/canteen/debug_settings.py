#!/usr/bin/env python
# encoding: utf-8

DEBUG = True
TEMPLATE_DEBUG = DEBUG

#local config
import os
PROJECT_DIR = os.path.dirname(
    os.path.abspath(
        os.path.dirname(__file__).decode('utf-8')))


ADMINS = (
    ('zhkzyth', 'zhkzyth@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        # Or path to database file if using sqlite3.
        'NAME': 'canteen',
        'USER': 'canteen',  # Not used with sqlite3.
        'PASSWORD': 'canteen',  # Not used with sqlite3.
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'
#LANGUAGE_CODE = 'zh-cn'

LANGUAGES = (
    ('zh-cn', u'简体中文'),  # instead of 'zh-CN'
    ('zh-tw', u'繁體中文'),  # instead of 'zh-TW'
)

LOCALE_PATHS = (
    '/Users/admin/code/canteen/canteen/locale/',
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

#Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR,'static_dev'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'jf2qbdt=@lsln%omah7e@_nc+#-lr(yr8)r-)!@#s(s9mh@d_q'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #server proxy x-forward
    'canteen.common.http.SetRemoteAddrFromForwardedFor',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #IP check and login
    'canteen.accounts.middleware.IpLoginMiddleware',
    #add the debug tool
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'canteen.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'canteen.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates"
    #or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    #food taging
    #'tagging',
    #use to trace the sql
    'debug_toolbar',
    #foods
    'canteen.foods',
    #accounts management
    'canteen.accounts',
    #
    'canteen.order',
    #menu support
    'canteen.menu',
    #
    'canteen.exercise',
    #gunicorn for production dev
    'gunicorn',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


#config for the debug-tool
INTERNAL_APPS = ('127.0.0.1',)


def custom_show_toolbar(request):
    return True  # Always show toolbar, for example purposes only.

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    #'EXTRA_SIGNALS': [''],
    'HIDE_DJANGO_SQL': False,
    'TAG': 'div',
    'ENABLE_STACKTRACES': True,
}

#debug panel for configuration
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)


#TODO try the ssh connection
ENABLE_SSH = False


#Context processor
#add the meta info for fallback support


# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    #    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    #
    'canteen.common.context_processors.canteen'
)

#IF ENABLE SSL CONNECTION
ENABLE_SSL = False

#SITE NAME
SITE_NAME = "175game Canteen"
#META KEYWORD
META_KEYWORDS = "canteen"
#META_DESCRIPTION
META_DESCRIPTION = "a canteen demo for 175game.And just enjoy.=)"


#
LOGIN_REDIRECT_URL = '/accounts/my_account/'


# Host for sending email.
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = 'zhkzyth@gmail.com'
EMAIL_HOST_PASSWORD = ''

# Port for sending email.
EMAIL_PORT = 587

# Implement our auth
AUTHENTICATION_BACKENDS = (
    #for customer
    'canteen.accounts.views.IpLoginBackend',
    #for super user
    'django.contrib.auth.backends.ModelBackend',
)

# admin static files put here
#ADMIN_MEDIA_PREFIX = '/static_admin/'
