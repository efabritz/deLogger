import datetime

def logger(fct):
    def dateTimeFile(*args, **kwargs):
        with open('deco_file.txt', 'w') as file:
            t_date = datetime.datetime.now()
            f_name = fct.__name__
            f_args = ''
            for arg in args:
                f_args += f'{arg} '
            f_return = fct(*args, **kwargs)
            line = f'date: {t_date}, name: {f_name}, arguments: {f_args}, returns: {f_return} \n'
            file.write(line)
        return f_return
    return dateTimeFile

@logger
def fun_func(mult1, mult2):
    arg_to_return = mult1 * mult2
    return arg_to_return

def logger_with_path(log_path):
    def logger(fct):
        def dateTimeFile(*args, **kwargs):
            with open(log_path, 'w') as file:
                t_date = datetime.datetime.now()
                f_name = fct.__name__
                f_args = ''
                for arg in args:
                    f_args += f'{arg} '
                f_return = fct(*args, **kwargs)
                line = f'date: {t_date}, name: {f_name}, arguments: {f_args}, returns: {f_return} \n'
                file.write(line)
            return f_return
        return dateTimeFile
    return logger

@logger_with_path('deco_logger.txt')
def fun_func2(mult1, mult2):
    arg_to_return = mult1 * mult2
    return arg_to_return


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
fun_func(5, 5)
if __name__ == '__main__':
    fun_func(5, 5)
    fun_func2(10, 10)
