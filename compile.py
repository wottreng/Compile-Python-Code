#!/usr/bin/env python3
import os
# version 3.0

# ADD MODULES TO THIS LIST THAT ARE REQUIRED FOR RUN TIME EXECUTION ex. "module_name"
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
print("[*] creating standalone binary for distribution: main.bin")
os.system("./venv/bin/python3 -m nuitka --onefile main.py")
#
print("[!] cleaning build environment..")
os.system("rm -r ./main.build && rm -r ./main.dist && rm -r ./venv")
#
print("[*] compliation complete. call function by: './main.bin'")
