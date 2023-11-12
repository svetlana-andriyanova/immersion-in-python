import logging
import os

FORMAT = '{levelname}, {asctime}, {msg}'
current_dir = os.path.dirname(os.path.realpath(__file__))
log_filename = os.path.join(current_dir, 'logs.log')
logging.basicConfig(format=FORMAT, style='{', filename=log_filename, filemode='w', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


def log_dec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f'Ошибка {e} в функции {func.__name__} при аргументах {args}, {kwargs}')
        return None

    return wrapper