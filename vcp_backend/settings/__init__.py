from .base import *
import os

# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
try:
    if os.environ['VCP_BACKEND_SERVER'] == 'PROD':
        from .prod import *
    elif os.environ['VCP_BACKEND_SERVER'] == 'DEV':
        from .dev import *
    else:
        print('Please add environ \'VCP_BACKEND_SERVER\' to start using the service.\n\
The value could be:\n\
    PROD\n\
    DEV')
        raise EnvironmentError
except KeyError:
    print('Please add environ \'VCP_BACKEND_SERVER\' to start using the service.\n\
        The value could be:\n\
            PROD\n\
            DEV')
    raise KeyError