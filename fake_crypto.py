import random, time, os, getpass
from art import tprint
code = getpass.getpass("Buat password: ")
os.system("clear")
koin_btc = 5
idr = 100000
usd = 100
dice = random.randint(1,2)
tprint("Investasi")
print("""
      pilih akses
      
1.Bitcoin
2.Money Digital 
      """)
option=int(input("Pilih motode: "))
if option==1:
    os.system("clear")
    tprint("INVESTASI_BTC")
    print("")
    print("Cara investasi btc (1/2/3/4/5 BTC), Anda hanya bisa memasukkan minimal 5 coin BTC")
    investasi = int(input(">: "))
    if investasi <=koin_btc:
        if dice==1:
            time.sleep(3)
            print("YOU WIN!")
            print("Coin BTC anda ",koin_btc+investasi*10)
            coin_btc = koin_btc+investasi*10
            cek = input("Witdrawh: ")
            if cek=="y":
                password = getpass.getpass()
                if password==code:
                    ambil = int(input("Ambil Berapa Coin?: "))
                    if ambil <=coin_btc:
                        print(f"Anda mengambil {ambil} Coin BTC Sisa Coin anda sekarang",koin_btc+investasi*10-ambil)
                        print("Jangan lupa kembali!")
                    else:
                        print("Maaf coin anda tidak cukup")
                else:
                    print("Maaf password anda salah!")
            else:
                print("Jangan lupa kembali!")
        else:
            time.sleep(3)
            print("YOU LOSE")
            print("Jangan lupa kembali lagi!")
    else:
        print("Maaf coin BTC anda tidak cukup")
elif option==2:
    print("""
1.USD
2.IDR
          """)
    pilih = int(input("Pilih opion: "))
    if pilih==1:
        os.system("clear")
        tprint("INVESTASI_USD")
        print("")
        print("Saldo anda 100 Dolar, Cara investasi USD(Dolar$), Masukkan nominal dolar minimal 100 dolar contoh(100)")
        investasi_usd = int(input(">: "))
        if investasi_usd <=usd:
            time.sleep(3)
            if dice==1:
                print("YOU WIN")
                print(f"Saldo anda Sekarang ",usd+investasi_usd*5,"Dolar")
                saldo_usd = usd+investasi_usd*5
                usd_ambil = input("Witdrawh?: ")
                if usd_ambil=="y":
                    password = getpass.getpass()
                    if password==code:
                        print("Ambil berapa?: ")
                        ambil_usd = int(input("$: "))
                        if ambil_usd <= saldo_usd:
                            print("Anda mengambil",ambil_usd,"saldo anda sekarang ",usd+investasi_usd*5-ambil_usd)
                            print("Jangan lupa kembali lagi!")
                        else:
                            print("Maaf saldo anda kurang")
                    else:
                        print("Maaf password anda salah")
                else:
                    print("Jangan lupa kembali!") 
            else:
                time.sleep(3)
                print("YOU LOSE")
                print("Saldo anda ",usd-investasi_usd)
                print("Jangan lupa kembali lagi!")
        else:
            print("Maaf saldo anda kurang!")
    elif pilih==2:
        os.system("clear")
        tprint("INVESTASI_IDR")
        print("")
        print("Saldo anda 100.000 ,Cara investasi IDR(Rupiah), Masukkan nominal rupiah contoh(1000/10000/100000), minimal 100000")
        investasi_idr = int(input(">: "))
        if investasi_idr <= idr:
            time.sleep(3)
            if dice==1:
                print("YOU WIN")
                print("Saldo anda sekarang",idr+investasi_idr*5)
                wit_idr = input("Witdrawh?: ")
                saldo_idr = idr+investasi_idr*5
                if wit_idr=="y":
                    password = getpass.getpass()
                    if password==code:
                        ambil_idr = int(input("$: "))
                        if ambil_idr <=saldo_idr:
                            print("Anda mengambil",ambil_idr,"saldo anda",idr+investasi_idr*5-ambil_idr)
                            print("Jangan lupa kembali lagi!")
                        else:
                            print("Maaf saldo anda kurang!")
                    else:
                        print("Maaf password anda salah!")
                else:
                    print("Jangan lupa kembali!")
            else:
                time.sleep(3)
                print("YOU LOSE")
                print("Saldo anda sekarang",idr-investasi_idr)
                
else:
    print("Pilih metode ngab!")
