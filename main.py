import datetime
import inspect

def logger(fct):
    signature = inspect.signature(fct)
    def dateTimeFile(*args, **kwargs):
        bound_args = signature.bind(*args, **kwargs)
        with open('deco_file.txt', 'w') as file:
            t_date = datetime.datetime.now()
            f_name = fct.__name__
            f_args = ''
            for arg in bound_args.args:
                f_args += f'{arg} '
            f_return = fct(*args, **kwargs)
            line = f'date: {t_date}, name: {f_name}, arguments: {f_args}, returns: {f_return} \n'
            file.write(line)
        return
    return dateTimeFile

@logger
def fun_func(mult1, mult2):
    arg_to_return = mult1 * mult2
    return arg_to_return

fun_func(5, 5)

def logger_with_path(log_path):
    def logger(fct):
        signature = inspect.signature(fct)
        def dateTimeFile(*args, **kwargs):
            bound_args = signature.bind(*args, **kwargs)
            with open(log_path, 'w') as file:
                t_date = datetime.datetime.now()
                f_name = fct.__name__
                f_args = ''
                for arg in bound_args.args:
                    f_args += f'{arg} '
                f_return = fct(*args, **kwargs)
                line = f'date: {t_date}, name: {f_name}, arguments: {f_args}, returns: {f_return} \n'
                file.write(line)
            return
        return dateTimeFile
    return logger

@logger_with_path('deco_logger.txt')
def fun_func2(mult1, mult2):
    arg_to_return = mult1 * mult2
    return arg_to_return

fun_func2(10, 10)

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

@logger_with_path('flatlist_decor.txt')
def flat_generator(nested_list):
    pointer = 0
    ipointer = 0
    while pointer < len(nested_list):
        while ipointer < len(nested_list[pointer]):
            result = nested_list[pointer][ipointer]
            yield result
            ipointer += 1
        pointer += 1
        ipointer = 0

for item in flat_generator(nested_list):
     print(item)