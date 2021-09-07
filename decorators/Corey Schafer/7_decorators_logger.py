def my_logger(orig_func):
    import logging

    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger
def display_info(name, age=38):
    print(f'display_info ran with arguments ({name}, {age})')

display_info('Milan', age=76)