__test__ = False

if __name__ == '__main__':
    import eventlet
    eventlet.monkey_patch()
    import multiprocessing.pool
    multiprocessing.util.log_to_stderr(level=1)

    def fun():
        eventlet.sleep(0.01)
        return 42

    pool = multiprocessing.pool.ThreadPool(2)
    result = pool.apply_async(fun, []).get()
    assert result == 42
    pool.close()
    pool.join()
    print('pass')
