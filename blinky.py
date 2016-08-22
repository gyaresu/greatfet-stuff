# This is some blinky code to show Python interaction with Great Scott Gadget's new GreatFET "Azalea"
# http://greatscottgadgets.com/greatfet/
#
# Install the development tools to get the Python library.
# https://github.com/dominicgs/GreatFET-experimental/tree/master/host

from greatfet import GreatFET, protocol
from time import sleep
from random import randint

board = GreatFET()

def blinky(times, delay):
    for i in range(0, times):
        board.vendor_request_out(protocol.vendor_requests.LED_TOGGLE,randint(2,4))
        sleep(delay)

blinky(100, 0.1)
