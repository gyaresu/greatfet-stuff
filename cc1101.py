from greatfet import GreatFET, protocol

board = GreatFET()

def spi_read(device, length, command):
    data = device.vendor_request_in(request=protocol.vendor_requests.SPI_READ, length=length, value=command)
    return data

def spi_write(device, value, data, timeout):
    data = device.vendor_request_out(protocol.vendor_requests.SPI_WRITE, value=value, data=data, timeout=1000)

# 10.4: The command strobe registers are accessed by transferring a single header byte (no data is being transferred).
# That is, only the R/W¯ bit, the burst access bit (set to 0), and the six address bits (in the range 0x30 through 0x3D)

# 10.5:  0x3F The 64-byte TX FIFO and the 64-byte RX FIFO are accessed through the 0x3F address.
# 0xAF == 10101111

spi_write(board, value=0x3F, data=0xAFAA, timeout=1000)

#spi_read(board, 1, 0x30)
