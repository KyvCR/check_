#Latihan Tiket KRL 

print("========== Form Pemesanan Tiket KRL ==========\n")
class pemesananTiket:
    def __init__(self):
        self.namaPenumpang = []
        self.umurPenumpang = ''
        self.stasiunAwal = ''
        self.jarakAwal = ''
        self.jaraAhkir = ''
        self.stasiunAhkir = ''
        self.alamatPenumapng = ''
        # self.hargaTiket = hargaTiket

    def regisPenumapng(self):
        totalPenumpang = int(input('Masukkan Jumlah Penumpang : '))
        pnp = []
        count = 1
        for penumpang in range(totalPenumpang):
            print(f'\nPenumpang ke-{count}')
            nama = input('Masukkan Nama : ')
            umur = int(input('Masukan Umur : '))
            alamat = input('Masukkan Alamat : ')
            pnp.append([nama, umur, alamat])
            count += 1
        for dataPenumpang in pnp:
            print(f'\n=====Data Penumpang=====')
            print(f'Nama Penumpang : {dataPenumpang[0]}')
            print(f'Umur Penumpang : {dataPenumpang[1]}')
            print(f'Alamat Penumpang : {dataPenumpang[2]}')
            count += 1
        print(pnp[0][0])
        print(pnp[1][0])
        
            

    def stKeberangkatan(self):
        
        print('Pliih Stasiun Awal')
        print('1. Tanah Abang')
        print('2. Jakarta Kota')
        print('3. Manggarai')
        
        pilihan = input('Masukan Pilihan : ')
        if pilihan == '1' or pilihan == 'Tanah Abang':
            self.stasiunAwal = 'Tanah Abang'
            self.jarakAwal = 0
        elif pilihan == '2' or pilihan == 'Jakarta Kota':
            self.stasiunAwal = 'Jakarta Kota'
            self.jarakAwal = 10
        elif pilihan == '3' or pilihan =='Manggari':
            self.stasiunAwal = 'Manggarai'
            self.jarakAwal = 20
        else:
            print('salah pilih')

    
    def stTujaun(self):
        print('\nPliih Stasiun Ahkir')
        print('1. Cisauk')
        print('2. Depok')
        print('3. Bogor')
        pilihan = input('Masukkan Pilihan : ')

        if pilihan == '1' or pilihan == 'Cisauk':
            self.stasiunAhkir = 'Cisauk'
            self.jaraAhkir = 80
        elif pilihan == '2' or pilihan == 'Depok':
            self.stasiunAhkir = 'Depok'
            self.jaraAhkir = 50
        elif pilihan == '3' or pilihan == 'Bogor':
            self.stasiunAhkir = 'Bogor'
            self.jaraAhkir = 80

    def hargaTiekt(self):
        jarak = self.jaraAhkir - self.jarakAwal
        self.hargaTiekt = int(jarak) * 10000
        
        print(f'\nTn / Ny \t\t {self.namaPenumpang} \nkeberangkatan dari St \t {self.stasiunAwal} \nTujuan ke St \t\t {self.stasiunAhkir} \nDengan Harga \t\t {self.hargaTiekt}')
        


# nama = input('Masukkan Nama anda : ')
# umur = int(input('Masukkan Umur anda : '))
# stAwal = input('Masukkan Stasiun Awal : ')
# stAhkir = input('Masukkan Stasiun Ahkir : ')
# harga = int(input('Masuskan Harga : '))


pemesan = pemesananTiket()
pemesan.regisPenumapng()
# pemesan.stKeberangkatan()
# pemesan.stTujaun()
# pemesan.hargaTiekt()