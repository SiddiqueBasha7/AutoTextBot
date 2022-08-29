import pyautogui as auto
import time
import pyfiglet

banner = pyfiglet.figlet_format("AutoText Bot")
print(banner)
print("                           By K1NGM4K3R \n")
print("Open Application and click the textbox you want to sent \n")

n = int(input("Enter the count of msg: "))
msg = str(input("Enter the message : "))
print("Bot job will started in 5 secs...")
print("Note : If you want to stop press CTRL + Z")
time.sleep(5)
for i in range(0,n):
    auto.write(msg)
    auto.press('enter')
    time.sleep(1)
print("Bot job completed")