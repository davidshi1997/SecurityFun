## Bandit Level 21 → Level 22
Our first encounter with cronjobs! 
- ssh bandit21@bandit.labs.overthewire.org -p 2220
- cat cronjob_bandit22
- cat /usr/bin/cronjob_bandit22.sh
    - Once we read this file, we can see that the password is stored in a temporary directory every minute. We just need to find the directory.
- cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
    - Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
