___

### **Declare a string**

How to declare a string in Java :

``` java
String s = "Content Goes Here";
```

---

### **Convert a string as uppercase**

How to set every character as an Uppercase :

```java
s = s.toUpperCase();
```

Instead if we just want to return it we can use :

```java
s.toUpperCase();
```

And use it (for example) as :

```java
System.out.println(s.toUpperCase()); // Console Log : "CONTENT GOES HERE"
```

----

### **Compare a string with another string**

And to compare two strings we use :

```java
s.equals(anotherVariable);
```

The method:

$$.equals()$$ 

can compare a string variable with another string variable inside the method parameters and return a **boolean** back (that can be set in a boolean variable).
 
----

### **String methods**

- Returns the amount of characters inside a string with :

```java
int length(s);
```


- Returns the character in a specific index inside a string with :

```java
char charAt(int);
```


- Returns (as a boolean) if a string is empty with :

```java
boolean isEmpty();
```


- Returns (as a boolean) if the string inside the parameters is the same with the one we are calling the method with :

```java
boolean equals(s);

boolean equalsIgnoreCase(s); //if we want to ignore uppercase/lowercase
```


- Compares two strings and return < 0 if it's smaller, 0 if it's equal length, and >0 if it's bigger :

```java
int compareTo(s);
```


- Returns the string we enter as all uppecase characters with :

```java
String toUppercase();
```


- Returns the string we enter as all lowercase characters with :

```java
String toLowercase();
```


- Returns adds the string we send from the parameters to the String we are calling the method with :

```java
String concat(s);
```


- Returns the index of a specific character inside a string or return -1 if it's not found :

```java
int indexOf(s);
```


- Returns the a boolean value if the specific set of characters exists inside the string :

```java
bolean contains(s);
```


- Returns the String we call the method with, with the first character it encounters (first parameter) with the character we set (second parameter) with :

```java
String replace(char, char);
```


- Returns the string without the spaces with :

```java
String trim();
```


- Returns the string from one index (first parameter) to the second (second parameter) with :
```java
String substring(int, int);
```


- Returns the String with the first set of characters replaced (first parameter) with the set of characters (second parameter) with :

```java
String replaceFirst(String, String); // does it only the first time it encounters

String replaceAll(String, String); //Does it for all the encounters
```


----

