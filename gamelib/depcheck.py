''' Dependency checks '''

def check_version():
    import sys 
    required_version = (3,5)
    if sys.version_info[0:2] < required_version:
        print('This game required Python 3.5 or higher to work.')
        return False
    return True



def check_dependencies():
    from importlib.util import find_spec
    from itertools import filterfalse
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