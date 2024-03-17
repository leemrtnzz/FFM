import os
import sys
import time
from datetime import datetime

# Waktu
waktu = datetime.now()
tahun, bulan, hari = waktu.year, waktu.month, waktu.day
jam, menit, detik = waktu.hour, waktu.minute, waktu.second

# Warna
W, G, R = "", "", ""
if sys.platform in ["linux", "linux2"]:
    W = "\033[0m"
    G = "\033[32;1m"
    R = "\033[31;1m"

# Banner
banner = (f"{G} d88888b d88888b .88b  d88. \n 88'     88'     88'YbdP`88  {R}- Fastboot Flashing Mobile\n"
          f"{G} 88ooo   88ooo   88  88  88  {R}- Version : 1.1\n {G}88~~~   88~~~   88  88  88  {R}- Author : Alee Martinezz\n"
          f"{G} 88      88      88  88  88  {R}- Donate : +6283841365567 (AX)\n {G}YP      YP      YP  YP  YP ")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def port():
    clear_screen()
    print(f"{R}-----------------------------\n{G}[!] Cek Devices\n{R}-----------------------------\n")
    os.system("fastboot devices")
    print(f"{R}\n-----------------------------\n")

def twrp():
    try:
        print(f"{G}[+] Menginstall TWRP...")
        namaF = input("Masukan nama file : ")
        if not os.path.isfile(namaF):
            print(f"{R}[!] Gagal menginstall TWRP\n")
        else:
            os.system(f"fastboot flash recovery TWRP/{namaF}")
            print(f"{G}[+] Berhasil menginstall TWRP\n[!] Rebooting...")
            time.sleep(3)
            os.system("fastboot reboot")
    except Exception as e:
        print(f"{R}\n[!] Gagal menginstall TWRP\n{e}\n")

def flash():
    try:
        print(f"{R}------------------------\n{G}[1] Flash all\n[2] Flash all except data storage\n{R}------------------------")
        pilih = int(input(f"{W}Pilih menu : "))
        if pilih not in [1, 2]:
            print(f"{R}\n[!] Pilih menu dengan benar\n")
            return

        namaF = input(f"{G}Masukan nama folder di path ROM : ")
        if not os.path.isdir(f"ROM/{namaF}"):
            print(f"{R}\n[!] Gagal flashing ROM/Folder tidak di temukan\n")
        else:
            print(f"{G}[+] Flashing rom...")
            os.system(f"fastboot flash boot ROM/{namaF}/boot.img")
			os.system(f"fastboot flash tz ROM/"{namaF}"/tz.mbn")
			os.system(f"fastboot flash sbll ROM/"{namaF}"/sbll.mbn")
			os.system(f"fastboot flash rpm ROM/"{namaF}"/rpm.mbn")
			os.system(f"fastboot flash aboot ROM/"{namaF}"/emmc_appsboot.mbn")
			os.system(f"fastboot flash tzbak ROM/"{namaF}"/tz.mbn")
			os.system(f"fastboot flash rpmbak ROM/"{namaF}"/rpm.mbn")
			os.system(f"fastboot flash abootbak ROM/"{namaF}"/emmc_appsboot.mbn")
			os.system(f"fastboot flash devcfg ROM/"{namaF}"/devcfg.mbn")
			os.system(f"fastboot flash lksecapp ROM/"{namaF}"/lksecapp.mbn")
			os.system(f"fastboot flash cmnlib ROM/"{namaF}"/cmnlib.mbn")
			os.system(f"fastboot flash cmnlib64 ROM/"{namaF}"/cmnlib64.mbn")
			os.system(f"fastboot flash keymaster ROM/"{namaF}"/keymaster.mbn")
			os.system(f"fastboot flash devcfgbak ROM/"{namaF}"/devcfg.mbn")
			os.system(f"fastboot flash lksecappbak ROM/"{namaF}"/lksecapp.mbn")
			os.system(f"fastboot flash cmnlibbak ROM/"{namaF}"/cmnlib.mbn")
			os.system(f"fastboot flash cmnlib64bak ROM/"{namaF}"/cmnlib64.mbn")
			os.system(f"fastboot flash keymasterbak ROM/"{namaF}"/keymaster.mbn")
			os.system(f"fastboot flash dsp ROM/"{namaF}"/adspso.bin")
			os.system(f"fastboot erase boot")
			os.system(f"fastboot flash modem ROM/"{namaF}"/NON-HLOS.bin")
			os.system(f"fastboot flash system ROM/"{namaF}"/system.img")
			os.system(f"fastboot flash cache ROM/"{namaF}"/cache.img")
			os.system(f"fastboot flash userdata ROM/"{namaF}"/userdata.img")
			os.system(f"fastboot flash recovery ROM/"{namaF}"/recovery.img")
			os.system(f"fastboot flash boot ROM/"{namaF}"/boot.img")
			os.system(f"fastboot flash misc ROM/"{namaF}"/misc.img")
			os.system(f"fastboot flash splash ROM/"{namaF}"/splash.img")
			os.system(f"fastboot flash cust ROM/"{namaF}"/cust.img")
            print(f"{G}[!] Flashing ROM selesai\n[!] Rebooting...")
            time.sleep(3)
            os.system("fastboot reboot")
    except ValueError:
        print(f"{R}\n[!] Pilih menu dengan benar\n")

