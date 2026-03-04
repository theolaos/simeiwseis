Κατα παράγοντες:
$$\int f(x)g(x)dx = \int F'(x)g(x) = F(x)g(x) - \int F(x)g'(x)dx $$

Με αντικατάσταση:
Έστω $f(x) = u$ τότε $\frac{du}{dx}=u' \Leftrightarrow dx=\frac{du}{u'}$

Και απλά αντικατηστώ στην συνέχεια στο ολοκλήρωμα.

Κάποιες φορές στα κλάσματα μπορώ να αντικαταστήσω με σκοπό να βγάλω την μεταβλητή στον αριθμητή ή και στον παρανομαστή.

π.χ.

$$\int\frac{x}{\sqrt{1-x^2}}dx = $$
Έστω $u=1-x^2$
$dx=-\frac{du}{2x}$
άρα 
$$\int\frac{x}{\sqrt{ u }}\cdot\frac{du}{-2x} = \int\frac{1}{\sqrt{ u }}\cdot\frac{du}{-2} = -\int\frac{du}{2\sqrt{u }}$$
Και φυσικά η λύση θα είναι: $\sqrt{ u } +C$

Επίσης μην ξεχνάμε για τριγωνομετρικά ολοκληρώματα έχουμε τους παρακάτω τύπους:

## ~Τριγωνομετρικά
Σε περίπτωση που έχουμε μονές δυνάμεις π.χ.:

$$\int f(\sin x, \cos x)dx$$
τότε μπορούμε να εφαρμόσουμε την παρακάτω αντικατάσταση:

$$u = \tan\frac{x}{2}$$
$$dx = \frac{2du}{1 + u^2}$$
$$\sin x = \frac{2u}{1+u^2}, \cos x = \frac{{1-u^2}}{1+u^2}, \tan x = \frac{2u}{x-u^2}$$
Σε περίπτωση που έχεις δύναμη εις την δύο, τότε:
$$\int f(\sin^2x, \cos^2x)dx$$τότε κάνεις την παρακάτω αντικατάσταση:
$$u = \tan x$$
$$dx = \frac{du}{1+u^2}$$
$$\sin x = \frac{u^2}{1+u^2}, \cos x = \frac{1}{1+u^2}$$

### Ταυτότητες

Τριγωνομετρικές ταυτότητες:
$$\sin^2x = \frac{1}{2}(1-\cos 2x)$$
$$\cos^2x = \frac{1}{2}(1+\cos 2x)$$
$$\sin x\cos y = \frac{1}{2}(\sin (x-y) - \sin(x+y))$$$$\cos x\cos y = \frac{1}{2}(\cos (x-y) + \cos(x+y))$$
$$\sin x\sin y = \frac{1}{2}(\cos (x-y) - \cos(x+y))$$
$$\cos(x+y) = \cos x\cos y - \sin x\sin y$$
$$\sin(x+y) = \sin x\cos y + \cos x\sin y$$


Κάποια εξτρά χρήσιμα βασικά αόριστα ολοκληρώματα, πέρα από γνωστά είναι:

$$\int a^xdx = \frac{a^x}{\ln a}+C$$
$$\int\frac{1}{\cos^2x}dx=\tan x + C$$
$$\int \frac{1}{\sqrt{ 1-x^2 }} = \arcsin x+C$$
$$\int \frac{1}{1+x^2} = \arctan x+C$$
