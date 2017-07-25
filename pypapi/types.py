from collections import namedtuple


Flips = namedtuple("Flips", "rtime ptime flpins mflips")
Flops = namedtuple("Flops", "rtime ptime flpops mflops")
IPC = namedtuple("IPC", "rtime ptime ins ipc")
EPC = namedtuple("EPC", "rtime ptime ref core evt epc")
