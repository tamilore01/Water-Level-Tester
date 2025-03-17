import serial
import time
import edge_tts
import asyncio
import tempfile
import os


# Configure the serial port - MacOS looks somethinglike this: "/dev/ttyUSB0"
port = "COM15"  # Replace with your serial port
baud_rate = 9600
arduino = serial.Serial(port, baud_rate)


async def text_to_speech(text, voice):
    communicate = edge_tts.Communicate(text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_path = tmp_file.name
        await communicate.save(tmp_path)
    return tmp_path

try:
    while True:
        # Send data
        message_to_send = "ON\n"
        arduino.write(message_to_send.encode('utf-8'))
        print(f"Sent: {message_to_send.strip()}")
       
        # Receive data
        if arduino.in_waiting > 0:
            received_data = arduino.readline().decode('utf-8').strip()
            audio = asyncio.run(text_to_speech(f"The water level is {received_data}", "en-NZ-MitchellNeural - en-NZ (Male)"))
            os.system('start ' + audio)
            print(f"Received: {received_data}")

        time.sleep(1)  # Wait for 1 second

except serial.SerialException as e:
    print(f"Error: {e}")
finally:
    arduino.close()
    print("Serial port closed")
