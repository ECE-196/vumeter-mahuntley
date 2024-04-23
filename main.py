import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26,  
    board.IO47,
    board.IO33, 
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value
    print(volume)

    # Adjusted linear thresholds starting above the noise floor of 15000
    # Assuming the desired range for LED activation starts from 15000 to a max value, e.g., 48000
    # Calculate incremental steps based on the range and number of LEDs
    base_threshold = 15000
    max_value = 48000
    step = (max_value - base_threshold) / len(leds)
    volume_thresholds = [base_threshold + step * i for i in range(len(leds))]

    # Update LED states based on volume
    for i, led in enumerate(leds):
        if volume > volume_thresholds[i]:
            led.value = True
        else:
            led.value = False
