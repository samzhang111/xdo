import nose
from nose.tools import eq_
import xdo

def test_subst():
    tests = [(['*.*', 'hello.py', 1], 'hello.py'),
             (['dir2/*.*', 'dir/hello.py', 1], 'dir2/hello.py'),
             (['*.*', 'dir/hello.py', 1], 'hello.py'),
             (['dir/*_#.*', 'hello.py', 1], 'dir/hello_1.py'),
             (['dir/*_#.*', 'hello.py', 1], 'dir/hello_1.py'),
             (['*.csv', 'hello.py', 1], 'hello.csv'),
             (['*.csv', 'hello', 1], 'hello.csv'),
             (['hello.*', 'hello.py', 1], 'hello.hello.py'),
             (['hello.*', 'hello', 1], 'hello.hello'),
                         ]

    for i, o in tests:
        yield eq_, xdo.subst(*i), o
