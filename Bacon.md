# Bacon
[Code](Bacon.py) <br>
Bacon Ciphers are basically binary code with extra steps. This program will decode a string (in the variable `plain`) and output a Super Secret Message $^{TM}$. Our Bacon Cipher is going to use upper and lowercase letters as 1s and 0s respectively (special characters and whitespace will be filtered out).  <br>
When functioning properly, the program will: 
1. Iterate through the string character by character. If the character is uppercase, store a 1. If lowercase, store a 0. If neither, store nothing and continue.
2. Split the new binary string into chunks of eight (8) characters.
3. Translate each string of eight (8) binary characters into decimals (there may be a [python function](https://www.geeksforgeeks.org/python/python-int-function/) for this...)
4. Translate the decimals into ASCII characters (there may be a [python function](https://www.w3schools.com/python/ref_func_chr.asp) for this...)  

### Output
`Hi`
