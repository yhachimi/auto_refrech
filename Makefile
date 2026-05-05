

run: install
	python3  1337_auto_refrech.py

install: 
	pip install pyautogui
	pip install pynput


clean:
	pip uninstall pyautogui
	pip uninstall pynput
