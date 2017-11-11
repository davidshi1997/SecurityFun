## Bandit Level 22 → Level 23
More cronjob interpretation.
- ssh bandit22@bandit.labs.overthewire.org -p 2220
- cd /etc/cron.d
- cat cronjob_bandit23.sh
- cat cronjob_bandit23
- cat cronjob_bandit23.sh
    - Inside we can see that the tmp file it’s stored in is created by : echo I am user $myname  | md5sum | cut -d ' ' -f 1
    - Recreate bandit23’s, using: echo I am user bandit23 | md5sum | cut -d ' ' -f 1
- cat /tmp/8ca319486bfbbc3663ea0fbe81326349
    - jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
