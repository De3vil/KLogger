rm /var/lib/dpkg/lock
rm /var/cache/apt/archives/lock
rm /var/lib/apt/lists/lock
sudo dpkg --add-architecture i386
sudo apt install python3
sudo wget https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe
wine python-3.8.10.exe
wine msiexec /i python-3.8.10.exe
sudo wine ~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python38-32/python.exe -m pip install --upgrade pip
sudo wine ~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python38-32/python.exe -m pip install  colored requests  pyinstaller pynput
pip install colored requests pyinstaller pynput
pip3 install colored requests pyinstaller pynput
apt install -y gnome-shell-extension-dashtodock