import os, platform, time, sys
os.system('clear')
os.system('git pull')
time.sleep(1)
ranaxd = platform.architecture()[0]
os.system('clear')
if ranaxd == '64bit':
 print(' [+] Your Device is 64bit')
 time.sleep(1)
 import LM64
elif ranaxd == '32bit':
 print(' [+] Your Devive is 32bit')
 time.sleep(1)
 import LM64
 

