grup_smp = {
  'andi', 'budi', 'ratna', 'sari'
}

grup_sma = {
  'putri', 'ratna', 'andi', 'agus'
}

#union
print(grup_smp | grup_sma)
print(grup_smp.union(grup_sma))

#intersect
print(grup_smp & grup_sma)
print(grup_smp.intersection(grup_sma))

#difference
print(grup_smp - grup_sma)
print(grup_smp.difference(grup_sma))

#symmetric difference
print(grup_smp.symmetric_difference(grup_sma))


