import logging

logger = logging.getLogger(__name__)


def make_log(option: int, instance:  str, id=None):
    message = f'{instance} '
    if option == 1: # New instance is created
        message += 'is created'
    elif option == 2:
        message += f'id={id} is updated'
    elif option == 3:
        message += f'id={id} is deleted'
    elif option == 4:
        message += 'is listed'
    return logger.info(message)