import turtle
import json
from itertools import permutations
from pprint import pprint
from datetime import datetime

masukan = []
status = []
def login():
    waktu = datetime.now()
    today = waktu.strftime("%d/%m/%Y %H:%M:%S")
    inpLogin = ''
    while inpLogin != "q":
        print('''
           ========= SELAMAT DATANG =========
           |            PROCEDIA            |
           |      (PROSES DI KOTA-KOTA)     |
           |         Login       [1]        |
           |         Daftar      [2]        |
           ==================================''')
        inpLogin = input("Masukkan Perintah [1. Login] [2. Daftar] : ")
        if (inpLogin == "2") :
            nama = input("Ketik Nama : ")
            password = input("Ketik Password : ")
            berkas = {
                "Nama" : nama,
                "Password" : password
            }
            masukan.append(berkas)
            berkas2 = {
                "Data Pengguna" : masukan,
                "Jadwal" : status
            }
            with open('Tugas Akhir.json', 'w') as file:
                json.dump(berkas2, file, indent=2)
            print("Pendaftaran Berhasil. Silahkan Login")
        elif (inpLogin == "1") :
            try:
                with open('Tugas Akhir.json', 'r') as file :
                    data = json.load(file)["Data Pengguna"][0]
                namaLogin = input("Ketik Nama : ")
                passwordLogin = input("Ketik Password : ")
                if(namaLogin == data["Nama"]):
                    if(passwordLogin == data["Password"]):
                        if(namaLogin == data["Nama"] and passwordLogin == data["Password"]):
                            print("Login Berhasil Pada", today)
                            menu()
                            break
                        else:
                            print("Akun yang anda masukkan tidak ada")
                    else:
                        print("Password yang anda masukkan salah")
                else:
                    print("Nama yang anda masukkan salah")
            except:
                print("Akun tidak ada.\nSilahkan Daftar terlebih dahulu")
        else:
            print("Data yang anda masukkan tidak benar")
def menu():
    masuk = ''
    while masuk !='q':
        print('''
           ============ PROCEDIA ============
           | Tata letak titik kota     [1]  |
           | Pilih kota keberangkatan  [2]  |
           | Akun yang terkait         [3]  |
           | Hapus akun                [4]  |
           | Exit                      [5]  |
           ==================================
NB = Masukkan 2x apabila ingin melihat urutan alur yang tidak tampil''')
        masuk = input("Masukkan kode : ")
        if masuk == '1':
            graf()
        elif masuk == '2':
            urutanAlur()
        elif masuk == '3':
            bacaAkun()
        elif masuk == '4':
            hapusAkun()
        elif masuk == '5' or masuk == 'exit' or masuk == 'Exit' or masuk == 'EXIT':
            ulangKeluar()
            menu()
        elif masuk == '6':
            search(daftar_biaya, n)
        else:
            print("Perintah yang anda masukkan tidak ada\n")

def urutanAlur():
    i=0
    kota = ['Malang','Situbondo','Lumajang','Bondowoso','Jember','Banyuwangi']
    for data in range(len(graph)):
        print(f"Mulai dari kota {data+1}: {kota[i]},{tsp(graph, data)}")
        i=i+1

    tanya = input("Pilih Jalur Nomer 1, 2, 3, 4, 5, 6 = ")
    if tanya == '1':
        jalurpertama()
        perulangan()
    elif tanya == '2':
        jalurkedua()
        perulangan()
    elif tanya == '3':
        jalurketiga()
        perulangan()
    elif tanya == '4':
        jalurkeempat()
        perulangan()
    elif tanya == '5':
        jalurkelima()
        perulangan()
    elif tanya == '6':
        jalurkeenam()
        perulangan()
            
def perulangan():
    tanya = input("Apakah ingin melihat urutan alur lagi? [y/n]")
    if tanya == 'y' or tanya == 'Y':
        urutanAlur()
    elif tanya == 'n' or tanya == 'N':
        menu()
    else:
        perulangan()
        
