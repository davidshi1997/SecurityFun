## Natas Level 20 → Level 21
- Go to url: http://natas21.natas.labs.overthewire.org
    - User: natas21
    - Password: IFekPyrQXftziDEsUr3x21sYuahypdgJ
- This one's interesting! The two websites are collocated, so we should be able to affect one session with the other
- Looking at http://natas21.natas.labs.overthewire.org first
    - Just like last time, there's an admin key in the session that is checked
- Looking at http://natas21-experimenter.natas.labs.overthewire.org/index.php
    - It seems as though each field that can be changed is stored as a key in the SID
    - There's a client side check that makes sure that no extra fields can appear on the website, but doesn't affect what can be sent
- Putting this together, if we can send the admin key in the second site, we can affect the SID which we can then use for the first site
- This time we will use the Browser and Burp suite

Browser
- We can send an addition field to the second website's form by submitting to the form via the URL
    - http://natas21-experimenter.natas.labs.overthewire.org/index.php?align=center&fontsize=100%25&bgcolor=yellow&submit=Update&admin=1
- Next, using an extension like EditThisCookie, we can copy the SID and adjust the first websites cookie to match the SID
- Once we refresh the page, we have our password!
    - chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ

Burp suite
- After turning on the interceptor, we can intercept a POST request to the second site
    - By right clicking, we can send the request to the repeater
    - Here, we will edit the submitted values and include admin=1 like so
    - align=center&fontsize=100%25&bgcolor=yellow&submit=Update&admin=1
    - After we see the request successful, let's copy the cookie to use on the other site
- Next, we will intercept a GET request to the first site
    - We simply have to replace the cookie with the second site's cookie and forward it
- This will give us the page with admin results
    - chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