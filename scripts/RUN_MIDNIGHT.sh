#!/bin/sh
# Runs at Midnight

cd qc
python adjust_snet_precip.py
python check_hilo.py

cd ../dbutil
./save_snet_raw.csh
python rwis2archive.py
python snet2archive.py

cd ../smos
python plot.py 0

# Wait a bit before doing this
sleep 600
cd ../qc
python correctGusts.py

python check_station_geom.py