def ulangKeluar():
    tanya = input("Apakah anda ingin keluar atau kembali ke menu [y/n]")
    if tanya == 'y' or tanya == 'Y':
        exit()
    elif tanya == 'n' or tanya == 'N':
        menu()
    else:
        ulangKeluar()

def hapusAkun():
    tampung = []
    berkas2 = {
        "Data Pengguna" : tampung,
        "Jadwal" : status
    }
    pertanyaan = input("Nama Akun yang di hapus : ")
    with open('Tugas Akhir.json') as file :
        baca = json.load(file)["Data Pengguna"]
        for hapus in baca:
            if pertanyaan == hapus['Nama']:
                continue
            else:
                tampung.append(hapus)
    with open('Tugas Akhir.json', 'w') as file:
        baru = json.dump(berkas2, file, indent = 2)
    print("Akun Anda Sudah Terhapus")
    menu()
            
def bacaAkun():
    with open('Tugas Akhir.json') as file :
        tampilan = json.load(file)
    print(tampilan["Data Pengguna"])
    menu()
   
def graf():
    try:
        drawing_area = turtle.Screen()
        drawing_area.bgcolor("light green")
        drawing_area.title("Tampilan Kota yang Akan Dilewati")
        drawing_area.setup(startx=0, starty=0, width=700, height=600)
        skk = turtle.Turtle()
        skk.speed(5)
        skk.penup()
        skk.goto(-250,200)#1
        skk.dot()
        skk.goto(-250,200)#1
        skk.write('Malang', font = 40)
        skk.pendown()
        skk.width(3)
        skk.goto(250,200)#2
        skk.write('Situbondo', font = 40)
        skk.dot()
        skk.goto(140,50)#4
        skk.write('Bondowoso', font = 40)
        skk.dot()
        skk.goto(-140,50)#3
        skk.write('Lumajang', font = 40)
        skk.dot()
        skk.goto(-250,200)
        skk.goto(-250,-100)#5
        skk.write('Jember', font = 40)
        skk.dot()
        skk.goto(250,-100)#6
        skk.write('Banyuwangi', font = 40)
        skk.dot()
        skk.goto(250,200)#2
        skk.goto(140,50)#4
        skk.goto(250,-100)#6
        skk.goto(-250,-100)#5
        skk.goto(-140,50)#3
        skk.goto(-250,200)#1

        #pelabelan
        skk.penup()
        skk.goto(0,205)
        skk.write('50', font = 20)
        skk.goto(190,100)
        skk.write('10', font = 20)
        skk.goto(0,55)
        skk.write('30', font = 20)
        skk.goto(-210,100)
        skk.write('15', font = 20)
        skk.goto(-270,50)
        skk.write('25', font = 20)
        skk.goto(-210,-20)
        skk.write('10', font = 20)
        skk.goto(0,-90)
        skk.write('45', font = 20)
        skk.goto(190,-10)
        skk.write('15', font = 20)
        skk.goto(255,55)
        skk.write('20', font = 20)
        skk.goto(-250,200)
        turtle.exitonclick()
    except:
        menu()

