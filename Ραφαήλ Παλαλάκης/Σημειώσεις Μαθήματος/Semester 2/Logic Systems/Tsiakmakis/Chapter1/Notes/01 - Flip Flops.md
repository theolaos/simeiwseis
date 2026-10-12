___
## Εισαγωγή

Πύλες
- Μανδαλωτής
 Με **NAND**
Με **NOR**
- Flip Flop
**SR**
**D**
**JK**
**T**


___
## Πύλες

![[AND-GATE.png]]

![[OR-GATE.png]]

![[NOT-GATE.png]]

![[NAND-GATE.png]]

![[NOR-GATE.png]]


___
# Σύνθετες Πύλες

![[AND&NOR-GATE.png]]

![[NAND&OR-GATE.png]]

![[OR&NAND-GATE.png]]

![[NOR&AND-GATE.png]]

![[XOR-GATE.png]]

![[XNOR-GATE.png]]


---
## Άλγεβρα Boole

1. $A*0=0$
2. $A*1=A$
3. $A+0=A$
4. $A+1=1$
5. $A*A=A$
6. $A+A=A$
7. $A*\overline{A}=0$
8. $A+\overline{A}=A$
9. $\overline{\overline{A}}=A$
10. $A+(A*B)=A=A*(A+B)$

## De Morgan

$\overline{A*B} = \overline{A} + \overline{B}$
$\overline{A+B} = \overline{A} * \overline{B}$


---
## Flip Flop

Έχει δύο σταθερές καταστάσεις, το 0 ή το 1 (ως έξοδος).

Λειτουργεί επίσης και σαν μνήμη, αφου η εξοδός του είναι σταθερή μεχρι να την αλλάξει κάποιο **Clock Pulse**.

Ονομάζεται επίσης κύτταρο μνήμης και χρησιμοποιήται σε **SDRAM**


---
## Είδη και Σύμβολα Flip Flops

##### SR
![[SR-FF.png]]

| S   | R   | Q(t+1)         |
| --- | --- | -------------- |
| 0   | 0   | Q(t)           |
| 0   | 1   | 0              |
| 1   | 0   | 1              |
| 1   | 1   | ? (**RANDOM**) |

##### D
![[D-FF.png]]

| D   | Q(t+1) |
| --- | ------ |
| 0   | 0      |
| 1   | 1      |

##### JK
![[JK-FF.png]]

| J   | K   | Q(t+1) |
| --- | --- | ------ |
| 0   | 0   | Q(t)   |
| 0   | 1   | 0      |
| 1   | 0   | 1      |
| 1   | 1   | Q'(t)  |

##### T
![[T-FF.png]]

| T   | Q(t+1) |
| --- | ------ |
| 0   | Q(t)   |
| 1   | Q'(t)  |

Το $Q(t)$ είναι η προηγούμενη τιμή που είχε για έξοδο το flip flop.

---
### Θετικα ακροπυροδοτούμενο Clock
![[Positive-Clock.png]]

### Αρνητικά ακροπυροδοτούμενο Clock
![[Negative-Clock.png]]


---
##  DM7474 

Dual Positive-Edge triggered D-Type Flip-Flop with preset clear and complementary outputs.
 
![[DM7474-Diagram.png]]

![[DM7474-FunctionTable.png]]

---
## Πίνακες Διέγερσης Flip-Flop


## RS

| $Q(t)$ | $Q(t+1)$ | $S$ | $R$ |
| ------ | -------- | --- | --- |
| 0      | 0        | 0   | X   |
| 0      | 1        | 1   | 0   |
| 1      | 0        | 0   | 1   |
| 1      | 1        | X   | 0   |

### JK
| $Q(t)$ | $Q(t+1)$ | $J$ | $K$ |
| ------ | -------- | --- | --- |
| 0      | 0        | 0   | X   |
| 0      | 1        | 1   | X   |
| 1      | 0        | X   | 1   |
| 1      | 1        | X   | 0   |

### D
| $Q(t)$ | $Q(t+1)$ | $D$ |
| ------ | -------- | --- |
| 0      | 0        | 0   |
| 0      | 1        | 1   |
| 1      | 0        | 0   |
| 1      | 1        | 1   |