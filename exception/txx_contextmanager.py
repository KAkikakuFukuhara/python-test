from contextlib import contextmanager

STATUS_SUCCESS = 0
STATUS_UNIVERSUL_ERROR = 1
STATUS_ZERODIVISION_ERROR = 2
STATUS_INDEX_ERROR = 3


def access_idx(x, idx):
    x[idx]

def mod(x, y):
    z = x / y


def get_var_name(var):
    for n, v in globals().items():
        if v == var:
            return n


@contextmanager
def trycatch():
    status: int
    try:
        yield
    except ZeroDivisionError:
        status = STATUS_ZERODIVISION_ERROR
    except IndexError:
        status = STATUS_INDEX_ERROR
    except:
        status = STATUS_UNIVERSUL_ERROR
    else:
        status = STATUS_SUCCESS
    finally:
        print(get_var_name(status))


# success
with trycatch():
    access_idx([1], 0)
# index error
with trycatch():
    access_idx([], 1)
# success
with trycatch():
    mod(2, 1)
# division error
with trycatch():
    mod(2, 0)
