#!/bin/bash

# Sanal ortamı etkinleştir (venv klasörünüzün yolunu buraya ekleyin)
source ./venv/bin/activate

# Python betiğini sürekli çalıştırmak için while döngüsü
while true
do
    # Python betiği çalıştır (main.py yerine betiğinizin adını kullanın)
    python main.py
done

# Sanal ortamı devre dışı bırak (Bu satır muhtemelen hiç çalışmayacak)
deactivate
