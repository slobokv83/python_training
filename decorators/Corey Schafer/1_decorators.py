def decorator_function(message):
    def wrapper_function():
        print(message)
    return wrapper_function

hi_func = decorator_function('Hi')
bye_func = decorator_function('Bye')

hi_func()
bye_func()