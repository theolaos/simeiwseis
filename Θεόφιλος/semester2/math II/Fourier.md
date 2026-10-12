Ταυτότητα **Euler**:

$$
sin(\omega) = \frac{e^{i\omega} - e^{-i\omega}}{2i} \iff 2 \ i\ sin(\omega) = e^{i\omega} - e^{-i\omega}
$$
Το $\omega$ μπορεί να είναι "οτιδήποτε".

Στον μετασχ. Fourier ισχύουν οι παρακάτω ιδιότητες:

### Γραμμικότητα:
$$ a \cdot f(t) + b \cdot g(t) \to a \cdot \hat{F}(\omega) + b \cdot \hat{G}(\omega)$$
### Μετατόπιση (στον χρόνο):
$$F\{f(t - t_0)\} \to \hat{F}(\omega) \cdot e^{-i \omega t_0}$$
$$F^{-1}\{ \hat{F}(\omega - \omega_0)\} \to f(t) \cdot e^{-i \omega_0 t}$$
Ισχύουν και οι αντίστροφες πράξεις. Παράδειγμα:
$$F\{f(t) \cdot e^{-i \omega_0 t}\} \to \hat{F}(\omega - \omega_0)$$

### Αλλαγή κλίμακας χρόνου/συχνότητας:

$$f(a \cdot t) \to \frac{1}{|a|} \hat{F}\left(\frac{\omega}{a}\right)$$
### Συνέλιξη:
$$f(t) * g(t) \longrightarrow \hat{F}(\omega) \cdot \hat{G}(\omega)$$

### Παραγώγιση:
$$\frac{df(t)}{dt} \to i\omega \cdot \hat{F}(\omega)$$
