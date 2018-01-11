# Force non-green threading for multiprocessing.pool
from eventlet import patcher
from eventlet.green import time
# from eventlet.green import Queue
from eventlet.support import six

__patched__ = ['Pool', 'ThreadPool']

__orig_threading = patcher.original('threading')
__orig_queue_name = 'Queue' if six.PY2 else 'queue'
__orig_queue = patcher.original(__orig_queue_name)

patcher.inject(
    'multiprocessing.pool',
    globals(),
    (__orig_queue_name, __orig_queue),
    ('threading', __orig_threading),
    ('time', time),
)

del patcher
