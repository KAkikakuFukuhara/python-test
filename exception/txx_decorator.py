STATUS_SUCCESS = 0
STATUS_UNIVERSUL_ERROR = 1
STATUS_ZERODIVISION_ERROR = 2
STATUS_INDEX_ERROR = 3


def try_catch_decorator(func):
    def decorator(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ZeroDivisionError:
            return STATUS_ZERODIVISION_ERROR
        except IndexError:
            return STATUS_INDEX_ERROR
        except:
            return STATUS_UNIVERSUL_ERROR
        else:
            return STATUS_SUCCESS
    return decorator


@try_catch_decorator
def access_idx(x, idx):
    x[idx]


@try_catch_decorator
def mod(x, y):
    z = x / y


def get_var_name(var):
    for n, v in globals().items():
        if v == var:
            return n

# success
print(get_var_name(access_idx([1], 0)))
# index error
print(get_var_name(access_idx([], 1)))
# success
print(get_var_name(mod(2, 1)))
# division error
print(get_var_name(mod(2, 0)))
