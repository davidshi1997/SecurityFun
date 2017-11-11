## Bandit Level 10 -> Level 11
Apparently data.txt comes in base64, so we need to decode it using the base64 command.
- ssh bandit10@bandit.labs.overthewire.org -p 2220
- ls
- base64 -d data.txt
    - decodes the base64 text in the file
    - IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
