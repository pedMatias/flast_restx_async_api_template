
import logging
import os

_ENV_VAR = "ENVIRONMENT"
_PRODUCTION = "PRODUCTION"
_LOCAL = "LOCAL"

if os.environ.get(_ENV_VAR) == _PRODUCTION:
    from .production import *
else:
    if os.environ.get(_ENV_VAR) != _LOCAL:
        logging.warning("No valid value set for environment variable '{}'. "
                        "Assuming value '{}'".format(_ENV_VAR, _LOCAL))
    from .local import *
