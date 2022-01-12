import time
import board
import displayio
import terminalio
import adafruit_aw9523
import busio
import adafruit_ssd1327
import digitalio
import usb_midi
import adafruit_midi
from adafruit_midi.note_on          import NoteOn
from adafruit_midi.note_off         import NoteOff

#  MIDI setup as MIDI out device
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

#  array for LEDs on AW9523
#leds = []
#led_pins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#  setup to create the AW9523 outputs for LEDs
#for led in led_pins:
#    led_pin = aw.get_pin(led)
#    led_pin.direction = digitalio.Direction.OUTPUT
#    leds.append(led_pin)

#  button pins, all pins in order skipping GP15
#note_pins = [board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
#            board.GP12, board.GP13, board.GP14, board.GP16, board.GP17,
#             board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26]
note_pins = [board.RX,board.MISO,board.MOSI,board.SCK,board.D25,board.D24,board.A3,board.A2,board.TX,board.D4,board.D6,board.D9,board.D10,board.D11,board.D12]

# ON DIY PCB:
# 1  2  3  4  5  6  7  8
# 9 10 11 12 13 14 15 16

note_buttons = []

for pin in note_pins:
    note_pin = digitalio.DigitalInOut(pin)
    note_pin.direction = digitalio.Direction.INPUT
    note_pin.pull = digitalio.Pull.UP
    note_buttons.append(note_pin)

#  note states
note0_pressed = False
note1_pressed = False
note2_pressed = False
note3_pressed = False
note4_pressed = False
note5_pressed = False
note6_pressed = False
note7_pressed = False
note8_pressed = False
note9_pressed = False
note10_pressed = False
note11_pressed = False
note12_pressed = False
note13_pressed = False
note14_pressed = False
note15_pressed = False
#  array of note states
note_states = [note0_pressed, note1_pressed, note2_pressed, note3_pressed,
               note4_pressed, note5_pressed, note6_pressed, note7_pressed,
               note8_pressed, note9_pressed, note10_pressed, note11_pressed,
               note12_pressed, note13_pressed, note14_pressed, note15_pressed]

#  default midi number
midi_num = 60
#  default MIDI button
button_num = 0
#  default MIDI button position
button_pos = 0
#  check for blinking LED
#led_check = None
#  time.monotonic() device
clock = time.monotonic()

#  array of default MIDI notes
midi_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]


print("Looking for input...")
while True:
    #  MIDI input
    for i in range(15):
        buttons = note_buttons[i]
        #  if button is pressed...
        if not buttons.value and note_states[i] is False:
            #  send the MIDI note and light up the LED
            midi.send(NoteOn(midi_notes[i], 120))
            note_states[i] = True
#            leds[i].value = True
        #  if the button is released...
        if buttons.value and note_states[i] is True:
            #print("Button pressed")
            #  stop sending the MIDI note and turn off the LED
            midi.send(NoteOff(midi_notes[i], 120))
            note_states[i] = False
#            leds[i].value = False
