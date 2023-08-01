@echo off
"C:\Users\octob\AppData\Local\bin\NASM\nasm.exe" -o disk.img kernel.asm
set PATH=%PATH%;C:\Program Files\qemu
qemu-system-i386 -fda disk.img -s -drive format=raw,file=disk.img

pause