def jalurpertama():
    try:
        drawing_area = turtle.Screen()
        drawing_area.bgcolor("light green")
        drawing_area.title('''Urutan Kota dari Kota Malang 
        [(0, 1, 3, 5, 4, 2), 145]''')
        drawing_area.setup(startx=0, starty=0, width=700, height=600)
        skk = turtle.Turtle()
        skk.speed(6)
        skk.penup()
        skk.goto(-250,200)#1
        skk.dot()
        skk.goto(-250,200)#1
        skk.write('Malang', font = 40)
        skk.pendown()
        skk.width(3)
        skk.goto(250,200)#2
        skk.write('Situbondo', font = 40)
        skk.dot()
        skk.goto(140,50)#4
        skk.write('Bondowoso', font = 40)
        skk.dot()
        skk.goto(-140,50)#3
        skk.write('Lumajang', font = 40)
        skk.dot()
        skk.goto(-250,200)
        skk.goto(-250,-100)#5
        skk.write('Jember', font = 40)
        skk.dot()
        skk.goto(250,-100)#6
        skk.write('Banyuwangi', font = 40)
        skk.dot()
        skk.goto(250,200)#2
        skk.goto(140,50)#4
        skk.goto(250,-100)#6
        skk.goto(-250,-100)#5
        skk.goto(-140,50)#3
        skk.goto(-250,200)#1

        #pelabelan
        skk.penup()
        skk.goto(0,205)
        skk.write('50', font = 20)
        skk.goto(190,100)
        skk.write('10', font = 20)
        skk.goto(0,55)
        skk.write('30', font = 20)
        skk.goto(-210,100)
        skk.write('15', font = 20)
        skk.goto(-270,50)
        skk.write('25', font = 20)
        skk.goto(-210,-20)
        skk.write('10', font = 20)
        skk.goto(0,-90)
        skk.write('45', font = 20)
        skk.goto(190,-10)
        skk.write('15', font = 20)
        skk.goto(255,55)
        skk.write('20', font = 20)
        skk.goto(-250,200)

        #urutan
        skk.color('red')
        skk.goto(-250,200)#1
        skk.pendown()
        skk.speed(1)
        skk.goto(250,200)#2
        skk.goto(140,50)#4
        skk.goto(250,-100)#6
        skk.goto(-250,-100)#5
        skk.goto(-140,50)#3
        skk.goto(-250,200)#1
        skk.penup()
        skk.goto(-300,230)
        skk.write('''Urutan Kota Malang, Situbondo, Bondowoso,
         Banyuwangi, Jember, Lumajang, Malang''', font = 20)
        turtle.exitonclick()
    except:
        menu()

def jalurkedua():
    try:
        drawing_area = turtle.Screen()
        drawing_area.bgcolor("light green")
        drawing_area.title('''Urutan Kota dari Kota Situbondo 
        [(1, 3, 5, 4, 2, 0), 145]''')
        drawing_area.setup(startx=0, starty=0, width=700, height=600)
        skk = turtle.Turtle()
        skk.speed(6)
        skk.penup()
        skk.goto(-250,200)#1
        skk.dot()
        skk.goto(-250,200)#1
        skk.write('Malang', font = 40)
        skk.pendown()
        skk.width(3)
        skk.goto(250,200)#2
        skk.write('Situbondo', font = 40)
        skk.dot()
        skk.goto(140,50)#4
        skk.write('Bondowoso', font = 40)
        skk.dot()
        skk.goto(-140,50)#3
        skk.write('Lumajang', font = 40)
        skk.dot()
        skk.goto(-250,200)
        skk.goto(-250,-100)#5
        skk.write('Jember', font = 40)
        skk.dot()
        skk.goto(250,-100)#6
        skk.write('Banyuwangi', font = 40)
        skk.dot()
        skk.goto(250,200)#2
        skk.goto(140,50)#4
        skk.goto(250,-100)#6
        skk.goto(-250,-100)#5
        skk.goto(-140,50)#3
        skk.goto(-250,200)#1

        #pelabelan
        skk.penup()
        skk.goto(0,205)
        skk.write('50', font = 20)
        skk.goto(190,100)
        skk.write('10', font = 20)
        skk.goto(0,55)
        skk.write('30', font = 20)
        skk.goto(-210,100)
        skk.write('15', font = 20)
        skk.goto(-270,50)
        skk.write('25', font = 20)
        skk.goto(-210,-20)
        skk.write('10', font = 20)
        skk.goto(0,-90)
        skk.write('45', font = 20)
        skk.goto(190,-10)
        skk.write('15', font = 20)
        skk.goto(255,55)
        skk.write('20', font = 20)
        skk.goto(-250,200)

        #urutan
        skk.color('red')
        skk.goto(250,200)#2
        skk.pendown()
        skk.speed(1)
        skk.goto(140,50)#4
        skk.goto(250,-100)#6
        skk.goto(-250,-100)#5
        skk.goto(-140,50)#3
        skk.goto(-250,200)#1
        skk.goto(250,200)#2
        skk.penup()
        skk.goto(-300,230)
        skk.write('''Urutan Kota Situbondo, Bondowoso, Banyuwangi, Jember, 
        Lumajang, Malang, Situbondo''', font = 20)
        turtle.exitonclick()
    except:
        menu()
        
