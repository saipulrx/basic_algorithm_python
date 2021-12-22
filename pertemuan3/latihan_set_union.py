grup_smp = {
    'andi','budi','dewi','ferdi'
}

grup_sma = {
    'dena', 'gunawan','ferdi','andi'
}

#union
print(grup_smp | grup_sma)
print(grup_smp.union(grup_sma))

#intersection
print(grup_smp & grup_sma)
print(grup_smp.intersection(grup_sma))

#difference
print(grup_smp - grup_sma)
print(grup_smp.difference(grup_sma))

#symmetric_difference
print(grup_smp.symmetric_difference(grup_sma))