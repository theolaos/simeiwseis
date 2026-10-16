___
### The 3 Categories Of Instructions

- **Byte-Oriented File Register Operations** (18 Instructions)
- **Bit-Oriented File Register Operations** (4 Instructions)
- **Literal and Control Operations** (13 Instructions)
  
This brings the Instruction Set to **35 Instructions**. This is a **medium sized** instruction set that is used by PICs in the **16Family**.

___
### Byte-Oriented File Register Operations
___

1. **ADDWF f,d** (Add ``W`` and ``f``)
   Adds the value in the **Working Register** to the value that exists in the ``f`` memory address, and stores the result :
   
   - In the **Working Register** if ``d`` is **0**.
   - In the ``f`` if ``d`` is **1**.
   
   **Example** ~ Assembly : 
   
   ```assembly
   ADDWF CNT, 1
   ```
   
   **Example** ~ C : 
   
   ```C
   if (d == 0)
   {
      W = CNT + W;
   }
   else // In The Case Above, This Is What Will Happen Since d = 1
   {
      CNT = CNT + W;
   }
   ```
   
   This adds the value in the **Working Register** to the value that ``CNT`` holds and then saves it.
---
   
2. **ANDWF f,d** (AND ``W`` with ``f``)
   Performs a logical **AND** between the value in the **Working Register** and ``f``. Usually used for bitmasking. It stores the result :
   
   - In the **Working Register** if ``d`` is **0**.
   - In the ``f`` if ``d`` is **1**.
   
   **Example** ~ Assembly : 
   
   ```assembly
   ANDWF STATUS, 0
   ```
   
   **Example** ~ C : 
   
   ```C
   if (d == 0) // In The Case Above, This Is What Will Happen Since d = 0
   {
      W = W & STATUS;
   }
   else
   {
	   STATUS = W & STATUS;
   }
   ```
   
   This Performs an **AND** operation with the value in **STATUS** and the value in the **Working Register**, calculates the answer and stores it in the **STATUS** value memory address.
   
___

3. **CLRF f** (Clear ``f``)
   Sets the **file register** ``f`` to **zero** ($0$).
   
   **Example** ~ Assembly : 
   
   ```assembly
   CLRF PORTA
   ```
   
   **Example** ~ C : 
   
   ```C
   PORTA = 0;
   ```
   
   This clears the value at **PORT A** in the memory.
   
___

4. **CLRW** (Clear ``W``)
   Sets **Working Register** to **zero** ($0$).
   
   **Example** ~ Assembly : 
   
   ```assembly
   CLRW
   ```
   
   **Example** ~ C : 
   
   ```C
   W = 0; // The 'W' represents the value stored inside the Working Register
   ```
   
   This resets the **Working Register** and does not require any operand.
   
___
   
5. **COMF f,d** (Complement ``f``)
   Inverts every bit in ``f`` (0 becomes 1 & 1 Becomes 0). It stores the result :
   
   - In the **Working Register** if ``d`` is **0**.
   - In the ``f`` if ``d`` is **1**.
   
   **Example** ~ Assembly : 
   
   ```assembly
   COMF REG1, 0
   ```
   
   **Example** ~ C : 
   
```C
if (d == 0) // In The Case Above, This Is What Will Happen Since d = 0
{
	REG1 = REG1 * (-1);
}
else
{
	W = REG * (-1);
}
```
   
   This inverts the ``REG1`` value and stores the result.
   
___
   
6. **DECF f,d** (Decrement ``f``)
   Subtracts 1 from the value in ``f``. It stores the result :
   
   - In the **Working Register** if ``d`` is **0**.
   - In the ``f`` if ``d`` is **1**.
   
   **Example** ~ Assembly : 

   ```assembly
   DECF CNT, 1
   ```
   
   **Example** ~ C
   
   ```C
   if (d == 0)
   {
	   CNT = CNT - 1;
   }
   else // In The Case Above, This Is What Will Happen Since d = 1
   {
	   W = CNT - 1;
   }
   ```
   
   This decrements ``f`` by 1 and stores the result.
   
___

