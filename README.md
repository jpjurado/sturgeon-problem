<b>Problem 6.</b> 

Breaking the Nazi Code In this problem you will be asked to break the Geheimschreiber (a.k.a. the G-writer, or the Sturgeon). (We thank Johan Hastad for the following description of the Geheimschreiber.) The Geheimschreiber had 10 wheels of lengths, 47,53,59,61,64,65,67,69,71,and 73 respectively. Each position on each wheel contained a bit. The plaintext and crypto-text alphabets were given by the string 

2T3O4HNM5LRGIPCVEZDBSYFXAWJ6UQK7 

in that 2 corresponds to the integer 0, T to 1 etc.until 7 the corresponds to 31. 

Each day a fixed permutation of the wheels was chosen e.g. it could be that the wheel of length 71 was put in position one, the wheel of length 59 was set in position two etc. This remained fixed for the day. Each wheel was then rotated to a starting position that was different for each message. We here assume that the starting position was agreed between the sender and receiver. In some situations some of the positions were transmitted as part of the message but this is not the case for our messages. Encryption was performed as follows. 

Read one bit from each of the ten wheels getting bits b0, b1, b2, b3, b4, b5, b6, b7, b8 and b9. 
Use the given alphabet to convert the clear-text to a number between 0 and 31 and let c0, c1, c2 c3 and c4 be the bits of this written in binary. 
For i = 0 . . . 4, ci = ci ⊕ bi (take xor) • If b5 is 1 interchange c0 and c4. 
If b6 is 1 interchange c0 and c1. 
If b7 is 1 interchange c1 and c2. 
If b8 is 1 interchange c2 and c3. 
If b9 is 1 interchange c3 and c4. 1-3 
Output the character written as c0 . . . c4 in binary 

Before the next character was encrypted each wheel is stepped one step. 

Implement the encryption and decryption algorithm. Check your implementation with the plaintext, wheel configuration and ciphertext given on the course web page. 
On the course homepage you will find a plaintext and corresponding ciphertext under some wheel configuration. You are given that the order of the wheels is 47,53,59,61,64,65,67,69,71,and 73 (i.e. b0 comes from the 47-size wheel). Recover the bits on all wheels (you may assume without loss of generality that the offset is 0 for all wheels). 
On the course homepage you will find another plaintext and corresponding ciphertext under some wheel configuration. For this part of the problem, you no longer know the wheel order. Recover the bits on all the wheels and additionally the order of the wheels (again, you may assume without loss of generality that the offset is 0 for all wheels). 
(Bonus) You have a number of intercepted G-writer ciphertexts in the directory called ”bonus”; decode them! Hint: The plaintext follows the same structure as the plaintext in the earlier questions on the HW (e.g., they have the same header). 
