''' Dependency checks '''

from importlib.util import find_spec
from itertools import filterfalse

def check_dependencies():
    '''
    Checks whether all needed 3rd party libraries are installed
    and loadable.

    Returns True if everything is in order.

    Otherwise Fals is returned and the missing modules are
    listed on stdout
    '''
    required_modules = ['pygame']
    missing_modules = filterfalse(find_spec, required_modules)

    if any(missing_modules):
        print('The following modules are missing: ' + ' '.join(missing_modules))
        return False
    return True