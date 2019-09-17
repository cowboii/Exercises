# Övning 1.41 - ☆☆ Leibnitz formel för π
# 
# Det går att visa att följande oändliga summation:
#
#
# LaTeX: \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} = \frac{\pi}{4} \quad 
# \Longleftrightarrow \quad \pi = 4 \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}
# 
#
# går mot π (dock konvergerar serien långsamt).
# Uppgiften går ut på att göra en implementation om beräknar seriens summa 
# (med hjälp av iteration) för att beräkna närmevärden till π. Eftersom det är 
# en oändlig serie, dvs. oändligt antal termer så är det inte rimligt att låta 
# datorn iterera i all oändlighet. Därmed  krävs det en modifiering av formeln 
# (en approximation):
#
# LaTeX: \pi \approx 4 \sum_{n=0}^k \frac{(-1)^n}{2n+1}
#
# Genom att öka värdet på k t.ex 100, 200, 300, . . . får du mer och mer 
# noggranna närmevärden. Öka k i ditt program till dess att du börjar känna 
# igen värdet på π.
# Tips: Tänk på att (−1)n = 1 då n är jämnt och (−1)n = −1 då n är udda om du 
# sätter ett tröskelvärde på storleken av termerna för att avbryta iterationen.
#
#
# Anmärkning: Datorn arbetar med flyttal som är en approximation av ett 
# decimaltal vilket leder till att beräkningar inte är exakta.

from decimal import Decimal, getcontext
from sys import argv


def lei(n):
    return Decimal(4) * sum([(Decimal(-1)**x)/(2*x+1) for x in range(0,n+1)])


if __name__ == "__main__":
    getcontext().prec = int(argv[2]) if len(argv) > 2 else 8
    print(lei(int(argv[1])))
