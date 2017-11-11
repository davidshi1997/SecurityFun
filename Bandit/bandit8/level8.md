## Bandit Level 8 -> Level 9
There’s only one line in data.txt that is unique, so uniq and sort come in handy here.
- ssh bandit8@bandit.labs.overthewire.org -p 2220
- ls
- sort data.txt | uniq -u
    - It’s necessary to sort first, since uniq only checks lines in a row
    - UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
