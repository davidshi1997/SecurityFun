## Bandit Level 23 → Level 24
Making our own shell script! The cronjob runs every shell script in a folder at regular intervals.
- ssh bandit23@bandit.labs.overthewire.org -p 2220
- cat /etc/cron.d/cronjob_bandit24
- cat /usr/bin/cronjob_bandit24.sh
    - This cronjob appears to go through all the crons in /var/spool/bandit24 directory and execute them before deleting them every 60 seconds
- cd /var/spool/bandit24
- mkdir /tmp/bandit23
- chmod 777 /tmp/bandit23
- nano bandit23.sh
    - #!/bin/bash cat /etc/bandit_pass/bandit24 > /tmp/bandit23/pass.txt
- chmod 777 bandit23.sh
- /usr/bin/cronjob_bandit24.sh
- cat /tmp/bandit23/pass.txt
    - UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
