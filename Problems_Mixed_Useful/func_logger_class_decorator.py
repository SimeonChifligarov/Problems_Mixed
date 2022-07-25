class func_logger:
    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        log_string = self.func.__name__ + ' was called'
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        return self.func(*args, **kwargs)


@func_logger
def say_hi(name):
    print(f'Hi, {name}!')


say_hi('Peter')
