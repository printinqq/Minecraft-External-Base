# Minecraft External Base

This Python script allows you to check if a Java process (`javaw.exe`) is running on your system, and allows you to intergrate your own code that only works when javaw.exe is running, this is made for minecraft.

## Prerequisites

- Python 3.x
- psutil library (install using `pip install psutil`)

## Usage

1. Clone or download the repository to your local machine.
2. Make sure you have the `psutil` library installed by running `pip install psutil`.
3. Open the script file `main.py` in a text editor.
4. intergrate your code within the `run_autoclicker` function.
5. Save the file.
6. Run the script by executing `py main.py` in command prompt.

## Functionality

The script performs the following steps:

1. It checks if a Java process (`javaw.exe`) is running on your system.
2. If a Java process is found, it displays a message "Instance Found."
3. It then executes the `run_autoclicker` function, where you can add your own code.
4. If no Java process is found, it displays a message "No Instance of Java Found."
5. The script continues to check for the presence of the Java process in an infinite loop with a 1-second delay between checks.

## Integration of Your Code

To integrate your own code into the script:

1. Open the script file `main.py` in a text editor.
2. Locate the `run_autoclicker` function within the script.
3. Replace the existing `print` statement with your code.
4. Save the script file.

## Screenshots // UI

- Can be located in the screenshots folder.

## Support

If you have any questions, suggestions, or need assistance, please join our [Discord Server](https://discord.gg/AfgpyywTTh)
