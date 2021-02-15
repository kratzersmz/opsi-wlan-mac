# opsi-wlan-mac

## Info
This script reads from opsi hardware database the networkcontrollers description. If it's finding 'wireless' in this field it will add the mac and dns entry on udm server. If you own wireless hardware which is not recognized with with script feel free to send me your marker, as said, currently it only detects "wireless"

## HowTo run
ssh to opsi server (backup)

git clone https://github.com/kratzersmz/opsi-wlan-mac.git

cd opsi-wlan-mc

python wlan-mac-adding.py
