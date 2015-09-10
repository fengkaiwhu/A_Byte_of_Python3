#!/usr/bin/env python
# coding=utf-8
# Filename: using_logging.py

import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    logging_file = os.path.join(os.getenv('PWD'), 'test.log')

logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s:%(levelname)s:%(message)s',
                    filename = logging_file,
                    filemode = 'w')

logging.debug('Start the program')
logging.info('Doing something')
logging.warning('Dying now')
