import csv
#untuk input Data
data = []
jumlah_data = int(input("input data = ")) #jumlah data yang mau dimasukkan
for i in range(jumlah_data):
    temp = []  #untuk menampung sementara
    for j in range(1):
        temp.append(input("Mata Kuliah : "))
        temp.append(input("Semester : "))
    data.append(temp)    #menambah

#untukWrite
with open("Datamatkul.csv", "w", newline="") as file:
    writer = csv.writer(file) #menyimpan file yang dibaca
    for i in range(jumlah_data):
        print(data[i])
        writer.writerow(data[i])
#untukOpen
with open("Datamatkul.csv", "r") as file:
    reader = csv.reader(file)
    data_matkul = []
    for baris in reader:
        data_matkul.append(baris)
    cari = input("Search matkul atau semester = ") #untuk mencari data
    #cari = False
    for i in range(len(data_matkul)):
        if data_matkul[i][0] == cari or data_matkul[i][1] == cari:
            print("Data Ditemukan pada nomor urut ke-"+ str(i+1))
            print("Mata Kuliah = ",data_matkul[i][0])
            print("Semester = ",data_matkul[i][1])
            cari = True
        if(cari == False):
            print("Not found :( ")
