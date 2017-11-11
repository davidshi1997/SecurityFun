## Bandit Level 17 → Level 18
The only lines that are different in the two files can easily be found with diff
- ssh bandit17@bandit.labs.overthewire.org -p 2220
- diff passwords.new passwords.old
    - 42c42
    - < kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
    - ---
    - > R3GQabj3vKRTcjTTISWvO1RJWc5sqSXO
        - kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
