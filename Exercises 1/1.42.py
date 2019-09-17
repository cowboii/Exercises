# Övning 1.42 - ☆☆ Ramanujans formel för π
# Skriv en funktion LaTeX: \texttt{estimate_pi()} estimate_pi() för att beräkna
# och returnera ett närmevärde till \pi baserat på den formel som hittades 1910
# av den indiske matematikern Srinivasa Ramanujan. Denna formel konvergerar mot
# \pi mycket snabbare än Leibnitz formel. Använd en while-loop för att beräkna 
# summationstermer tills den sista termen är mindre än LaTeX: 10^{-15}.
#
# Formeln ges nedan:
# LaTeX: \hspace{2cm}\dfrac{1}{\pi} = \dfrac{2 \sqrt{2}}{9801}\displaystyle
# \sum_{k=0}^{\infty} \frac{(4k)!(1103 + 26390k)}{(k!)^4 \cdot 396^{4k}}

from math import pi, factorial
from decimal import Decimal as D
from sys import argv


def ramanujans(n):
    term = (D(2) * D(2).sqrt()) / D(9801)
    täljare = lambda k: D(factorial(4*k) * (1103 + (26390 * k)))
    nämnare = lambda k: D((factorial(k)**4) * (396**(4*k)))
    svar = (D(1) / D(pi))

    sparade = []

    while True:
        if sum(

    return term * sum([(täljare(k) / nämnare(k)) for k in range(0,n+1)])



if __name__ == "__main__":
    print(ramanujans(int(argv[1])))
    print(ans)

