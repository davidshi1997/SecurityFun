## Bandit Level 20 → Level 21
Here we need to simultaneously open a port to echo something back to the sender, and send to that port. So we use more commands related to processing.
- ssh bandit20@bandit.labs.overthewire.org -p 2220
- echo GbKksEFF4yrVs6il55v6gwY5aVje5f0j | nc -l 1234 &
- ./suconnect 1234
    - gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
