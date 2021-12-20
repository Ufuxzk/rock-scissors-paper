import random 
from random import choice


def main():
    print("""
            TAŞ-KAĞIT-MAKAS OYUNU ----------  Python ile proje geliştiriyorum #1- Ufuk Eren İnce
            Oyunun kuralları:
            1-Taş, makası yener
            2-kağıt, taşı yener
            3-makas, kağıtı yener
            4-3 Puan olan oyunu kazanır (Rakip: Bilgisayar)

    """
    )
    gameRuleFınısh = int(input('Oyunun kaçta biteceğini belirt:(1,10 arası sayı gir\n..'))
    gameMaterial = ['taş','kağıt','makas']
    pointPc = 0 # Points Pc
    pointPlayer = 0 # Points Player
    
    while True:
        if pointPlayer == gameRuleFınısh:
            print(f"Oyunu Sen kazandın!\nPuanın: {pointPlayer}\nBilgisayarın Puanı: {pointPc}")
            return False
        elif pointPc == gameRuleFınısh:
            print(f"Oyunu Kaybettin!\nPuanın: {pointPlayer}\nBilgisayarın Puanı: {pointPc}")
            return False
        else:
            #oyuncu ve bilgisayarın seçimlerinin karşılaştırılıp kazanana puan eklenilen bölüm.#
            playerCHOOSE = str(input('taş,kağıt,makas?:\n'))
            choosePC = random.choice(gameMaterial)
            if choosePC == playerCHOOSE:
                print(f'Bilgisayar:{choosePC}\nSen: {playerCHOOSE}\nBerabere!')
            elif choosePC == gameMaterial[0] and playerCHOOSE == 'kağıt':
                print(f'Bilgisayar:{choosePC}\nSen: {playerCHOOSE}\nKazanan Sensin!')
                pointPlayer += 1
            elif choosePC == gameMaterial[1] and playerCHOOSE == 'makas':
                print(f'Bilgisayar:{choosePC}\nSen: {playerCHOOSE}\nKazanan Sensin!')
                pointPlayer += 1
            elif choosePC == gameMaterial[2] and playerCHOOSE == 'taş':
                print(f'Bilgisayar:{choosePC}\nSen: {playerCHOOSE}\nKazanan Sensin!')
                pointPlayer += 1
            elif choosePC == gameMaterial[0] and playerCHOOSE == 'makas':
                print(f'Bilgisayar:{choosePC}\nSen: {playerCHOOSE}\nKazanan Bilgisayar!')
                pointPc += 1
            elif choosePC == gameMaterial[1] and playerCHOOSE == 'taş':
                print(f'Bilgisayar:{choosePC}\nSen: {playerCHOOSE}\nKazanan Bilgisayar!')
                pointPc += 1
            elif choosePC == gameMaterial[2] and playerCHOOSE == 'kağıt':
                print(f'Bilgisayar:{choosePC}\nSen: {playerCHOOSE}\nKazanan Bilgisayar!')
                pointPc += 1
    
if __name__ == '__main__':
    main()