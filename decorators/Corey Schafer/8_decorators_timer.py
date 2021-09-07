def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in: {t2} sec')
        return result

    return wrapper

import time

@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f'display_info ran with arguments ({name}, {age})')

display_info('Milan', 76)