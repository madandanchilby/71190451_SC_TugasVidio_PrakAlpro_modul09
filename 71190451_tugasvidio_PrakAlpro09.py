'''
Buatlah sebuah program yang meminta masukan dari user dan menyimpannya
dalam bentuk tipe data list dalam bentuk angka. Saat user memasukkan masukan ’done’, maka
program akan menampilkan nilai maksimum dan minimum dari deretan angka yang sudah user
masukkan. Gunakan fungsi list max() dan min() pada program ini.
'''
nilai=[]
while True:
    try:
        angka=int(input('masukan angka:'))
        if angka <=0 or angka >0:
            nilai.append(angka)
    except:
        break
nilai.sort()
print(nilai)
print('nilai maksimum:',max(nilai))
print('nilai minimum:',min(nilai))
print('nilai rata-rata=', sum(nilai)/len(nilai))
