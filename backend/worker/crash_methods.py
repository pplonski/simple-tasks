
def crash_with_segfault():
    import sys
    try:
        sys.setrecursionlimit(1<<30)
        f = lambda f:f(f)
        f(f)
    except Exception as e:
        raise Exception('Segfault is not catched')

def crash_with_import():
    import dupa # there is no such package
