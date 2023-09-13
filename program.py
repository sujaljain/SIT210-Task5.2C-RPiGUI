import tkinter as tk
import RPi.GPIO as GPIO

# GPIO pins for LEDs
LED_PINS = {
    "Red": 17,    # Replace with your GPIO pin numbers
    "Green": 18,
    "Blue": 27,
}

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Function to set the LED color
def set_led_color(color):
    for pin in LED_PINS.values():
        GPIO.output(pin, GPIO.LOW)  # Turn off all LEDs
    GPIO.output(LED_PINS[color], GPIO.HIGH)  # Turn on the selected LED

# Create the main window
root = tk.Tk()
root.title("LED Controller")
root.geometry("400x300")  # Set window size

# Create a label
label = tk.Label(root, text="Select LED Color", font=("Comic Sans", 20))
label.pack(pady=20)

# Function to handle button clicks
def button_click(color):
    set_led_color(color)

# Create buttons for each LED color
for color in LED_PINS.keys():
    button = tk.Button(root, text=color, command=lambda c=color: button_click(c))
    button.pack(pady=15)

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Start the GUI main loop
root.mainloop()

# Cleanup GPIO on program exit
GPIO.cleanup()
