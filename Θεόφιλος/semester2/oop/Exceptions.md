
Checked -  ΠΡΕΠΕΙ διαχειρίζομαι τις εξαιρέσεις. Δηλαδή πρέπει να διαχειριστώ 
Το `Exception` πρέπει να το διαχειριστής άμα δεν το γράψεις στο `throws`.

Unchecked - ΑΜΑ ΘΕΛΩ διαχειρίζομαι τις εξαιρέσεις. Δηλαδή πρέπει να διαχειριστώ 
Το `RuntimeException` δεν χρειαζεται να διαχειριστής. Αλλα λειτουργεί σαν το `throws`.
## Δημιουργία κλάσεων Εξαιρέσεων.
```java
class AgeException extends Exception {
	public AgeException(String meessage){
		super(message);
	}
}
```
Η προτεινόμενη υλοποίηση δημιουργίας κλάσεων Εξαιρέσεων.
Δηλαδή πρέπει να καλώ τον δομητή της Υπερκλάσεις.

```java
class MyExcept extends RuntimeException {
	private String message;
	public MyExcept(String meessage){
		this.message = message;
	}
	public String getMessage(){
		return message;
	}
}
```
Η διαφορά της `RuntimeException` με την `Exception` είναι πως στην δεύτερη περίπτωση

## Διαχείριση Εξαιρέσεων.

```java
class Main {
	public static void main(String[] args) {
		try{
			// Κώδικας που δεν είμαι σίγουρος οτι θα τρέξει σωστά
		} catch (<Exception Class> <name of variable that will get the Exception data>) {
			// διαχείρηση της εξαίρεσης που μόλις δημιουργήθηκε
		} catch (<...> <...>) {} // σε περίπτωση που έχουμε και άλλες εξαιρέσης που θέλουμε να διαχειρηστούμε τότε μπορούμε να το κάνουμε με επιπλέον `catch blocks`
	}
}
```




## Ερώτηση που πρέπει να κάνω στον Αδαμίδη.

Πότε πρέπει να χρησιμοποιώ το `throws Exception[, Exception[, ...]]`

Από το εργαστήριο άκουσα πως πρέπει να το χρησιμοποιώ συνέχεια, ανεκαθέν για το αμα χειρίζομαι την εξαίρεση.

Έπειτα πρέπει να ρωτήσω και την Ασδρε, με την απάντηση του Αδαμίδη.
