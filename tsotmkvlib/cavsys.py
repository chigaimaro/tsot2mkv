import logging
import sys

log = logging.getLogger(__name__)


# Check Python Version
def check_py_version():
    log.info("Checking version of Python")
    log.debug(sys.version_info)
    if sys.version_info[0] < 3 and sys.version_info[1] < 7:
        exit_on_critical("Please update your version of Python to at least 3.7.1")
    else:
        log.info("Python version check passes..")
        return True


# Log error and exit
def exit_on_critical(message):
    log.critical(message)
    exit(1)
