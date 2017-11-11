## Bandit Level 1 -> Level 2
Examining the effects of file names in commands
- ssh bandit1@bandit.labs.overthewire.org -p 2220
- ls
    - The file is named “-“, which makes it not possible to cat directly to it
- cat ./- 
    - Ensure that it is seen as a file
    - CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
