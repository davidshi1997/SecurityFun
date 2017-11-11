## Bandit Level 13 -> Level 14
Here, we use the ssh command again, but instead of the usual, we specify a key to use with ‘-i’.
- ssh bandit13@bandit.labs.overthewire.org -p 2220
- ls
    - sshkey.private appears to be a private key meant to be used for bandit14
- ssh -i sshkey.private bandit14@localhost