7. **DECFSZ f,d** (Decrement ``f`` and skip if it's zero)
   Subtracts 1 from the value in ``f`` and skips to the next instruction **if the result is zero**. It stores the result : 
   
   - In the **Working Register** if ``d`` is **0**.
   - In the ``f`` if ``d`` is **1**.
   
   **Example** ~ Assembly :
   
   ```assembly
   DECFSZ CNT, 1
   ```
   
   **Example** ~ C :
   
   ```C
   if (d == 0)
   {
		while (CNT != 0)
		{
			CNT = CNT - 1;
		}
		
		// Next are the instructions. Works like the ``LOOP GOTO``
   }
   else // In The Case Above, This Is What Will Happen Since d = 1
   {
		while (W != 0)
		{
			W = CNT - 1;
		}
		
		// Next are the instructions. Works like the ``LOOP GOTO``
   }
   ```
   
   This decrements ``f`` by 1 and stores the result. If ``f`` becomes zero it skips the `LOOP GOTO` (that is followed after the ``DECFSZ``) and goes to the next instruction.

--- 

8. **INCF f,d** (Increment ``f``)
   Adds 1 to the value in ``f``. It stores the result :
   
   - In the **Working Register** if ``d`` is **0**.
   - In the ``f`` if ``d`` is **1**.
   
   **Example** ~ Assembly
   
   ```assembly
   INCF CNT, 1
   ```
   
   **Example** ~ C
   
   ```C
   if (d == 0)
   {
	   CNT = CNT + 1;
   }
   else // In The Case Above, This Is What Will Happen Since d = 1
   {
	   W = CNT + 1;
   }
   ```
   
   This decrements ``f`` by 1 and stores the result.
   
___

9. **INCFSZ f,d** (Increment ``f`` and skip if it's zero)
   Adds 1 to the value in ``f`` and skips to the next instruction **if the result is zero**. It stores the result : 
   
   - In the **Working Register** if ``d`` is **0**.
   - In the ``f`` if ``d`` is **1**.
   
   **Example** ~ Assembly :
   
   ```assembly
   INCFSZ CNT, 1
   ```
   
   **Example** ~ C :
   
   ```C
   if (d == 0)
   {
		while (CNT != 0)
		{
			CNT = CNT + 1;
		}
		
		// Next are the instructions. Works like the ``LOOP GOTO``
   }
   else // In The Case Above, This Is What Will Happen Since d = 1
   {
		while (W != 0)
		{
			W = CNT + 1;
		}
		
		// Next are the instructions. Works like the ``LOOP GOTO``
   }
   ```
   
   This increases ``f`` by 1 and stores the result. If ``f`` becomes zero it skips the `LOOP GOTO` (that is followed after the ``INCFSZ``) and goes to the next instruction.

___

  10. **IORWF f,d** (Inclusive OR ``W`` with ``f``)
   Performs a logical **OR** between the value in the **Working Register** and ``f``. It is used for settings specific bits. It stores the result : 
   
   - In the **Working Register** if ``d`` is **0**.
   - In the ``f`` if ``d`` is **1**.
   
	   **Example** ~ Assembly :
	   
	   ```assembly
	   IORWF RESULT, 0
	   ```
	   
	   **Example** ~ C :
	   
	   ```C
	   if (d == 0) // In The Case Above, This Is What Will Happen Since d = 1
	   {
			RESULT = RESULT || W
	   }
	   else
	   {
			W = RESULT || W
	   }
	   ```
	   
	   This performs the logical operator **OR** between the value inside the **Working Register** and the value that ``f`` holds and stores the value.
	   
___

11. **MOVF f,d** (Move ``f``)
   Copies the value stored in the **Working Register** to ``f``. Often used to check if a register is zero (which sets the Z flag). It stores the result : 
   
   - In the **Working Register** if ``d`` is **0**.
   - In the ``f`` is ``d`` is **1**.
   
   **Example** ~ Assembly :
   
   ```assembly
   MOVWF CNT, 1
   ```
   
   **Example** ~ C :
   
   ```C
   if (d == 0)
   {
		W = CNT;
   }
   else // In The Case Above, This Is What Will Happen Since d = 1
   {
		CNT = CNT;
   }
   ```
   
   This moves/copies the value of ``CNT`` the the desired place but also updates the Z flag to see if it's zero.
   
___

12. **MOVWF f** (Move ``W`` to ``f``)
   Copies the value from the **Working Register** to ``f``.
   
   **Example** ~ Assembly :
   
   ```assembly
   MOVWF PORTB
   ```
   
   **Example** ~ C :
   
   ```C
   PORT = W;
   ```
   
   This copies the value from the **Working Register** to the ``PORTB``.

___

13. **NOP** (No Operation)
   Does literally nothing. It occupies one instruction cycle.
   
   **Example** ~ Assembly
   
   ```assembly
   NOP
   ```

___
