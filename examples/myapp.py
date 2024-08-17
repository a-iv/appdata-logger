import logging
import os
import sys

# Append path to import appdata_logger
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

import appdata_logger
import mylib


logger = logging.getLogger(__name__)


def main():
    appdata_logger.config_with_stdout_and_file_handlers(
        application='myapp',
        separate_stdout_and_stderr=True,
    )
    appdata_logger.log_command_line()
    logger.info('Started')
    logger.warning('NOTE: separating stdout and stderr may lead log messages to be displayed in the wrong order.')
    mylib.do_something()
    logger.info('Finished')


if __name__ == '__main__':
    main()
