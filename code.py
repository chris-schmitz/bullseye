import board
import digitalio
import time
import adafruit_dotstar as dotstar
import neopixel

totalPixels = 25
neopixelPin = board.D3
# dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
rings = neopixel.NeoPixel(neopixelPin, totalPixels,
                          auto_write=False, brightness=0.2)

duration = 0.05
while True:
    for i in range(totalPixels):
        print(i)
        rings[i] = (0, 255, 0)
        rings.show()
        time.sleep(duration)
    for i in range(totalPixels):
        print(i)
        rings[totalPixels - 1 - i] = (0, 0, 0)
        rings.show()
        time.sleep(duration)
