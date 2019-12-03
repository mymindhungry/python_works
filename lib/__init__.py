# __all__ = ['calculator']

from os.path import dirname, basename, isfile, join
import glob

all_modules = glob.glob(join(dirname(__file__), '*.py'))

__all__=[basename(file)[:-3] for file in all_modules if isfile(file) and not file.endswith('__init__.py')]

