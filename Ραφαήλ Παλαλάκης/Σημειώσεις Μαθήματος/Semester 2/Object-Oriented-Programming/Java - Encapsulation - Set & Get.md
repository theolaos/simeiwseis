---

---
___
The ability of a class to **hide** it's functions and properties.

All **properties**, **parameters** and **fields** are **private** and can be accessed with the use of **public methods**.

Access to that data can be only made with a specific way, set-up by the developer.

That way, we can modify the code from a class without changing any code for any of the users of that class. That way we can have better **security**, **maintenance** and **scaling**.


---
## How To Use Set & Get

Since all **private variables** can only be accessed within the same class, we need to have a way to access them.

That's where the **SET** and **GET** methods come in :

- **GET** : Returns the value of the variable (ExampleName)
- **SET** : Takes a Parameter (ExampleNameParameter) and sets it to the (ExampleName) variable. We use the instruction "this" to refer to the current object.


Example
```java
public class Example
{
	private String TestString;
	
	
	// Getter - Fetch This String
	public String getTestString()
	{
		return TestString;
	}
	
	
	// Setter - Set This Variable
	public void setTestString(String newTestString)
	{
		this.TestString = newTestString;
	}
}
```