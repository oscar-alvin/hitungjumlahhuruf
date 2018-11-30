#created by alvin meko
#www.kodingbeta.wordpress.com

def hurufDalamNama():
    print(nama)
    huruf = {}
    for h in nama:
        if h in huruf: #huruf.has_key(h)
            jml = huruf[h] + 1
        else:
            jml = 1
        huruf.update( {h:jml} )
    return huruf

nama = input("Nama Anda: ")
for k, v in hurufDalamNama().items():
    print(k, " = ", v)

input("tekan enter untuk keluar")
