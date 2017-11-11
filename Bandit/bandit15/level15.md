## Bandit Level 15 → Level 16
We need to use SSL/TLS to connect to this server, so openssl comes in handy.
- ssh bandit15@bandit.labs.overthewire.org -p 2220
- openssl s_client -connect localhost:30001 -quiet
    - openssl connects using SSL/TLS to a remote server
- BfMYroe26WYalil77FoDi9qh59eK5xNr
    - cluFn7wTiGryunymYOu4RcffSxQluehd