def jalurketiga():
    try:
        drawing_area = turtle.Screen()
        drawing_area.bgcolor("light green")
        drawing_area.title('''Urutan Kota dari Kota Lumajang 
        [(2, 0, 1, 3, 5, 4), 145]''')
        drawing_area.setup(startx=0, starty=0, width=700, height=600)
        skk = turtle.Turtle()
        skk.speed(6)
        skk.penup()
        skk.goto(-250,200)#1
        skk.dot()
        skk.goto(-250,200)#1
        skk.write('Malang', font = 40)
        skk.pendown()
        skk.width(3)
        skk.goto(250,200)#2
        skk.write('Situbondo', font = 40)
        skk.dot()
        skk.goto(140,50)#4
        skk.write('Bondowoso', font = 40)
        skk.dot()
        skk.goto(-140,50)#3
        skk.write('Lumajang', font = 40)
        skk.dot()
        skk.goto(-250,200)
        skk.goto(-250,-100)#5
        skk.write('Jember', font = 40)
        skk.dot()
        skk.goto(250,-100)#6
        skk.write('Banyuwangi', font = 40)
        skk.dot()
        skk.goto(250,200)#2
        skk.goto(140,50)#4
        skk.goto(250,-100)#6
        skk.goto(-250,-100)#5
        skk.goto(-140,50)#3
        skk.goto(-250,200)#1

        #pelabelan
        skk.penup()
        skk.goto(0,205)
        skk.write('50', font = 20)
        skk.goto(190,100)
        skk.write('10', font = 20)
        skk.goto(0,55)
        skk.write('30', font = 20)
        skk.goto(-210,100)
        skk.write('15', font = 20)
        skk.goto(-270,50)
        skk.write('25', font = 20)
        skk.goto(-210,-20)
        skk.write('10', font = 20)
        skk.goto(0,-90)
        skk.write('45', font = 20)
        skk.goto(190,-10)
        skk.write('15', font = 20)
        skk.goto(255,55)
        skk.write('20', font = 20)
        skk.goto(-250,200)

        #urutan
        skk.color('red')
        skk.goto(-140,50)#3
        skk.pendown()
        skk.speed(1)
        skk.goto(-250,200)#1
        skk.goto(250,200)#2
        skk.goto(140,50)#4
        skk.goto(250,-100)#6
        skk.goto(-250,-100)#5
        skk.goto(-140,50)#3
        skk.penup()
        skk.goto(-300,230)
        skk.write('''Urutan Kota Lumajang, Malang, Situbondo, 
        Bondowoso, Banyuwangi, Jember, Lumajang''', font = 20)
        turtle.exitonclick()
    except:
        menu()
        
