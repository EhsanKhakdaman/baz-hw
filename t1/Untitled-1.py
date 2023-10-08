pool = int(input())
if pool < 1000000000 :
    print('moaaf ! ')
elif pool >= 1000000000 and pool <= 10000000000 :
    maliyat = int (pool * 0.01)
    print(maliyat)      
elif pool > 10000000000:
    maliyat = int (pool * 0.15)
    print(maliyat)