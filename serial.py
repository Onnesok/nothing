import serial
import time

# Set up the serial connection to the HC-06 module
ser = serial.Serial('/dev/serial1', 9600, timeout=1)  # Added timeout for better handling
time.sleep(2)  # Wait for the serial connection to initialize

def receive_data():
    if ser.in_waiting > 0:
        return ser.readline().decode().strip()
    return None

try:
    print("Waiting for data from HC-06...")
    while True:
        # Check for incoming data
        received = receive_data()
        if received:
            print(f"Received: {received}")

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    ser.close()
