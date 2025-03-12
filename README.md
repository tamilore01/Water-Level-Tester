# Project Materials and Versions Used

- 	Arduino IDE: latest version
-   Python: latest version (2025)
-   PySerial: version 3.13
-   Edge-TTS: version 7.0.0
-   Hardware: Arduino Mega 2560
		          Arduino Water Level Sensor


# Project Steps

1. In the Arduino IDE:
  * create an int variable and assign it an analog pin number
  * create a variable for the LED and assign it a digital pin number
  * initialize the serial com at 9600 bits per second (baud rate)
  * initialize the LED pin as an output
  * in a loop, read the input on the analog pin number from the very first step
-       create a variable to store this in, like sensorValue
  * print out what is read to the console
-       Serial.println(sensorValue)
  * set up a condition for the LED light turning on/off
  * add a delay, so that the audio that is printed out using edge-tts</b> is given enough time between each read.</br> I recommend a delay of 10+ seconds.

2. Test the System:
  * Test the water levels in the Arduino IDE using the Serial Monitor
  * This is to ensure that the number is reading in the time duration/delay set
  
3. Connect Arduino and Python so they communicate:
- Install the Python libraries necesary:
  * pyserial, edge-tts, and asyncio
  * Use Python to send serial signals to the Arduino when the water level is </br> greater than 300 (or whatever limit you set it to),
  * the LED light will turn on, otherwise, it will stay off.

4. Using edge-tts and asyncio for the text-to-speech function:
-   This will output the results of each reading of the water level as audio

# My Files


# References
- https://stackoverflow.com/questions/20021457/playing-mp3-song-on-python
- https://docs.arduino.cc/
- https://pyserial.readthedocs.io/en/latest/
- https://colab.research.google.com/drive/1Cm9esTDH1Jn0DR4apQngvqZ2JDFfgNm1

# Video 
Link: https://youtube.com/shorts/NWoIarIDn0U?feature=share

