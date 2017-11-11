## Bandit Level 9 -> Level 10
Not everything in data.txt is human readable, and the ones that involve the password start with a number of equals.
- ssh bandit9@bandit.labs.overthewire.org -p 2220
- strings data.txt | grep ==
    - strings prints out only the printable characters
    - truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
