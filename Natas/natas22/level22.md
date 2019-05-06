## Natas Level 21 → Level 22
- Go to url: http://natas22.natas.labs.overthewire.org
    - User: natas22
    - Password: chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ
- This one starts out looking a little strange, but after looking at the source code, it's no biggy
    - If the key revelio exists, it will show the password. BUT if the user isn't an admin, it will redirect immediately
- With Burp suite, this becomes no problem at all
- Turning intercept on, we intercept a request to natas22 and send it to repeater
    - Then we just send it and look at the response with our password
    - D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE