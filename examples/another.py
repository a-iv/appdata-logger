import logging
import os
import sys

# Append path to import appdata_logger
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

import appdata_logger


logger = logging.getLogger(__name__)


def main():
    appdata_logger.config_with_stdout_and_file_handlers(application='myapp', caller_file_path=__file__)
    appdata_logger.log_command_line()
    logger.info('Started')


if __name__ == '__main__':
    main()
