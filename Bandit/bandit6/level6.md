## Bandit Level 6 → Level 7
It looks like they really want us to know find. Only one of the file is owned by bandit7, of group bandit6, and 33 bytes large
- ssh bandit6@bandit.labs.overthewire.org -p 2220
- ls
- cd /
- find ./ -user bandit7 -group bandit6 -size 33c
    - -user searches for file owned by the given user
    - -group searches for files owned by the given group
    - -size is the same as the previous level
- cat ./var/lib/dpkg/info/bandit7.password
    - HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
