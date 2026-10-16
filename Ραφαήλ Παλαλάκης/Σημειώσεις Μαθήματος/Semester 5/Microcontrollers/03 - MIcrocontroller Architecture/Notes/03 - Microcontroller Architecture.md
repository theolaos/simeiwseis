___
### PIC18F4550 Architecture

- Data Memory bus is **8-Bit**.
- Program Memory bus is **16-Bit**.
- Instructions are **ALWAYS** **16-Bit** length.


___
### CPU connection to Data & Program Memory

![[mC-03-01.png]]

Program Memory :
- Each Instrucion is **16-Bit** or **2-Byte** long.
- Data Memory Bus is **ONE WAY** from Memory to CPU
- Address bus is **ONE WAY** from CPU to Memory
- Control Bus is **BOTH WAYS**

Data Memory :
- In each memory slot, the data saved is **8-Bit** long,
- Data Memory Bus is **BOTH WAYS**
- Address bus is **ONE WAY** from CPU to Memory
- Control Bus is **BOTH WAYS**


___
### Memory Addresses

For memory addresses we use the **Base16 (h)** system
Example : (7FF)h which is the 2047th slot


___
### How To Read Data Map

![[mC-03-02.png]]

In the left, the Bank is the first value of the address

```

Bank 0 : 00h -> 000h
Bank 1 : 00h -> 100h
Bank 2 : 00h -> 200h
...
Bank 14 : 00h -> F50h
Bank 15 : 00h -> F60h
```

**WARNING** : Slots from **F60(h)** -> **FF0(h)** are also used for **Special Function Registers (SFR)**.


We can calculate memory space in this way
$2^{10} = 1024 = 1K$
$2^{20} = 1K * 1K = 1M$


___
### Program Memory

![[mC-03-03.png]]

Notes :
- The Values at the Address Bus are given by the **Program Counter**
- The **Program Counter** is a register inside the CPU. It sends the **memory address** of the next command. It helps execute an instruction while fetching the next instruction at the same time for minimal downtime.
- The Address Bus has 21 lanes. I t could access $2 * 2^{10} * 2^{10} = 2^{21} = 2M$ data slots
- The memory though, has address range from **(0000)h** to **(7FFF)h**, so $2^{15} = 32K$


___
### Moving Data via Data Memory

The insertion or fetch of data in the data memory is done via the **Work Register** which is part of the **Special Functions Register**. The **SFR** has the same length as the memory address (in this case it's **8Bit**).


___
### Reset Vector

A Hardwired memory slot **(000)h** that the micro-controller always fetches its first data from, and we can use it to add an instruction to redirect the CPU to fetch data from.

We can utilize it with :

``` ASSEMBLY
ORG 0x000
```

In that way we can set the origin to the reset vector (0x000 = 000h)


___
### Define Memory Access

The PIC datasheet has clarification for each memory (**Program Data** or **Memory Data**) by using two values (for example **0x** is the default **Memory Data**).


___
