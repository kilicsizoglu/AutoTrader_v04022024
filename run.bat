@echo off

:loop
REM Run the Python script (replace main.py with your script name)
python main.py
echo "Restarting..."

REM If the script exits, it will return to the loop
goto loop

REM Deactivate the virtual environment (This line will probably never run)
call deactivate