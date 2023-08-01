@echo off

REM Change directory to Image
cd Image

REM Convert PNG frames to binary
py png2bin.py frames\*.png image.bin

REM Change directory to Song
cd ../Song

REM Convert MIDI to binary
py midi2bin.py nyan.mid song.bin

REM Go back to the main directory
cd ..

REM Concatenate image, song, and message files into data.bin
copy /b Image\image.bin + Song\song.bin + Other\message.txt data.bin

REM Compress data.bin using the compressor
Compressor\compress.exe data.bin compressed.bin

echo Compression completed successfully.
