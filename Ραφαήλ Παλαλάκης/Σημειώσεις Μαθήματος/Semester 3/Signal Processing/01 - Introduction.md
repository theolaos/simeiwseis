___
#### Signal Categories 

- Continuous Time & Length SIgnals (example : temperature)
- Non-Continuous Time & Length SIgnals (example : digital sound)
- Non-Continuous Time & Continuous Length Signals (example : stock market)
- Continuous Time & Non-Continuous Length Signals (example : Goal at a football match)

| **Signal**          | Time           | Length         |
| ------------------- | -------------- | -------------- |
| Non-Continuous Time | Non-Continuous | Continuous     |
|                     | Non-Continuous | Non-Continuous |
| Continuous TIme     | Continuous     | Continuous     |
|                     | Continuous     | Non-Continuous |

___
#### Continuous Time Signal

The variables has continuous float values. We mark it with $x(t)$.

___
#### Non-Continuous Time Signal

The variables has non continuous integer values. We mark it with $x(n)$.

___
#### Multidimentional/Multichannel Signals

**Multidimentional** : Function of two or more variables (for example : digital video signal)

**Multichannel** : When the signal requires two or more functions/vectors (for example an rgb display with Red, Green, Blue).


___
#### Real-Complex Continuous Time Signal

- Continuous TIme Signal is a function consisting of the independend time variable and the dependend length variable $x(t)$.
- If length is a real variable, the signal is a **Real Continuous Time Signal**
- If length is a complex variable, the signal is a **Complex Continous TIme Signal**

___
### Limited Continuous Time Signal

- The values of this signal outside a specific time $[t_1, t_2]$ are all zero
- The signal that has at least one of two $t_1 \& t_2$ that is infinite, constists of an unlimited time signal

___
### Αιτιατό & Περιοδικο Σήμα

- **Αιτιατό** ειναι το σήμα που φερει μηδενικες τιμες στις αρνητικες χρονικες στιγμές.
- **Μη-Αιτιατό** ειναι το σήμα που φέρει μηδενικές τιμές σε θετικές χρονικές στιγμές
- **Περιοδικό** ειναι το σήμα που υπάρχει τουλάχιστον ενας θετικός αριθμός $Τ$ για τον οποιο ισχύει $x(t) = x(x+T)$. Το $Τ$ ονομάζεται περίοδος του σήματος. Ο ελάχιστος αριθμός $Τ$ ονομάζεται θεμελιώδης περίοδος συνεχούς σήματος.

---
#### Symetry Of Continuous Time Signal

- A Continuous Time Signal is **even** when $x(-t) = x(t)$ for every $t$
- A Continuous Time Signal is **odd** when $x(-t) = -x(t)$ for every $t$
- A Continuous Time Signal is **symetrical** when $x(-t) = x*(t)$
- A Continuous Time Complex Signal is **asymetrical** when $x(-t) = -x*(t)$

$x*(t)$ συζηγές

___
### Σημείο Δ (Dirac) Συνεχούς Χρόνου

- Το σήμα μοναδιαίου παλμού ή συνάρτηση δέλτα του Dirac $δ(t)$ ή κρουστική συν/ση ορίζεται απο την αποικόνιση
$$
\int_{-\infty}^{+\infty} f(t) * δ(t) dt = f(0)
$$

- Αν θεωρήσουμε $f(t) = 1$ τότε : 
$$
\int_{-\infty}^{+\infty} δ(t)dt = 1
$$

- Γενικός ορισμός συν/σης δέλτα :
$$
δ(t) = 0,t \ne 0
$$
$$
δ(t) = \infty,t = 0
$$

___
### Ιδιότητες Συν/σης Δέλτα Συνεχούς Χρόνου

- Χρονική Μετατόπιση
$$
\int_{-\infty}^{+\infty} f(t) * δ(t-t_0)dt = f(t_0)
$$

- Πολλαπλασιαστης στην συνάρτησης δέλτα
$$
\int_{-\infty}^{+\infty}f(t) * δ(α*t)*dt = \frac{1}{|a|}*f(0)
$$
$$
δ(α*t) = \frac{1}{|a|} * δ(t), α \ne 0
$$

- Η συν/ση δέλτα είναι άρτια
$$
δ(-t) = δ(t)
$$

___
#### Μοναδιαίο βηματικό σήμα συνεχούς χρόνου

Ορισμός
$$
u(t) = 1,t >= 0
$$
$$
u(t) = 0,t < 0
$$

Το βηματικό σήμα είναι ασυνεχές στη χρονική στιγμή $t=0$
Η μοναδιαία ώση είναι παράγωγος της βηματικής συν/σης $δ(t) = \frac{d * u(t)}{dt}$
