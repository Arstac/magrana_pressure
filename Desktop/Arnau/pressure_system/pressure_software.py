# Programa dissenyat per Magrana.
# El programa llegeix entrades analogices mitjançant el chip MCP3008 i analitza els resultats.

# Autor: Arnau Costa
# License: Public Domain
import time

# Importa la llibreria SPI (for hardware SPI) i la del MCP3008.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


# Loop principal del programa.
while True:
    # Llegeix totes les lectures del ADC i les guarda en una llista
    values = [0]*8
    for i in range(8):
    	# La funcio read_adc obtindrà el valor del canal especificat (0-7).
        values[i] = mcp.read_adc(i)
    # Print els valors guardats
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    # Pausa de mig segon
    time.sleep(0.5)