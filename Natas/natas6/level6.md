## Natas Level 6 → Level 7
- Go to url: http://natas6.natas.labs.overthewire.org
    - User: natas6
    - Password: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
- The input tells us to put in a secret, and there is also a link to the source code
- In the source code, the php block that is used to process the secret is wrapped in <? ?>
- Inside, it uses the variable $secret, which isn’t anywhere on the page… so it’s probably from the include
- Trying to go to the includes/secret.inc directory… works!
    - FOEIUWGHFEEUHOFUOIU
- Input the secret we found into the field to get the password
    - 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
