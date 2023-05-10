import time

# this benchmark decorator which will decorate a function with
# time stumps to calculate performing time

def time_decorator(decorated_function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = decorated_function(*args, **kwargs)
        print('Spent to perform: ', time.time() - start, 'second(s).')
        return result
    return wrapper

# example of use
if __name__ == '__main__':
    @time_decorator
    def sum(a, b):
        return a + b

    print(sum(2, 3))
