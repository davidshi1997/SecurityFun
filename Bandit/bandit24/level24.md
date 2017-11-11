## Bandit Level 24 → Level 25
Here we need to write a shell script to brute force this for us… because otherwise it’ll take forever.
- ssh bandit24@bandit.labs.overthewire.org -p 2220
- nano getpass.sh
    - Sends password and pins to localhost, storing the result in result.txt
- sort result.txt | uniq -u
    - uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
