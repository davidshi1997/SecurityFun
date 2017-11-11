## Bandit Level 16 → Level 17
Here, we need to find an open port to use on the machine in the range 31000-32000, using nmap.
- ssh bandit16@bandit.labs.overthewire.org -p 2220
- nmap -A -T4 localhost -p31000-32000
    - PORT      STATE SERVICE VERSION
    - 31046/tcp open  echo
    - 31518/tcp open  msdtc   Microsoft Distributed Transaction Coordinator (error)
    - 31691/tcp open  echo
    - 31790/tcp open  msdtc   Microsoft Distributed Transaction Coordinator (error)
    - 31960/tcp open  echo
        - Well we know it’s not the echo servers
- openssl s_client -connect localhost:31518
- openssl s_client -connect localhost:31790
    - Got an RSA private key?
- nano rsaprivate
    - Put in the RSA private key
- chmod 700 rsaprivate
- ssh -i rsaprivate bandit17@localhost
- cat /etc/bandit_pass/bandit17
    - xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn
