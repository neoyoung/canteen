import os, sys

vepath = '/home/zhkzyth/codeRep/canteen/lib/python2.7/site-packages'
#prev_sys_path = list(sys.path)
sys.path.append(vepath)
#path to directory of the .wsgi file('apache/')
wsgi_dir = os.path.abspath(os.path.dirname(__file__))
#path to project root directory (parent of 'apache/')
project_dir = os.path.dirname(wsgi_dir)
#add project directory to system's PATH
sys.path.append(project_dir)
#add the settings.py file to your system's PATH
#project_settings = os.path.join(project_dir, 'settings')

# explicitly define the DJANGO_SETTINGS_MODULE
os.environ['DJANGO_SETTINGS_MODULE'] = "canteen.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
