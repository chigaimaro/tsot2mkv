import logging
from datetime import datetime
from pathlib import Path

log = logging.getLogger(__name__)


def build_cavlog(log_level="DEBUG", input_path=None):
    """
    Sets up logging for the session
    :param log_level:
    :param input_path:
    :return:
    """
    # Setup Logging format and handlers
    session_log_format = logging.Formatter(
        '%(asctime)s : [%(module)s]: %(levelname)s : %(message)s')
    session_file_handler = logging.FileHandler(
        filename=str(setup_cavlog_folder(input_path)), mode='w')
    session_file_handler.setLevel(log_level)
    session_file_handler.setFormatter(session_log_format)

    # Initialize Logging
    session_log = logging.getLogger()
    session_log.setLevel(log_level)
    session_log.addHandler(session_file_handler)
    return session_log


def setup_cavlog_folder(input_path=None):
    """
    Creates log folder at a given path, if no path is supplied,
    current working directory is used and returned.
    :param input_path:
    :return: Absolute path as a string
    """

    # Creates new log file name
    log_filename = datetime.now().strftime("%Y%m%d-%H%M%S") + '.log'

    # Checks for log folder, if missing, creates log folder (exits on error)
    try:
        if not input_path:
            log_path = Path.cwd().joinpath('logs')
        else:
            log_path = Path(input_path).joinpath('logs')
        log_path.mkdir(parents=True, exist_ok=True)
        return str(log_path.joinpath(log_filename).absolute())
    except (IOError, FileNotFoundError, ValueError) as err:
        message = f"{err.errno}: {err.strerror}"
        with open(log_filename) as file:
            file.write(message)
        exit(1)
