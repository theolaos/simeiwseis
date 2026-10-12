___
**Inheritance** is the process of creating a new Class based on an already existing Class while also inheriting any **properties** and **methods**.

With **inheritance** we can have a **class hierarchy system**.

That makes reusing the code much easier.

**Subclasses** can **specialize** the **behaviour** of other **superclasses**.

We can use both **extends** & **implements**.

___
### **Extends**

By using **extends**, a class can **inherit** another class

A class can only extend only one **SuperClass**

A **subclass** that extends a **superclass** cannot override all of its methods


**Example below**
```java
class One()
{
	public void methodOne()
	{
	
	}
}

class Two extends One()
{
	public static void Main(String args[])
	{
		Two Example = new Two()
		
		t.methodOne(); // Calls the methodOne() of the class above
	}
}

```


---
### **Implements**

By using **implements** a class can implement an interface (or any number of interfaces at the same time).

An interface can **extend** other interfaces but **cannot** **implement** them


**Example below** : Use of **implements**
```java
interface One()
{
	public void methodOne();
}


interface Two()
{
	public void methodTwo();
}


class Three implemenets One, Two
{
	public void methodOne()
	{
		// here is an implementation of the method
	}
	
	
	public void methodTwo()
	{
		// here is an implementation of the method
	}
}
```


**Example Below :** interface that can extend other interfaces
```java
interface One()
{
	void methodOne();
}


interface Two()
{
	void methodTwo();
}


interface Three extends One, Two()
{

}
```