# Base64-Brute-Force
This is my first personal project for my study
## About Base64
Base64 is is a popular method of encoding binary data into ASCII text format.
Base64 is also widely used for sending e-mail attachments, because SMTP – in its original form – was designed to transport 7-bit ASCII characters only. Encoding an attachment as Base64 before sending, and then decoding when received, assures older SMTP servers will not interfere with the attachment.
Read more about [Base64](https://en.wikipedia.org/wiki/Base64).

### Base64 encode
1.Splitting the data

The input data (usually binary) is divided into blocks of 3 bytes (24 bits).Each byte contains 8 bits, so 3 bytes will form a block of 24 bits.

2.Converting to an integer

The 24-bit block is divided into 4 groups of 6 bits.
Each group of 6 bits will be converted to an integer from 0 to 63.

3.Finding the corresponding character

Each integer from 0 to 63 will be mapped to a character in the Base64 table. 
This [table](https://datatracker.ietf.org/doc/html/rfc4648#section-4) includes:
```
  26 uppercase characters: A-Z (0-25)
  26 lowercase characters: a-z (26-51)
  10 digits: 0-9 (52-61)
  2 special characters: + (62) and / (63)
```
4.Padding

If the input data is not a multiple of 3 bytes, Base64 will add padding characters (=) to the end of the encoded string.
If 1 byte is missing: add 2 = signs.
If 2 bytes are missing: add 1 = sign.

5.Final result

The final result will be an ASCII text string, which is safe to transmit over protocols that do not support binary data.

### Base64 decode
Example:
```
Input: "TWFu" (represents "Man")
```
Step 1: Convert character to integer
```
T → 19
W → 22
F → 5
u → 46
```
Step 2: Concatenate the integers into 24 bits
```
19 = 010011
22 = 010110
5  = 000101
46 = 101110
```
Combine into:
```
01001101 01100001 01101110
```
Step 3: Divide into 3 bytes
```
Byte 1: 01001101 → M
Byte 2: 01100001 → a
Byte 3: 01101110 → n
```
Output:
```
Base64 decoded : "Man"
```
### How to run:
    +) Clone this git/Download files  directly
    +) Use latest python
    +) Run file

[Download directly here](base64_bruteforce.py)

> [!NOTE]
> When you run the file, it will show you options.
