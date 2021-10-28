from multiprocessing.pool import CLOSE
from requests import get, post
import requests
from concurrent.futures import ThreadPoolExecutor ,as_completed
import threading 
import sys
import getopt
import sys
from colorama import Fore, Back, Style
from colorama import init, Fore, Back, Style
import time
import threading

init(convert=True)


class dirs():

    
    FILE_ACCESS = open('dirs.txt', 'r').read().splitlines()


class threads():  
    URL = None
    TRD = None
    ERROR = 0
    Headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,ar;q=0.8",
        "cache-control": "max-age=0",
        "sec-ch-ua": """Chromium"";v=""94"", ""Google Chrome"";v=""94"", "";Not A Brand"";v=""99""",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": """Windows""",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    }
    GOOD = 0
    argv = sys.argv[1:]
    LIST_DIRS= []
    def __init__(self):
        argv = sys.argv[1:]

        opts,self.args = getopt.getopt(self.argv, "u:")
        for opt, arg in opts:
                if opt in ['-u']:
                    self.URL = arg
                    dd = self.URL[::-1]
                    #remove "/"
                    if dd[0] == '/':
                        x = dd.replace("/", "", 1)
                        self.URL = x[::-1]
        

    def run(self):
        
        for int_ in dirs.FILE_ACCESS:

            th = threading.Thread(target=self.REQ,args=(int_,))
            th.start()
            time.sleep(0.01)

            print("\rResults : " + Fore.GREEN  + str(self.GOOD) +Style.RESET_ALL +f" | {str(len(dirs.FILE_ACCESS))} | " + Fore.RED + str(self.ERROR) + Style.RESET_ALL ,"\n", Fore.GREEN + "\n".join(self.LIST_DIRS) + Style.RESET_ALL,end='\n')
        print(Fore.RED,"""
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        █ ▄▄▄ █ █ █▄ ▄▄ █ ▄▄▄ █▄ █ ▄███▄ ▄▄ ██ ▄ ██ ▄ ▄ █ █ █
        █ ███▀█ ▄ ██ ▄█▀█ ███▀██ ▄▀█████ ▄▄▄██ ▀ ████ ███ ▄ █
        █▄▄▄▄▄█▄█▄█▄▄▄▄▄█▄▄▄▄▄█▄▄█▄▄███▄▄▄███▄▄█▄▄██▄▄▄██▄█▄█ v.1
        """,Style.RESET_ALL)
    def REQ (self,dir):
        # print(dir)
        try:
            with requests.get(self.URL+dir,headers=self.Headers) as response:
                # print(response.status_code)
                    if int(response.status_code) == 200 :
                        if 'admin' in dir :
                            self.LIST_DIRS.append( Fore.BLACK + Back.BLUE +'| + ADMIN + |' +Style.RESET_ALL+self.URL + dir)
                        if 'login' in dir :
                                self.LIST_DIRS.append( Fore.BLACK + Back.BLUE +'| + LOGIN + |' +Style.RESET_ALL+self.URL + dir)
                        if 'Index' in response.text :
                            if 'php' in response.text:
                                self.LIST_DIRS.append( Fore.BLACK + Back.RED +'| + HIGH + |' +Style.RESET_ALL+self.URL + dir)
                            if 'upload' in response.text:
                                self.LIST_DIRS.append( Fore.BLACK + Back.RED +'| + HIGH + |' +Style.RESET_ALL+self.URL + dir)
                            else:
                                self.LIST_DIRS.append( Fore.BLACK + Back.RED +'| + NORMALs + |' +Style.RESET_ALL+self.URL + dir)

                        else:
                            self.LIST_DIRS.append( Fore.BLUE +'| + NORMALs + |' +Style.RESET_ALL+self.URL + dir)


                        self.GOOD +=1
                        # print(Fore.RED + self.URL +  dir +Style.RESET_ALL,end='\n')
                        time.sleep(1)
                    # elif int(response.status_code) == 403 :
                    #     self.LIST_DIRS.append( Fore.RED +'| + Forbidden + |' +Style.RESET_ALL+self.URL + dir)

                    else:
                        
                        self.ERROR +=1
            try:
                print('\r'+Fore.RED + str(self.ERROR) + Style.RESET_ALL  ,end='')
            except :
                pass
        except :
            pass
        # print("Results : " + Fore.GREEN  + str(self.GOOD) +Style.RESET_ALL +" | " + Fore.RED + str(self.ERROR) + Style.RESET_ALL  ,end='\n')
        # print("Results : " + Fore.GREEN + "\n".join(self.LIST_DIRS))


dirs()

A = threads()
if A.URL != None:
    A.run()
else:
    print(Back.RED + Fore.BLACK +  "[+] - please -u [ENTER URL]" + Style.RESET_ALL)
