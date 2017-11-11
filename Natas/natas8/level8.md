## Natas Level 8 → Level 9
- Go to url: http://natas8.natas.labs.overthewire.org
    - User: natas8
    - Password: DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
- This level appears to be similar in format to natas6
- In the source code, the user’s input is put through a variety of processes to transform it before comparing it to $encodedSecret = "3d3d516343746d4d6d6c315669563362";
- All you have to do is write something that reverses the encodedSecret to an input you can put in, which I did here
    - $encodedSecret = "3d3d516343746d4d6d6c315669563362"; $hello = base64_decode(strrev(hex2bin($encodedSecret))); echo "secret: $hello";
- This tells us the secret is oubWYf2kBq
    - W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
