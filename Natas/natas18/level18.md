## Natas Level 17 → Level 18
- Go to url: http://natas18.natas.labs.overthewire.org
    - User: natas18
    - Password: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
- Looks like we've been given a pretty basic login application
    - If we take a look we notice some mention of session generation, where an ID is assigned 1 to 640
- After throwing in some random credentials, we get a screen that says we are not the admin
    - Taking a little peek at the cookies using a handy web extension called EditThisCookie, we catch a little cookie called PHPSESSID!
- All of this implies this is vulnerable to a session hijacking attack
    - There are a few approaches to handle this attack, so I'll go over two of them: Python scripting and using Burp suite

Python:
- Unlike previous scripts, we only need to send GET requests with the PHPSESSID cookie modified
    - Using the requests library, it becomes trivial to choose what cookies to send with the GET request
    - All we have to do is increment the cookies starting from 1 until we find and print a result that does not contain 'regular user'
- Sure enough the result pops up on attempt 119, giving us the password
    - 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs

Burp suite:
- This is a fairly basic application of Burp suite but it's still good practice for the future
- To start, we want to go to the Proxy tab and turn on intercept
    - After turning it on, we want to intercept a request to the index.php that has a cookie attached
    - If we right click, we can forward it directly to Intruder which will help us perform the attack
- In Intruder, we want to make sure we highlight only the PHPSESSID cookie so that value is being modified
    - Next, we go to the Payload tab and set the type to Number, iterating from 1 to 640
    - Finally, we go to the Options tab and Add to Grep-Extract the info between "content">\r\n and <div id=
        - This is so we can easily observe where different text appears
- Going back to the Positions tab, we start the attack, which takes a bit, but gives us the password after a while
    - 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs