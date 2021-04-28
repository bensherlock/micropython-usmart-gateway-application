import utime
import builtins

builtinsprint = builtins.print

def newprint(*args, **kwargs):
    timestamp_str = "{:d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(*utime.localtime()[:6])
    return builtinsprint("[" + timestamp_str + "]", *args, **kwargs)


builtins.print = newprint
