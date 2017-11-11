## Bandit Level 5 -> Level 6
Only one of the files in the directories is human-readable, 1033 bytes large, and not executable. 
- ssh bandit5@bandit.labs.overthewire.org -p 2220
- ls
- cd inhere
- ls
- find ./ -type f -size 1033c -exec cat {} \;
    - -type searches for ‘f’ files or ‘d’ directories
    - -size searches for file of specified block size or byte size if c is at the end of size
    - -exec executes the given command replacing {} with the file names and ending with \;
    - DXjZPULLxYr17uwoI01bNLQbtFemEgo7
