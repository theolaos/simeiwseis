---

---
___
## Comparators

![[Image01.png]]



## Size Comparators

![[Image02.png]]

Size Comparator (type 7485 - 4 Bit)
First Part (schematic and pin layout).
Second Part (explanation of the logic).



![[Image03.png]]



---
## Translation Systems : BCD / XS-3 / Gray

XS-3 : We skip the first three bits
Gray : All values next or before only change one bit.

| Decimal | BCD  | XS-3 | Gray |
| ------- | ---- | ---- | ---- |
| 0       | 0000 | 0011 | 0000 |
| 1       | 0001 | 0100 | 0001 |
| 2       | 0010 | 0101 | 0011 |
| 3       | 0011 | 0110 | 0010 |
| 4       | 0100 | 0111 | 0110 |
| 5       | 0101 | 1000 | 0111 |
| 6       | 0110 | 1001 | 0101 |
| 7       | 0111 | 1010 | 0100 |
| 8       | 1000 | 1011 | 1100 |
| 9       | 1001 | 1100 | 1101 |

BCD : Binary Coded Decimal
XS-3 : Excess 3


---
## Decoders

A **BSD** decoder outputs the right signal based on the **BCD** Input.

![[Image04.png]]


Example Table Below

| Input |       |       | Output |     |     |     |     |     |     |     |
| ----- | ----- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
| $2^2$ | $2^1$ | $2^0$ | 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| 0     | 0     | 0     | 1      | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| 0     | 0     | 1     | 0      | 1   | 0   | 0   | 0   | 0   | 0   | 0   |
| 0     | 1     | 0     | 0      | 0   | 1   | 0   | 0   | 0   | 0   | 0   |
| 0     | 1     | 1     | 0      | 0   | 0   | 1   | 0   | 0   | 0   | 0   |
| 1     | 0     | 0     | 0      | 0   | 0   | 0   | 1   | 0   | 0   | 0   |
| 1     | 0     | 1     | 0      | 0   | 0   | 0   | 0   | 1   | 0   | 0   |
| 1     | 1     | 0     | 0      | 0   | 0   | 0   | 0   | 0   | 1   | 0   |
| 1     | 1     | 1     | 0      | 0   | 0   | 0   | 0   | 0   | 0   | 1   |



#### Binary Decoder (3-Bit) using a Base8 system. It has a **NAND** gate at every output

![[Image05.png]]



#### 3-Bit Decoder with 3 Channels to 8 Channels Output

![[Image06.png]]



#### 8-Channel Output Decoder (74138)

Pins Layout
![[Image07.png]]


Circuit Symbol
![[Image08.png]]


Circuit Diagram
![[Image09.png]]



---
## Encoders

**Base10** to **BCD** or **Base2** conversion.

![[Image11.png]]



Logic Gates Diagram

![[Image12.png]]

Algebra Boole :

$$
A = I_1 + I_3 + I_5 + I_7 + I_9
$$
$$
B = I_2 + I_3 + I_6 + I_7
$$
$$
C = I_4 + I_5 +I_6 + I_7
$$
$$
D = I_8 + I_9
$$

Results Table Below

| Decimal Input | BCD Output |     |     |     |
| ------------- | ---------- | --- | --- | --- |
|               | D          | C   | B   | A   |
| 0             | 0          | 0   | 0   | 0   |
| 1             | 0          | 0   | 0   | 1   |
| 2             | 0          | 0   | 1   | 0   |
| 3             | 0          | 0   | 1   | 1   |
| 4             | 0          | 1   | 0   | 0   |
| 5             | 0          | 1   | 0   | 1   |
| 6             | 0          | 1   | 1   | 0   |
| 7             | 0          | 1   | 1   | 1   |
| 8             | 1          | 0   | 0   | 0   |
| 9             | 1          | 0   | 0   | 1   |



#### 8-Channel Encoder (74147)

**Base10** to **BCD** converter with **LOW** output

![[Image13.png]]



---
## Base Conversion

#### BCD to Binary with the IC 71484

![[Image14.png]]


#### BCD to 7-Segment Display

![[Image15.png]]

![[Image16.png]]

![[Image17.png]]


Binary Table Below

| A   | B   | C   | D   | a   | b   | c   | d   | e   | f   | g   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 0   |
| 0   | 0   | 0   | 1   | 0   | 1   | 1   | 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 0   | 1   | 1   | 0   | 1   | 1   | 0   | 1   |
| 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 0   | 0   | 1   |
| 0   | 1   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 1   | 1   |
| 0   | 1   | 0   | 1   | 1   | 0   | 1   | 1   | 0   | 1   | 1   |
| 0   | 1   | 1   | 0   | 1   | 0   | 1   | 1   | 1   | 1   | 1   |
| 0   | 1   | 1   | 1   | 1   | 1   | 1   | 0   | 0   | 0   | 0   |
| 1   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| 1   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | 0   | 1   | 1   |

![[Image19.png]]

![[Image18.png]]



---
