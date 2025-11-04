# import serial
# import time
# import asyncio
#
#
# # def send_character_to_esp32(character, port='COM3', baudrate=115200):
# #     ser = serial.Serial()
# #     try:
# #         time.sleep(4)
# #         ser.baudrate = 115200
# #         ser.port = 'COM8'
# #         ser.open()
# #         values = bytearray([ 17, 129])
# #         ser.write(values)
# #         time.sleep(2)  # Give ESP32 time to respond
# #         response = ser.read_all().decode(errors='ignore')
# #         print(f"ESP32 Response: {response}")
# #         ser.close()
# #     except serial.SerialException as e:
# #         print(f"Serial error: {e}")
# #         ser.close()
#
#
# def send_character_to_esp32(character, port='COM3', baudrate=115200):
#
#     try:
#         ser = serial.Serial(port, baudrate, timeout=1)
#         time.sleep(2)  # Wait for ESP32 to boot
#         ser.write(character.encode('utf-8'))  # Send character
#         time.sleep(0.5)  # Give ESP32 time to respond
#         response = ser.read_all().decode(errors='ignore')
#         print(f"ESP32 Response: {response}")
#         ser.close()
#     except serial.SerialException as e:
#         print(f"Serial error: {e}")
#
#
# def test2():
#     SerialObj = serial.Serial('COM3')  # COMxx  format on Windows
#     # ttyUSBx format on Linux
#     SerialObj.baudrate = 115200  # set Baud rate to 9600
#     SerialObj.bytesize = 8  # Number of data bits = 8
#     SerialObj.parity = 'N'  # No parity
#     SerialObj.stopbits = 1  # Number of Stop bits = 1
#     time.sleep(3)
#     SerialObj.write(b'A')  # transmit 'A' (8bit) to micro/Arduino
#     SerialObj.close()
#
#
# test2()
#
#
# # async def send_character_to_esp32(character, port='COM8', baudrate=115200):
# #     await asyncio.to_thread(_send_character_blocking, character, port, baudrate)
# #
#
# send_character_to_esp32("g")

import serial
import time
import asyncio


# def send_character_to_esp32(character, port='COM3', baudrate=115200):
#     ser = serial.Serial()
#     try:
#         time.sleep(4)
#         ser.baudrate = 115200
#         ser.port = 'COM8'
#         ser.open()
#         values = bytearray([ 17, 129])
#         ser.write(values)
#         time.sleep(2)  # Give ESP32 time to respond
#         response = ser.read_all().decode(errors='ignore')
#         print(f"ESP32 Response: {response}")
#         ser.close()
#     except serial.SerialException as e:
#         print(f"Serial error: {e}")
#         ser.close()
#

def send_character_to_esp32(character, port='COM3', baudrate=115200):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        ser.reset_input_buffer()
        ser.reset_output_buffer()

        ser.dtr = False
        ser.rts = False
        time.sleep(2)  # Wait for ESP32 to boot

        # ser.write(character.encode('utf-8'))
        # ser.write(b'A#')  # '#' is the terminator
        ser.write(character.encode('utf-8'))  # Correct usage
        ser.flush()
        time.sleep(10)  # Give ESP32 time to respond
        response = ser.read_all().decode(errors='ignore')
        print(f"ESP32 Response: {response}")
        # ser.close()

    except serial.SerialException as e:
        print(f"Serial error: {e}")
#

# def test_send_to_esp32(port="COM3", baudrate=115200, character='B'):
#
#     try:
#         ser = serial.Serial(port, baudrate, timeout=2)
#         time.sleep(2)  # Wait for ESP32 to reset
#         print(f"Sending '{character}' to ESP32 on port {port}...")
#
#         ser.reset_input_buffer()
#         ser.write(character.encode())
#         time.sleep(1)  # Wait for ESP32 to respond
#
#         incoming = ser.read_all().decode(errors='ignore')
#         if incoming:
#             print(f"Received from ESP32: {incoming}")
#         else:
#             print("No response from ESP32")
#
#         ser.close()
#
#     except serial.SerialException as e:
#         print(f"Serial error: {e}")
#
#
# # test_send_to_esp32()
#
# def test():
#     SerialObj = serial.Serial('COM8')  # COMxx  format on Windows
#     # ttyUSBx format on Linuxino
#     SerialObj.close()
#     SerialObj.baudrate = 9600  # set Baud rate to 9600
#     SerialObj.bytesize = 8  # Number of data bits = 8
#     SerialObj.parity = 'N'  # No parity
#     SerialObj.stopbits = 1  # Number of Stop bits = 1
#     time.sleep(3)
#     SerialObj.write(b'A')  # transmit 'A' (8bit) to micro/Ardu
#


if __name__ == "__main__":
    send_character_to_esp32("E")

    # send_character_to_esp32("\n")