def adb():
    try:
        print(f"{G}[+] Menginstall adb & fastboot....")
        os.system("cp ADB/fastboot /usr/local/bin")
        os.system("cp ADB/adb /usr/local/bin")
        print(f"{G}[+] Menginstall adb & fastboot selesai")
    except Exception as e:
        print(f"{R}[!] Terjadi kesalahan: {e}")

def oem():
    clear_screen()
    print(f"{R}--------------------------\n{G}Check OEM & lock".center(30) + f"\n{R}--------------------------\n{G}")
    os.system("fastboot oem device-info")
    print(f"{G}\n--------------------------")
    try:
        print(f"{R}--------------------------\n{G}[1] Lock OEM [2] Cancel\n{R}--------------------------")
        pilih = int(input(f"{W}Pilih menu : "))
        if pilih == 1:
            clear_screen()
            print(f"{R}[!] Locking OEM...")
            time.sleep(3)
            os.system("fastboot oem lock")
            print(f"{G}\n[!] Success locking OEM\n")
        elif pilih == 2:
            print(f"{R}\n[!] Cancel for lock OEM\n")
        else:
            print(f"{R}\n[!] Pilih menu dengan benar\n")
    except ValueError:
        print(f"{R}\n[!] Pilih menu dengan benar\n")

def about():
    clear_screen()
    print(f"{R}------------------------------------\n{G}Fastboot Flashing Mobile".center(37) +
          f"\n{R}------------------------------------\n{G}Coder : Alee Martinezz\nFind Me :\nFacebook :{R} http://fb.me/leemrtnzz\n"
          f"{G}Telegram :{R} http://t.me/leemrtnzz\n{G}Github :{R} http://github.com/leemrtnzz\n{G}Whatsapp :{R} +6283841365567\n"
          f"{R}------------------------------------\n{G}Donate :\nPaypal :{R} https://paypal.me/leemrtnzz\n{G}Phone :{R} +6283841365567 (Axis)\n"
          f"{R}------------------------------------")

def reset():
    try:
        print(f"{R}[!] Me-reset data...")
        os.system("fastboot -w")
        print(f"{G}[!] Me-reset data selesai\n[!] Rebooting....")
        time.sleep(3)
        os.system("fastboot reboot")
    except Exception as e:
        print(f"{R}[!] Terjadi kesalahan: {e}")

def splash():
    try:
        print(f"{G}[!] Menginstall splash...")
        masukan = input("Masukan nama file splash : ")
        os.system(f"fastboot flash splash SPLASH/{masukan}.img")
                print(f"{G}[!] Install splash selesai")
        time.sleep(3)
        print(f"{G}[!] Rebooting....")
        os.system("fastboot reboot")
    except Exception as e:
        print(f"{R}[!] Terjadi kesalahan: {e}")

def update():
    try:
        print(f"{G}[!] Updating tools...")
        os.system("git pull")
        print(f"{G}[!] Update success")
    except Exception as e:
        print(f"{R}[!] Koneksi/File Error: {e}")

def menu():
    try:
        for dir_name in ["TWRP", "ROM", "ADB", "SPLASH"]:
            os.makedirs(dir_name, exist_ok=True)

        clear_screen()
        print(f"{banner}\n{R}--------{G}| {hari}/{bulan}/{tahun} |{R}--------\n")
        print(f"{G}[1] Check Device        [5] TWRP\n[2] Check & Lock OEM    [6] Reset\n[3] Flash ROM           [7] Splash\n[4] Install ADB         [8] About Tool\n[0] Exit                [9] Update Tool\n{R}--------{G}|  {jam}:{menit}:{detik}  |{R}--------")
        pilihan = int(input(f"{W}Pilih menu : "))

        if pilihan == 1:
            port()
        elif pilihan == 2:
            oem()
        elif pilihan == 3:
            flash()
        elif pilihan == 4:
            adb()
        elif pilihan == 5:
            twrp()
        elif pilihan == 6:
            reset()
        elif pilihan == 7:
            splash()
        elif pilihan == 8:
            about()
        elif pilihan == 9:
            update()
        elif pilihan == 0:
            print(f"{R}\n[!] Selamat tinggal\n")
            exit()
        else:
            print(f"{R}\n[!] Pilih menu dengan benar\n")
    except ValueError:
        print(f"{R}\n[!] Pilih menu dengan benar\n")
    except Exception as e:
        print(f"{R}[!] Terjadi kesalahan: {e}")

if __name__ == "__main__":
    while True:
        menu()
