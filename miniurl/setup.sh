#!/usr/bin/bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar -xvzf geckodriver-v0.26.0-linux64.tar.gz
rm geckodriver-v0.26.0-linux64.tar.gz
cp geckodriver /usr/local/bin
chmod 755 /usr/local/bin/geckodriver
cp miniurl.py $HOME
chmod +x $HOME/miniurl.py
echo "#!/usr/bin/bash" >> /usr/local/bin/miniurl
echo "python3 $HOME/miniurl.py" >> /usr/local/bin/miniurl
python3 -m pip install -r requirements.txt
echo "installation complete!"
