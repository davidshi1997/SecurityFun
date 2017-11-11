## Bandit Level 19 → Level 20
Here, we’re seeing a setuid binary for the first time. All it does is let us run a command as another user, so we can easily cat the next password.
- ssh bandit19@bandit.labs.overthewire.org -p 2220
- ./bandit20-do
    - Run a command as another user.    Example: ./bandit20-do id
- ./bandit20-do cat /etc/bandit_pass/bandit20
    - GbKksEFF4yrVs6il55v6gwY5aVje5f0j
