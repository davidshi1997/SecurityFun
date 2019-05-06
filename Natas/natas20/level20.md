## Natas Level 19 → Level 20
- Go to url: http://natas20.natas.labs.overthewire.org
    - User: natas20
    - Password: eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF
- Another challenge with along a similar vein of hijacking an admin session
- In this case, it looks like they actually put a little more effort into making the cookie
    - It follows the standard php session_set_save_handler
    - Most importantly, we should watch the myread and mywrite, which store and retrieve session cookies
- Now for some sleuthing
    - Let's take a closer look starting with mywrite
        - First, it checks that the SID is composed of numbers and letters
        - Next, the session is split with each key value pair on a new line
        - Finally, a file named after the SID is created with this data stored directly inside
    - Next, let's observe myread
        - First, the file named after the SID is opened
        - Next, the contents are split by \n (newline) and stored in an array by their key value pairs
    - The last point of importance is the print_credentials portion
        - It checks only for a key called admin and whether it is 1 and then allows showing of the admin information
- Based on this, the solution is very simple, we just need to submit "a\nadmin 1", which will first be saved. Afterwards, we will refresh and the newly written file will be split up by \n and the admin token will be read into existence
    - With the power of percentage encoding we can easily adjust the string to "a%0Aadmin%201"
    - Unfortunately, when we submit this in browser, the % will automatically be percent encoded, so we need to rely on another method
- We will use direct URL encoding, Python, and Burp suite

URL encoding
- All we have to do is go to the url
- http://natas20.natas.labs.overthewire.org/index.php?name=admini%0Aadmin%201
    - IFekPyrQXftziDEsUr3x21sYuahypdgJ

Python
- A very basic script using the requests library can be used with url encoding above or directly submitting the fields
    - IFekPyrQXftziDEsUr3x21sYuahypdgJ

Burp suite
- After turning on the interceptor, we can catch a POST request to natas20
    - This request can be sent to the repeater by right clicking
    - Now we modify the name to be our preferred string send it twice!
    - IFekPyrQXftziDEsUr3x21sYuahypdgJ
