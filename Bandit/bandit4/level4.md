## Bandit Level 4 -> Level 5
Only one of the files in the inhere directory is human-readable. This is where file comes in handy.
- ssh bandit4@bandit.labs.overthewire.org -p 2220
- ls
- cd inhere
- file ./*
    - file attempts to classify each argument based on their type
        - https://www.computerhope.com/unix/ufile.htm
    - reveals file07 is in ASCII, readable text
- cat ./-file07
    - koReBOKuIDDepwhWk7jZC0RTdopnAYKh
