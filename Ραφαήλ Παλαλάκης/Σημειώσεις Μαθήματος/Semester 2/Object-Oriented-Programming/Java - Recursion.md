___

### **What is recursion**

Recursion is the process where a method calls itself. Mandatory part of it, is a statement that ends the recursion.

Every time a recursive method is being called, new local variables and parameters are being created.

Recursion algorithms are best used in **divide & conquer** algorithms.


---

### **(Example) Factorial Algorithm** (With Recursion)

```java
public static int Factorial(int num)
{
	if (num == 0)
	{
		return 1;
	}
	else
	{
		return num * Factorial(num - 1);
	}
}
```


### **(Example) Factorial Algorithm** (Without Recursion)

```java
public static int Factorial(int n)
{
	int result = 1;
	
	for (int i = 2; i <= n; i++)
	{
		result = result * i;
	}
	
	return result;
}
```


----

### **(Example) Fibonacci Algorithm**

```java
public static int Fibonacci(int num)
{
	if (num == 1 || num == 2)
	{
		return 1;
	}
	else
	{
		return Fibonacci (num-1) + Fibonacci(num-2);
	}
}
```


---

### **(Example) Calculate power on a variable**

```java
int power(int a, int n)
{
	int p;
	
	if (n == 0)
	{
		p = 1;
	}
	else
	{
		p = a * power(a, n-1);
	}
	
	return p;
}
```


---