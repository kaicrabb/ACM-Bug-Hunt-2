# Stream Cipher
[Code](Kasper.py) <br>

Christof and Jan want to send each other secret messages using a stream cipher where $a = 0, b = 1, ... z = 25$. <br>
The stream cipher works by:
- Converting the characters of a ciphertext string (`c`) and a key string (`k`) into their integer equivalents
- For each character, finding the value of `(c-k)%26` 
- Converting the resultes of `(c-k)%26` back into plaintext (`p`)

Jan and Christof's program isn't showing the right results. Find the bug!
<br> 
### Correct Output
`bearcat`