def jalurkeempat():
    try:
        drawing_area = turtle.Screen()
        drawing_area.bgcolor("light green")
        drawing_area.title('''Urutan Kota dari Kota Bondowoso 
        [(3, 5, 4, 2, 0, 1), 145]''')
        drawing_area.setup(startx=0, starty=0, width=700, height=600)
        skk = turtle.Turtle()
        skk.speed(6)
        skk.penup()
        skk.goto(-250,200)#1
        skk.dot()
        skk.goto(-250,200)#1
        skk.write('Malang', font = 40)
        skk.pendown()
        skk.width(3)
        skk.goto(250,200)#2
        skk.write('Situbondo', font = 40)
        skk.dot()
        skk.goto(140,50)#4
        skk.write('Bondowoso', font = 40)
        skk.dot()
        skk.goto(-140,50)#3
        skk.write('Lumajang', font = 40)
        skk.dot()
        skk.goto(-250,200)
        skk.goto(-250,-100)#5
        skk.write('Jember', font = 40)
        skk.dot()
        skk.goto(250,-100)#6
        skk.write('Banyuwangi', font = 40)
        skk.dot()
        skk.goto(250,200)#2
        skk.goto(140,50)#4
        skk.goto(250,-100)#6
        skk.goto(-250,-100)#5
        skk.goto(-140,50)#3
        skk.goto(-250,200)#1

        #pelabelan
        skk.penup()
        skk.goto(0,205)
        skk.write('50', font = 20)
        skk.goto(190,100)
        skk.write('10', font = 20)
        skk.goto(0,55)
        skk.write('30', font = 20)
        skk.goto(-210,100)
        skk.write('15', font = 20)
        skk.goto(-270,50)
        skk.write('25', font = 20)
        skk.goto(-210,-20)
        skk.write('10', font = 20)
        skk.goto(0,-90)
        skk.write('45', font = 20)
        skk.goto(190,-10)
        skk.write('15', font = 20)
        skk.goto(255,55)
        skk.write('20', font = 20)
        skk.goto(-250,200)

        #urutan
        skk.color('red')
        skk.goto(140,50)#4
        skk.pendown()
        skk.speed(1)
        skk.goto(250,-100)#6
        skk.goto(-250,-100)#5
        skk.goto(-140,50)#3
        skk.goto(-250,200)#1
        skk.goto(250,200)#2
        skk.goto(140,50)#4
        skk.penup()
        skk.goto(-300,230)
        skk.write('''Urutan Kota Bondowoso, Banyuwangi, 
        Jember, Lumajang, Malang, Situbondo, Bondowoso''', font = 20)
        turtle.exitonclick()
    except:
        menu()

def jalurkelima():
    try:
        drawing_area = turtle.Screen()
        drawing_area.bgcolor("light green")
        drawing_area.title('''Urutan Kota dari Kota Jember 
        [(4, 0, 2, 3, 1, 5), 145]''')
        drawing_area.setup(startx=0, starty=0, width=700, height=600)
        skk = turtle.Turtle()
        skk.speed(6)
        skk.penup()
        skk.goto(-250,200)#1
        skk.dot()
        skk.goto(-250,200)#1
        skk.write('Malang', font = 40)
        skk.pendown()
        skk.width(3)
        skk.goto(250,200)#2
        skk.write('Situbondo', font = 40)
        skk.dot()
        skk.goto(140,50)#4
        skk.write('Bondowoso', font = 40)
        skk.dot()
        skk.goto(-140,50)#3
        skk.write('Lumajang', font = 40)
        skk.dot()
        skk.goto(-250,200)
        skk.goto(-250,-100)#5
        skk.write('Jember', font = 40)
        skk.dot()
        skk.goto(250,-100)#6
        skk.write('Banyuwangi', font = 40)
        skk.dot()
        skk.goto(250,200)#2
        skk.goto(140,50)#4
        skk.goto(250,-100)#6
        skk.goto(-250,-100)#5
        skk.goto(-140,50)#3
        skk.goto(-250,200)#1

        #pelabelan
        skk.penup()
        skk.goto(0,205)
        skk.write('50', font = 20)
        skk.goto(190,100)
        skk.write('10', font = 20)
        skk.goto(0,55)
        skk.write('30', font = 20)
        skk.goto(-210,100)
        skk.write('15', font = 20)
        skk.goto(-270,50)
        skk.write('25', font = 20)
        skk.goto(-210,-20)
        skk.write('10', font = 20)
        skk.goto(0,-90)
        skk.write('45', font = 20)
        skk.goto(190,-10)
        skk.write('15', font = 20)
        skk.goto(255,55)
        skk.write('20', font = 20)
        skk.goto(-250,200)

        #urutan
        skk.color('red')
        skk.goto(-250,-100)#5
        skk.pendown()
        skk.speed(1)
        skk.goto(-250,200)#1
        skk.goto(-140,50)#3
        skk.goto(140,50)#4
        skk.goto(250,200)#2
        skk.goto(250,-100)#6
        skk.goto(-250,-100)#5
        skk.penup()
        skk.goto(-300,230)
        skk.write('''Urutan Kota Jember, Malang, Lumajang, 
        Bondowoso, Situbondo, Banyuwangi, Jember''', font = 20)
        turtle.exitonclick()
    except:
        menu()

