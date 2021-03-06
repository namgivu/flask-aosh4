#auto import all module, ie. *.py files, in the package folder ref. http://stackoverflow.com/a/1057534/248616
from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [
  basename(f)[:-3] for f in modules if isfile(f)
]
