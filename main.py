import pyfirmata
from time import sleep

board = pyfirmata.Arduino('COM3')
i = 3

while i < 14:
    board.digital[i].write(1)
    sleep(1)
    board.digital[i].write(0)
    i += 1
    board.digital_ports[]

