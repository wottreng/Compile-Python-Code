#!/usr/bin/env python3
import os

# ADD MODULES TO THIS LIST THAT ARE REQUIRED FOR RUN TIME EXECUTION
required_modules_for_project: list = []

# -----------------------------------
print("[*] installing requirements...")
#
print("[*] installing patchelf {required for compiling standalone packages}")
os.system("sudo apt install patchelf")
#
print("[*] creating virtual environment: venv")
os.system("python3 -m venv venv")
#
print("[*] installing nuitka")
os.system("./venv/bin/pip3 install nuitka")
#
for module in required_modules_for_project:
    print(f"[*] Installing module, {module}, into virtual environment")
    os.system(f"./venv/bin/pip3 install {module}")
#
print("[*] creating standalone package for distribution: main.dist")
os.system("./venv/bin/python3 -m nuitka --standalone main.py")
#
print("[!] cleaning build environment..")
os.system("sudo rm -r ./main.build && sudo rm -r ./venv")
#
print("[*] compliation complete. call function by: './main.dist/main'")
