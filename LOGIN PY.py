def Aritmatika():
  print("            <--- Operasi Aritmatika --->")
  print("Masukkin dua bilangan yahh ⊂⁠(⁠´⁠･⁠◡⁠･⁠⊂⁠ ⁠)⁠∘⁠˚⁠˳⁠°")
  while True:
    try:
      print("Bilangan Pertama: ")
      bilangan = int(input())
      if bilangan > 0:
        break
      else:
        print("Masukkin bilangan diatas 0 (>.<)")
    except:
      print("Tolong masukkin angka (⁠.⁠ ⁠❛⁠ ⁠ᴗ⁠ ⁠❛⁠.⁠))")
  while True:
    try:
      print("Bilangan kedua: ")
      bilangan1 = int(input())
      if bilangan1 > 0:
        break
      else:
        print("Masukkin bilangan diatas 0 (>.<)")
    except:
      print("Tolong masukkin angka yahh.. (⁠.⁠ ⁠❛⁠ ⁠ᴗ⁠ ⁠❛⁠.)")     
  print("******************")
  print(f"Bilangan yang kamu masukkin itu... ({bilangan}) dan ({bilangan1})\nPilih Operasi Aritmatikanya (⁠≧⁠▽⁠≦⁠)")
  print("a. +\nb. -\nc. x\nd. ÷\ne. %(modulus)\nf. keluar dari program")
  pl = ["+", "a", "a. +"]
  min = ["-", "b", "b. -"]
  kal = ["x", "c", "c. x"]
  bag = ["÷", "d", "d. ÷"]
  mod = ["%", "e", "e. %(modulus)", "modulus"]
  
  def hitung(pl, min, kal, bag, mod):
    while True:    
      try:
        operasi = input(" Masukkin disini:\n •> ").lower()
        if operasi in pl:
          plus = bilangan + bilangan1
          print(f"Hasil dari {bilangan} + {bilangan1} adalah {plus}")
          break
        elif operasi in min:
          minus = bilangan - bilangan1
          print(f"Hasil dari {bilangan} - {bilangan1} adalah {minus}")
          break
        elif operasi in kal:
          kali = bilangan * bilangan1
          print(f"Hasil dari {bilangan} × {bilangan1} adalah {kali}")
          break
        elif operasi in bag:
          bagi = bilangan / bilangan1
          print(f"Hasil dari {bilangan} ÷ {bilangan1} adalah {bagi}")
          break
        elif operasi in mod:
          modulus = bilangan % bilangan1
          print(f"Hasil dari pembagian sisa ({bilangan} dan {bilangan1}) adalah {modulus}")
          break
        elif operasi == "f":
          print("Keluar Dari Program. Terimakasih (⁠≧⁠▽⁠≦⁠)")
          break
        else:
          print(f"Pilihanmu ga ada •́⁠ ⁠ ⁠‿⁠ ⁠,⁠•̀")
      finally:
        print("Tekan Enter Untuk Kembali ke Menu Program")
    input()    
  hitung(pl, min, kal, bag, mod)

def Materi():
  print("Kali ini kita akan membahas loop atau pengulangan\n 'Apasih itu Loop?..'\n •> Loop adalah perulangan. Didalam sebuah program loop ini dapat dijadikan validasi input, pengkoreksian data base\n 'Jenis loop di Python ada apa aja?...'\n •> Ada 3 jenis yaitu.. for loop, while loop")
  print("Tekan Enter Untuk Kembali ke Menu Program")
  input()
  
def login():
  nama = ["Ray", "Aulia", "Bella", "Bila"]
  cek = False 
  print("------ LOGIN ------")
  print(" (>///<)\nBella meminta input pengguna!!")
  print(" Masukkin nama kamu!!")
  
  def masuk(cek):
   while True:
      pilihan = input("  •> ").capitalize()
      if pilihan in nama:
        cek = True
        if cek:
          print(f"\nBerhasil, selamat datang {pilihan}")
          break
      else:
        print("\nNama kamu ga ada??, Masukkin Ulang!")
  masuk(cek)
  def menu():
    art =  ["a", "operasi aritmatika", "a. operasi aritmatika"]
    mtri = ["b", "materi python", "b. materi python"]
    while True:
      try:
        print("------ MENU PROGRAM ------")
        print("a. Operasi Aritmatika")
        print("b. Materi Python")
        print("c. Perhitungan Diskon")
        print("d. Talk santay with Bella")
        men_pro = input("\nMasukkin pilihanmu!!\n •> ").lower()
        if men_pro in art:
          Aritmatika()
        elif men_pro in mtri:
          Materi()
      except:
        print(f"Pilihannya ga ada •́⁠ ⁠ ⁠‿⁠ ⁠,⁠•̀")
  menu()
login()