import os

def push_firmware(serial_port="/dev/ttyUSB0", firmware="firmware.hex"):
    os.system(f"avrdude -v -patmega328p -carduino -P{serial_port} -b115200 -D -Uflash:w:{firmware}:i")

if __name__ == "__main__":
    push_firmware()
