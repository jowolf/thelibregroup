
import os, sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]
settings_module = "%s.settings" % PROJECT_DIRNAME
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

#from settings import PROJECT_ROOT, PROJECT_DIRNAME
#print PROJECT_ROOT, PROJECT_DIRNAME

os.chdir(PROJECT_ROOT)
#sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_ROOT, "..")))
sys.path.insert(0, PROJECT_ROOT)

#settings_module = "%s.settings" % PROJECT_DIRNAME  # PROJECT_ROOT.split(os.sep)[-1]
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
