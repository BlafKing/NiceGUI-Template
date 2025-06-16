@echo off
REM Delete the build and dist directories if they exist
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

REM Run the NiceGUI packer
nicegui-pack --name "PLACEHOLDER" --windowed main.py --add-data "backend;backend" --add-data "components;components" --add-data "gui;gui" --add-data "icons;icons" --add-data "static;static" --icon="icons/app-icon.ico"

echo Build complete!