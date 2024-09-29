import requests
from pystyle import Write
from pyfiglet import figlet_format
import os
from pystyle import Colorate, Colors
from colorama import Fore, Style

text = figlet_format("Cyber End")
Write.Print(text, Colors.red, interval=0.01)

def printcolor(text):
    print(Colorate.Horizontal(Colors.blue_to_purple, text, 1))

def printerror(text):
    print(Colorate.Color(Colors.red, text, 1))

def printgreen(text):
    print(Colorate.Color(Colors.green, text, 1))

def inputcolor(text):
    return input(Colorate.Horizontal(Colors.blue_to_purple, text, 1))

def limpar_tela():
    if os.name == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')

def obter_coordenadas(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            dados = resposta.json()
            if dados.get("status") == "success":
                return (
                    dados.get("lat"),
                    dados.get("lon"),
                    dados.get("country"),
                    dados.get("regionName"),
                    dados.get("city"),
                    dados.get("isp"),
                )
            else:
                printerror("[ERRO] Erro ao obter as coordenadas.")
                return None
        else:
            printerror("[ERRO] Erro ao obter as coordenadas.")
            return None
    except Exception as e:
        printerror(f"[ERRO] Ocorreu um erro ao obter as coordenadas: {e}")
        return None

def mostrar_mapa(ip, lat, lon):
    if lat is not None and lon is not None:
        link_mapa = f"https://www.google.com/maps?q={lat},{lon}"
        printgreen(f"Link para o Google Maps com a localização do IP: {link_mapa}")
        input("Pressione Enter para continuar...")
        limpar_tela()
    else:
        printerror("[ERRO] Não foi possível obter as coordenadas.")
def localizar_ip():
    ip = inputcolor("Digite o endereço IP a ser localizado: ")
    if not ip:
        printerror("Endereço IP não pode ser vazio.")
        inputcolor("Pressione Enter para continuar...")
        limpar_tela()
        return
    printcolor(f"Buscando informações para o IP: {ip}")
    lat, lon, country, region, city, isp = obter_coordenadas(ip)
    if lat is not None and lon is not None:
        printcolor(f"Informações de localização para o IP {ip}")
        print(f"País: {country}")
        print(f"Estado: {region}")
        print(f"Cidade: {city}")
        print(f"Provedor de Internet: {isp}")
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")
        mostrar_mapa(ip, lat, lon)
    else:
        printerror(f"[ERRO] Não foi possível localizar o IP {ip}")
        inputcolor("Pressione Enter para continuar.")
        limpar_tela()

def main():
    localizar_ip()

if __name__ == "__main__":
    main()

#feito por Mil
# oferecimento de C.E