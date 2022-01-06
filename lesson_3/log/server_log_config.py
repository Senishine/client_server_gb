import logging

logger = logging.getLogger('gb.server')

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

fh = logging.FileHandler("gb.server.log", encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.setLevel(logging.INFO)

if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Test logging message')