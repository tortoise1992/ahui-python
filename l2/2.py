import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a,%Y-%m-%d %H:%M:%S',
                    filename='ahui.log',
                    filemode='w'
                    )

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')