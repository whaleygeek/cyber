from microbit import *
import radio

radio.config(group=3, length=64)
radio.on()

PLAIN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # unshifted caeser cipher
WHEEL = ".........................." # build up your key here
#WHEEL= "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # use this to show ciphered text

def cipher(wheel, message, shifti=0, shiftd=0):
    result = ""
    shift = shifti
    for letter in message:
        index = ord(letter) - ord('A')
        index = (index + shift) % len(wheel)
        result = result + wheel[index]
        shift = (shift + shiftd) % 26
    return result

# on reset, try to receive the first message we see
message = None
display.show("?")
while message is None:
    try:
        message = radio.receive()
        if message is not None:
            break
    except: # reset radio if it crashes
        radio.off()
        radio.on()
   
radio.off()

# try to decipher the message using the wheel you have worked out       
message = cipher(WHEEL, message)
index = 0
display.show(message[index])
       
# read out the decoded message, using the presently worked out wheel 
while True:    
    if button_a.was_pressed():
        if index > 0:
            index = index - 1
            display.clear()
            sleep(100)
        else:
            display.show("[")
            sleep(1000)
        display.show(message[index])

    elif button_b.was_pressed():
        if index < len(message)-1:
            index = index + 1
            display.clear()
            sleep(100)
        else:
            display.show("]")
            sleep(1000)
        display.show(message[index])
        
