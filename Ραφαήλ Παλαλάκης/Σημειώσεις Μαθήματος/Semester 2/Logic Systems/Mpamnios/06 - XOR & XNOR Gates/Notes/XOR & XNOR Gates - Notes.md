___
## The XOR Logic Gate

Circuit Symbol :

![[XOR-LogicGate.png]]

Algebra Boole Fox **XOR** 
$$
X = A ⊕ B=\overline{A}B + A\overline{B}
$$


XOR Value Table (**A**,**B** are the **inputs**, **X** is the **output**)

| A   | B   | X   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 1   | 0   | 1   |
| 0   | 1   | 1   |
| 0   | 0   | 0   |

Other Ways We Can Form A **XOR** Function :

With **NOT**, **AND** & **OR** Logic Gates :
![[XOR-Circuit1.png]]

With **AND**, **NAND** & **OR** Logic Gates :
![[XOR-Circuit2.png]]



---
## The XNOR Logic Gate

Circuit Symbol :

![[XNOR-LogicGate.png]]

Algebra Boole For **XNOR**
$$
X = \overline{A⊕B} = AB + \overline{A}\overline{B}
$$

XNOR Value Table (**A**,**B** are the **inputs**, **X** is the **output**)

| A   | B   | X   |
| --- | --- | --- |
| 0   | 0   | 1   |
| 1   | 0   | 0   |
| 0   | 1   | 0   |
| 0   | 0   | 1   |

Another Way We Can For a **XNOR** Function :

With **NOT**, **AND** & **OR** Logic Gates :
![[XNOR-Circuit1.png]]



---
## Equality Generator/Controller

We have **ODD** or **EVEN** circuits. They add an extra bit to the data packet.

- For an **ODD** circuit, the extra validation bit should make the result of the bits to **5 ODD**
- For an **EVEN** circuit, the extra validation bit should make the result of the bits to **5 EVEN**

![[GeneratorDiagram.png]]
(The above method uses an **ODD** result, and can only detect **ONE** error)


Equality Generator (**ODD** or **EVEN**)
![[Pasted image 20260330095924.png]]



---
## Parallel Binary Compare


The Generator In Details (with Logic Gates)
![[GeneratorCircuit.png]]



---
## Controlled Inverter

![[Pasted image 20260330100733.png]]