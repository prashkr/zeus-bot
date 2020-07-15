import time


def timeit(method):
    """
    Use this decorator to debug running time of any method.
    Usage:
        Add @timeit on top of the function you want to time
    """
    def timed(*args, **kw):
        t_start = time.time()
        result = method(*args, **kw)
        t_end = time.time()
        print('{}: {}ms'.format(method.__name__, (t_end - t_start) * 1000))
        return result
    return timed
