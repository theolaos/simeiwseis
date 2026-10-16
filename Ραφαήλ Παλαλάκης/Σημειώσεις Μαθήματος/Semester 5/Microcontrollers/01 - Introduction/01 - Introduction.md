___
### Τυπικό υπολογιστικό σύστημα

- **Microprocessor** -> Central Processing Unit inside a chip 
- **Microcontroller** -> CPU, Memory, IO etc
- **Output** -> Information to CPU, Analog to Digital Signals (0V and 5V signals)
- **Input** -> Signals from CPU to physical devices (displays, relays, speakers etc)
- **Memory** -> Types of memory : **RAM/ROM(EPROM, EEPROM)**
- **Clock** -> Usually uses a Crystal


___
### Microcontroller Programming Languages

C Language : 
- Εύκολο να γράψεις προγράμματα
- Δεν είναι απαραίτητη η γνώση της δομής του μΕ

C Compile :
- Είναι ένα πρόγραμμα με το οποίο γίνεται μετάφραση απο γλώσσα C σε Machine Code

Assembly Language :
 - Πιο δύσκολη γλώσσα
 - Είναι απαραίτητη κάποια γνώση της δομής του μικροελεγκτή

Assembler :
- Είναι ένα πρόγραμμα με το οποίο γίνεται μετάφραση απο Assembly σε Machine Code


___
### Κατάταξη Microcontrollers αναλογα με την αρχιτεκτονική τους

- Harvard Architecture (Seperate Address Bus and Data Bus for Program and Data Memory as seperate memory spaces)
- Von Neumann Architecture (Same Address and Data bus for one unified memory that holds both program code and data)


___
### Program Memory vs Data Memory

Program Memory :
- Holds the data for all programs running on this system

Data Memory :
- Holds the data that all programs generate/hold on this system


___
### Address Bus vs Data Bus

Address Bus :
- One way (**CPU** to **Memory** or **CPU** to **IO**). It only serves as a way to transfer addresses to help the counterparts communicate through the data busses.

Data Bus :
- Both ways. It servers as a physical connection to transfer data from one counterpart to another.


---
