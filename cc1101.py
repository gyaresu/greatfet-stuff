from greatfet import GreatFET, protocol

board = GreatFET()

def spi_read(device, length, command):
    data = device.vendor_request_in(request=protocol.vendor_requests.SPI_READ, length=length, value=command)
    return data

def spi_write(device, value, data, timeout):
    data = device.vendor_request_out(protocol.vendor_requests.SPI_WRITE, value=value, data=data, timeout=1000)

# 10.5:  0x3F The 64-byte TX FIFO and the 64-byte RX FIFO are accessed through the 0x3F address.



