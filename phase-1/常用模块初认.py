'''
import getpass

name = raw_input("please input your username:")
password = getpass.getpass('please type your password:')

print name+', ' + password
'''

import os
os.system('df')
cmd_res = os.system('df -h')
os.mkdir('yourDir')
cmd_res = os.popen('df -h').read()
'''
>>> import os
>>> cmd_res = os.system('df -h')
Filesystem                              Size   Used  Avail Capacity iused      ifree %iused  Mounted on
/dev/disk1                             465Gi   66Gi  399Gi    15% 1406893 4293560386    0%   /
devfs                                  187Ki  187Ki    0Bi   100%     646          0  100%   /dev
map -hosts                               0Bi    0Bi    0Bi   100%       0          0  100%   /net
map auto_home                            0Bi    0Bi    0Bi   100%       0          0  100%   /home
/Users/jiaqixu/Downloads/Caffeine.app  465Gi   56Gi  408Gi    13% 1316264 4293651015    0%   /private/var/folders/wg/l7bm_36j0j7d050l8hctyvc80000gp/T/AppTranslocation/64794938-D7CF-4843-8A15-E6C86397DD4B
/dev/disk2s1                            10Mi  1.5Mi  8.5Mi    15%      94 4294967185    0%   /Volumes/FileZilla
/dev/disk3s1                            15Mi  4.9Mi   10Mi    33%     262 4294967017    0%   /Volumes/Install Cisco WebEx Add-On
>>> cmd_res
0


>>> cmd_res = os.popen('df -h').read()
>>> cmd_res
'Filesystem                              Size   Used  Avail Capacity iused      ifree %iused  Mounted on\n/dev/disk1                             465Gi   66Gi  399Gi    15% 1406895 4293560384    0%   /\ndevfs                                  187Ki  187Ki    0Bi   100%     646          0  100%   /dev\nmap -hosts                               0Bi    0Bi    0Bi   100%       0          0  100%   /net\nmap auto_home                            0Bi    0Bi    0Bi   100%       0          0  100%   /home\n/Users/jiaqixu/Downloads/Caffeine.app  465Gi   56Gi  408Gi    13% 1316264 4293651015    0%   /private/var/folders/wg/l7bm_36j0j7d050l8hctyvc80000gp/T/AppTranslocation/64794938-D7CF-4843-8A15-E6C86397DD4B\n/dev/disk2s1                            10Mi  1.5Mi  8.5Mi    15%      94 4294967185    0%   /Volumes/FileZilla\n/dev/disk3s1                            15Mi  4.9Mi   10Mi    33%     262 4294967017    0%   /Volumes/Install Cisco WebEx Add-On\n'
>>>
'''


import sys
print sys.path
'''
>>> import sys
>>> sys.path
['', '/usr/local/Cellar/python/2.7.13_1/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', '/usr/local/Cellar/python/2.7.13_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/usr/local/Cellar/python/2.7.13_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/usr/local/Cellar/python/2.7.13_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/usr/local/Cellar/python/2.7.13_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/usr/local/Cellar/python/2.7.13_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/usr/local/Cellar/python/2.7.13_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', '/usr/local/Cellar/python/2.7.13_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', '/Users/jiaqixu/Library/Python/2.7/lib/python/site-packages', '/usr/local/lib/python2.7/site-packages']
'''