def jalurkeenam():
    try:
        drawing_area = turtle.Screen()
        drawing_area.bgcolor("light green")
        drawing_area.title('''Urutan Kota dari Kota Banyuwangi 
        [(5, 1, 3, 2, 0, 4), 145]''')
        drawing_area.setup(startx=0, starty=0, width=700, height=600)
        skk = turtle.Turtle()
        skk.speed(6)
        skk.penup()
        skk.goto(-250,200)#1
        skk.dot()
        skk.goto(-250,200)#1
        skk.write('Malang', font = 40)
        skk.pendown()
        skk.width(3)
        skk.goto(250,200)#2
        skk.write('Situbondo', font = 40)
        skk.dot()
        skk.goto(140,50)#4
        skk.write('Bondowoso', font = 40)
        skk.dot()
        skk.goto(-140,50)#3
        skk.write('Lumajang', font = 40)
        skk.dot()
        skk.goto(-250,200)
        skk.goto(-250,-100)#5
        skk.write('Jember', font = 40)
        skk.dot()
        skk.goto(250,-100)#6
        skk.write('Banyuwangi', font = 40)
        skk.dot()
        skk.goto(250,200)#2
        skk.goto(140,50)#4
        skk.goto(250,-100)#6
        skk.goto(-250,-100)#5
        skk.goto(-140,50)#3
        skk.goto(-250,200)#1

        #pelabelan
        skk.penup()
        skk.goto(0,205)
        skk.write('50', font = 20)
        skk.goto(190,100)
        skk.write('10', font = 20)
        skk.goto(0,55)
        skk.write('30', font = 20)
        skk.goto(-210,100)
        skk.write('15', font = 20)
        skk.goto(-270,50)
        skk.write('25', font = 20)
        skk.goto(-210,-20)
        skk.write('10', font = 20)
        skk.goto(0,-90)
        skk.write('45', font = 20)
        skk.goto(190,-10)
        skk.write('15', font = 20)
        skk.goto(255,55)
        skk.write('20', font = 20)
        skk.goto(-250,200)

        #urutan
        skk.color('red')
        skk.goto(250,-100)#6
        skk.pendown()
        skk.speed(1)
        skk.goto(250,200)#2
        skk.goto(140,50)#4
        skk.goto(-140,50)#3
        skk.goto(-250,200)#1
        skk.goto(-250,-100)#5
        skk.goto(250,-100)#6
        skk.penup()
        skk.goto(-300,230)
        skk.write('''Urutan Kota Banyuwangi, Situbondo, 
        Bondowoso, Lumajang, Malang, Jember, Banyuwangi''', font = 20)
        turtle.exitonclick()
    except:
        menu()

def tsp(graph, start):
    node = []
    for node_left in range(len(graph)):
        if node_left != start:
            node.append(node_left)
    min_cost = 99999
    path = permutations(node)
    path_now = ''
    for data in path:
        current_cost = 0
        row = start
        for col in data:
            current_cost += graph[row][col]
            row = col
        current_cost += graph[col][start]
        if current_cost < min_cost:
            path_now = data
        min_cost = min(current_cost, min_cost)
    return path_now, min_cost

graph = [[ 0, 50, 15, 99, 25, 99 ],
         [ 50, 0, 99, 10, 99, 20 ],
         [ 15, 99, 0, 30, 10, 99 ],
         [ 99, 10, 30, 0, 99, 15 ],
         [ 25, 99, 10, 99, 0, 45 ],
         [ 99, 20, 99, 15, 45, 0 ]]

start = 0

login()
