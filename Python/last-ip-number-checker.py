# Last Number IP Checker
# Code by Mugi F.
import requests
host = input("Input IP : ")
hitung = int(host.split('.')[3])
while hitung < 256:
    try:
        ip = '.'.join(map(str, host.split(".")[:-1]+[hitung]))
        get = requests.get('http://'+ip, timeout=0.25)
        if get.status_code == 200:
            print('http://'+ip+"/ "+str(get.status_code)+"\033[32m OK    \033[39m")
        else:
            print('http://'+ip+"/ "+str(get.status_code)+"\033[31m Error     \033[39m", end='\r')
        hitung += 1
    except requests.exceptions.ConnectionError:
        print('http://'+ip+"/ 404\033[31m Error     \033[39m", end='\r')
        hitung += 1
        pass
    finally:
        continue