from pynput.keyboard import Key, Controller
import time
from colorama import init   #for windows 
init()                      #for windows
from colorama import Fore
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')



discordlogo = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssyyyyyyyyyyyyyyyyyysssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyso++///++syyyyyyyyyyyyyyyys++///++osyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyyyyyyyyyyso+///+ossssssoooo++++++++oooosssssso+///+osyyyyyyyyyyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyyyyyyyso////+osoo+//////////////////////////+ooso+////osyyyyyyyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyyyyyyo////+o+////////////////////////////////////+o+////oyyyyyyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyyyyyo////////////////////////////////////////////////////oyyyyyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyyyyo//////////////////////////////////////////////////////oyyyyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyyys////////////////////////////////////////////////////////syyyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyys//////////////////////////////////////////////////////////syyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyy+//////////////////////////////////////////////////////////+yyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyo////////////////////////////////////////////////////////////oyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyy////////////////////:////////////////////:////////////////////yyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyo/////////////////-`    `-////////////-`    `-/////////////////oyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyy/////////////////`        .//////////.        ./////////////////yyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyo////////////////-          :////////:          -////////////////syyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyy+////////////////-          :////////:          -////////////////+yyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyy//////////////////`        `//////////`        `//////////////////yyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyo//////////////////:.`    `-////////////-`    `.://////////////////oyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyy+////////////////////:::::://////////////::::::////////////////////+yyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyy+//////////////////////////////////////////////////////////////////+yyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyy///////////+////////////////////////////////////////////+///////////yyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyy+///////////+o+//////////////////////////////////////+o+///////////+yyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyo+///////////+osoo+////////////////////////////+ooso+///////////+oyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyys+////////////+osssssoo++++////////++++oossssso+////////////+syyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyyyyso+////////////+syyyyyyyyyyyyyyyyyyyyyys+////////////+osyyyyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyyyyyyysso++///////oyyyyyyyyyyyyyyyyyyyyyyyyo///////++ossyyyyyyyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssssyyyyyyyyyyyyyyyyyyyyyyyyyysssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\nyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n'
print(Fore.GREEN+ discordlogo)

keyboard = Controller()

runs = 0
print(Fore.GREEN+ "[-] Initializing")
time.sleep(1)
print(Fore.GREEN+ "[-] Ready!")
time.sleep(1)

clearConsole()
print(Fore.GREEN+ discordlogo)

print(Fore.YELLOW+"[-] DISCLAIMER: You need to have Discord open to use this script")
print(Fore.YELLOW+"[-] Github: https://github.com/KindCoder-no/send-counter")
print(Fore.GREEN+"Start number:")
start_number = input()
print(Fore.GREEN+"Stop number:")
stop_number = input()
print(Fore.GREEN+"Wait:")
wait = input()
print(Fore.GREEN+"Custom message that is sent occasionally (leave empty if you don't want any)")
custom_message = input()

clearConsole()
print(Fore.GREEN+ discordlogo)
print(Fore.GREEN+'[-] Starting in: 3')
time.sleep(1)

clearConsole()
print(Fore.GREEN+ discordlogo)
print(Fore.GREEN+'[-] Starting in: 2')
time.sleep(1)

clearConsole()
print(Fore.GREEN+ discordlogo)
print(Fore.GREEN+'[-] Starting in: 1')
time.sleep(1)

clearConsole()
print(Fore.GREEN+ discordlogo)
print(Fore.YELLOW+"[-] DISCLAIMER: You need to have Discord open to use this script")
print(Fore.YELLOW+"[-] Github: https://github.com/KindCoder-no/send-counter")
print(Fore.GREEN+'[-] Working...')

while True:
    count = int(start_number)

    while count <= int(stop_number):
        time.sleep(int(wait))
        keyboard.type(str(count))

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        int(count)
        count += 1
        
    runs += 1
    clearConsole()
    print(Fore.GREEN+ discordlogo)
    
    ##print(Fore.GREEN+'[-] Done with a run')
    print(Fore.YELLOW+"[-] DISCLAIMER: You need to have Discord open to use this script")
    print(Fore.YELLOW+"[-] Github: https://github.com/KindCoder-no/send-counter")
    print(Fore.GREEN+'[-] Total runs:', runs)
    time.sleep(int(wait))
    keyboard.type(custom_message)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    ##time.sleep(3)