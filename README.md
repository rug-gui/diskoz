# diskoz
Disk Perf Utility. Run IO Benchmarks. Speed Test for Devices.


Runnung diskoz provides the following result
```bash
master@ZG14:~$ python diskoz.py
Done.
Created 6144 files of 1MB each in 102.98610496520996 seconds.
Creation rate:  59.658533566984815 mb per second
Transferred 6144 files of 1MB each in 147.2998549938202 seconds.
Cleaning up...
Transfer rate:  41.71083535864828 MB per second
```
I designed this to test variable speed in microSD and SSD and HDD in Raspberry Pi for checking small file transfers (usually slower) and large file transfers (usually faster) both.
