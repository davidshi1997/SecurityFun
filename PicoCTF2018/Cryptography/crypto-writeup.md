#PicoCTF Cryptography Walkthrough

##Crypto Warmup 1
- Looking at the table, we see that this is a Vigenere cipher!
- To use the Vigenere square, ciphertext as the rows, plaintexxt as the columns, key in the body
- ciphertext: llkjmlmpadkkc    key: thisisalilkey
- SECRETMESSAGE is the plaintext

##Crypto Warmup 2
- They mention this is rot13, which is... just rotating every character by 13
- picoCTF{this_is_crypto!} is the plaintext

##HEEEEEEERE'S Johnny!
- Looking at the two files they provide, one of them looks awfully like a /etc/shadow file
- These shadow files are typically used to store hashed passwords in a certain format
    - That is username:$encrypt_type$salt$hash:misc
- Looking at the encrypt type, we can tell that this hash uses SHA-512
- We can crack this using hashcat and the rockyou commonly used passwords hinted at
    - tail shadow | awk -F ':' '{print $2}' >> password.hash
    - hashcat -m 1800 -ai/Documents/School/Sololearn/CompSec/dictionaries/rockyou.txt -O
- picoCTF{J0hn_1$_R1pp3d_5f9a67aa}
- P.S. From the name, they seem to be recommending John the Ripper, but I didn't notice...

##caesar cipher 1
- This is just a simple caesar cipher, which we can decrypt with online tools
- The ciphertext is payzgmuujurjigkygxiovnkxlcgihubb
- I used https://www.dcode.fr/caesar-cipher but you can use anything you want
    - Looking through all the shifts, the +6 shift kind of looks like a proper flag
- picoCTF{justagoodoldcaesarcipherfwacbovv}

##hertz
- Here, they give us a nc to connect to, so let's check it out: nc 2018shell3.picoctf.com 18581
- It gave us back a ciphertext that I put into hertz.txt
- Using a frequency analyzer, we can recreate the alphabet for this ciphertext
    - U B A J O P H I T F E N Y D R M C Q S L X K G V Z W
    - E A T O H S N I R D L U F C M W Y G P V B K Q X
    - After decrypting, it seems like this is an excerpt from Don Quixote
- substitution_ciphers_are_solvable_uyhyldalrg

##blaise's cipher
- This is another Vigenere cipher, which there are a lot of online tools for
    - I used https://www.dcode.fr/vigenere-cipher
    - It has a feature that decrypts withs statistical analysis, so we can guess a key from the first paragraph
- We find the key FLAG
- Then we can use it on the key, which is pretty obviously in the middle of the ciphertext
- picoCTF{v1gn3r3_c1ph3rs_ar3n7_bad_cdf08bf0}

##hertz 2
- Here, they give us a nc to connect to, so let's check it out: nc 2018shell3.picoctf.com 23479
- This can be solved again using the concept of frequency analysis like the previous hertz
    - I used this site http://crypto.interactive-maths.com/frequency-analysis-breaking-the-code.html
- picoctf{substitution_ciphers_are_too_easy_nlrgrwmynn}

##safeRSA
- This is finally a modern encryption, RSA!
- We can exploit the vulnerability of having a small e, since the mod won't mask it at all
    - iroot(mpz(2205316413931134031046440767620541984801091216351222789180535786851451917462804449135087209259828503848304180574549372616172217553002988241140344023060716738565104171296716554122734607654513009667720334889869007276287692856645210293194853),mpz(3))
    - hex(13016382529449106065839070830454998857466392684017754632233814825405652260960637)
    - bytearray.fromhex("7069636f4354467b655f7734795f7430305f736d3431315f33343039363235397d").decode()
- picoCTF{e_w4y_t00_sm411_34096259}

##caesar cipher 2
- This seems to be another caesar cipher, except with ascii
- Since we know that the beginning must be picoCTF, we can find the shift easily
- def asciiCaesar(s):
	temp = s[0]
	upshift = 0
	solution = []
	while (temp != 'p'):
		temp = chr(ord(temp)+1)
		upshift = upshift + 1
	temp = s[4]
	downshift = 0
	while (temp != 'C'):
		temp = chr(ord(temp)-1)
		downshift = downshift - 1
	for c in s:
		i = ord(c)+upshift
		if i > 127:
			i = ord(c)+downshift
		solution.append(chr(i))
	return ''.join(solution)
- picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}

##rsa-madlibs
- This is the first more modern encryption, RSA!
- Let's scope out the netcat they gave us first: nc 2018shell3.picoctf.com 36859
    - 	Hello, Welcome to RSA Madlibs
	Keeping young children entertained, since, well, nev3r
	Tell us how to fill in the blanks, or if it's even possible to do so
	Everything, input and output, is decimal, not hex
	#### NEW MADLIB ####
	q : 93187
	p : 94603
	##### WE'RE GONNA NEED THE FOLLOWING ####
	n
	IS THIS POSSIBLE and FEASIBLE? (Y/N):Y
    - It seems like they are just asking us to obtain numbers related to RSA
    - It'll be helpful to have another window open to whip up some python when needed
