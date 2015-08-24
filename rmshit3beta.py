#!/usr/bin/python3

import os
import getpass
import shutil

print ("""
###########
###########
##       ##                             #############
##       ##                                  ##
########### ########### ####### ##      ##   ##
##          ##  ###  ## #       ##           ##
## ##       ##  ###  ## ####### ##      ##   ##
##  ##      ##       ##       # ######  ##   ##
##   ##     ##       ##       # ##   #  ##   ##
##    ###   ##       ## ####### ##   #  ##   ##
by:
https://www.facebook.com/archdesktop
https://www.facebook.com/InSeguridadInformaticaSt
yoamotenerinternet.blogspot.com.es
It works for systems based on Debian Linux
It will run:
1-autoremove
2-clean
3-history terminal
4-trash
5-""")

usuario = getpass.getuser()
passw = input("escribe la contraseña del usuario / type user password:")
continuar= getpass.getpass("¿Deseas continuar?responde si o no / Do you want to continue?answer yes or no:")

def autoremove():
    os.system('echo '+passw+' | sudo -S apt-get autoremove -y')
def clean():
    os.system("echo "+passw+" | sudo -S apt-get clean")
def dependencias():
    os.system("echo "+passw+" | sudo  -S apt-get -f install -y")
def history(users):
    if users == "root":
        os.chdir("/root/")
        logs = open(".bash_history",'w')
        logs.write('')
        logs.close()
    else:
        os.chdir("/home/"+users+"/")
        logs = open(".bash_history",'w')
        logs.write('')
        logs.close()
def papelera(users):
    if users == "root":
        os.chdir("/root/.local/share/")
        shutil.rmtree('Trash' , True)
        os.mkdir("Trash")
    else:
        os.chdir("/home/"+users+"/.local/share/")
        shutil.rmtree('Trash' , True)
        os.mkdir("Trash")
        
if continuar == "si" or continuar == "yes":
    autoremove()
    clean()
    dependencias()
    history(usuario)
    papelera(usuario)
    print("Mantenimiento realizado con exito / Maintenance performed successfully")
elif continuar == "no":
    salir = input("pulsa enter para salir / hit enter to exit")
else:
    pass