## Bandit Level 11 -> Level 12
This time, data.txt is encoded with a basic caesar cipher. All we need to do is rotate it back.
- ssh bandit11@bandit.labs.overthewire.org -p 2220
- ls
- cat data.txt | tr '[a-z][A-Z]' '[n-za-m][N-ZA-M]'
    - 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
