def persentase(total,jumlah):
    if(total >= 0 and total <= jumlah):
        return total / jumlah * 100
    
    return False

print(persentase(30,60))

print(persentase(60,30))