- This was a little long, so the full question is in another text file called rsa-madlibs.txt
- The final plaintext is 240109877286251840533272915662757983981706320845661471802585807564915966910384375649897669765182077
- We need to convert this to hex, then ascii, we will get the flag
    - 0x7069636f4354467b64305f755f6b6e30775f7468335f7740795f325f5253405f39646337356431327d
    - picoCTF{d0_u_kn0w_th3_w@y_2_RS@_9dc75d12}

##SpyFi
- This is another more modern cryptography question! It's time to handle AES-ECB mode
- Really, ECB is just awful unless you're only encrypting a single block
- Let's see what it would look like if I used a fake flag and some of my own input, since we know ECB encrypts by splitting into 16 byte blocks
    - 	Agent,\nGreetings
	. My situation r
	eport is as foll
	ows:\nAAAAAAAAAAA
	de is: picoCTF{x
	CCCCCCCCCCCCCCCC
	CCCCCCCC\nMy agen
	t identifying co
	de is: picoCTF{t
	his_is_a_flag}.\n
	Down with the So
	viets,\n006\n  - with 5 character padding
- We can't be sure how long the message is, so I played it a little safe in my code with a buffer of 48
- You can see my solution in spyfi.py
- picoCTF{@g3nt6_1$_th3_c00l3$t_1028618}

##super-safe rsa
- It seems like its another RSA question where we get the following values
    - 	c: 9125683611266651067436136529886906035767932796842287669849659671177722034531887                                                                                     
	n: 14210331343297585354458135607699966236077689070980311982043378155096748100255607                                                                          
	e: 65537
- The n value seems a little small, so we can bruteforce out a p and q
    - Trivial algorithms are quite slow, so make sure to find a good site
    - https://www.alpertron.com.ar/ECM.HTM	
- p: 97025682909623703640642359888749220101
q: 146459482862223716397365917561551755224907
totient(n): 14210331343297585354458135607699966235931132562435178641942371595175307595810600
d: 2655289647527690163582317296365317096071114780346692672066562133672838500668273
    - 	pow(9125683611266651067436136529886906035767932796842287669849659671177722034531887,2655289647527690163582317296365317096071114780346692672066562133672838500668273,14210331343297585354458135607699966236077689070980311982043378155096748100255607)
    -	hex(198614235373674103789367498165241205414198384663776181046663386474495750269)
    - 	bytearray.fromhex("7069636f4354467b7573335f6c40726733725f7072316d33245f333436307d").decode()
- picoCTF{us3_l@rg3r_pr1m3$_3460}

##eleCTRical
- Let's take a look at the code we're given
    - From the looks of it, it's an AES-CTR mode encryption this time
    - The code looks good until about line 18 and 26 where they reuse the same counter for all encrypt and decrypt
- Based on this, we can use the property of CTR mode to obtain the flag share code
    - Essentially, CTR mode combines a Nonce and Counter with any lossless operation and then encrypted with a Key
    - By xor-ing this final value with the plaintext, a ciphertext can be obtained
    - However, by reusing the same counter repeatedly, the final encrypted xor value never changes, so if we can obtain it, everything becomes very simple
- In the program eleCTR.py, 


##super-safe rsa 2
- They're hitting us with another 'safe' rsa, let's see what we get this time: nc 2018shell3.picoctf.com 56543
    - 	c: 3286997629288152254701495442746713422912075100800961850745052466756698916540300294622556055507376476994056826951303748974152778717842903578923777790147474031281714601314815467828690326712568714594454276036496866991262795910030933634915550129315522018230297686239745847511811524133261547044019002972653516259
	n: 128563390315770008426997236803822377855872601082428473101117314986561383384666883780637509301060825524831117114585636449484664837436501607320517770480113603494968369554273065890275697688598199977124916003115666382611124848136912491958121367219038083130056171444258958103165256228915650826733626941385046180177
	e: 23964026063100941803015063930230162623973323387139268312605842804459066777958872885000348102930543732721011438908984769930034418025303319270449442058456558910273662347986052507708183592570160073560834882189580093972401559919866847166305616709210146843290907871347541024837710909478200081170867014192312628193
- Based on the hint it seems like they're telling us d might be the usual value of e: 65,537
- Let's plug it in and give it a shot!
    - pow(3286997629288152254701495442746713422912075100800961850745052466756698916540300294622556055507376476994056826951303748974152778717842903578923777790147474031281714601314815467828690326712568714594454276036496866991262795910030933634915550129315522018230297686239745847511811524133261547044019002972653516259,65537,128563390315770008426997236803822377855872601082428473101117314986561383384666883780637509301060825524831117114585636449484664837436501607320517770480113603494968369554273065890275697688598199977124916003115666382611124848136912491958121367219038083130056171444258958103165256228915650826733626941385046180177)
    - hex(264003602020102370693041857442610586342633199683725005643958437442448465210344626586049655751883798592626440573)
    - bytearray.fromhex("7069636f4354467b77407463685f793075725f5870306e336e74245f6340723366753131795f343133373939397d").decode()
- picoCTF{w@tch_y0ur_Xp0n3nt$_c@r3fu11y_4137999}
- But what's the actual way to solve this...
    - After doing some research, I found Wiener's attack, which applies when d is small, or, more precisely, d < (1/3) * N^(1/4)
    - By only using convergents found from fraction expansion as possible k and d values, d can be found in a reasonable amount of time
    - Doing a wiener attack on this once again gives us the key 65,537!

Magic Padding Oracle
- 



