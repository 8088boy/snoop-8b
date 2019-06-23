from tests.test_snoop import sample_traceback


@snoop
def main():
    x = 1
    y = 2
    try:
        pp.deep(lambda: x + y + bad() + 2)
    except:
        sample_traceback()


def bad():
    raise TypeError('bad')


expected_output = """
12:34:56.78 >>> Call to main in File "/path/to_file.py", line 5
12:34:56.78    5 | def main():
12:34:56.78    6 |     x = 1
12:34:56.78    7 |     y = 2
12:34:56.78    8 |     try:
12:34:56.78    9 |         pp.deep(lambda: x + y + bad() + 2)
12:34:56.78 LOG:
12:34:56.78 ................ x = 1
12:34:56.78 ................ y = 2
12:34:56.78 ............ x + y = 3
12:34:56.78 ................ bad = <function bad at 0xABC>
12:34:56.78 !!! TypeError: bad
12:34:56.78 !!! When calling: pp.deep(...)
12:34:56.78   10 |     except:
12:34:56.78   11 |         sample_traceback()
Traceback (most recent call last):
    pp.deep(lambda: x + y + bad() + 2)
    return self._pp([arg], frame, deep=True)
    returns = deep_pp(self._write, event, call_arg.body, frame)
    return eval(code, frame.f_globals, frame.f_locals)
    pp.deep(lambda: x + y + bad() + 2)
    raise TypeError('bad')
TypeError: bad
12:34:56.78 <<< Return value from main: None
"""
