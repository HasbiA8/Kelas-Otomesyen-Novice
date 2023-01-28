# Sebuah Program 1 File Alarm sudah 22.30 mengeluarkan output sebuah tulisan hore bisa

# x = input('masukin waktunya: ')
import time
from datetime import datetime

x = input('masukin waktunya (HH:MM): ')

while  True:
   now = datetime.now()
   now = now.strftime("%H:%M")
   if now == x:
    print("Hore Bisa lo")
    break
   time.sleep(1)
