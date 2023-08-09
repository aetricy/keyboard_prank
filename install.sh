#!/bin/sh

#pip install pygame
#pip install pynput



sudo cat > config.py <<EOF
PATH="`pwd`"
EOF

sudo cat > start.sh <<EOF
nohup python3 `pwd`/main.py &
EOF

chmod +x config.py
chmod +x start.sh
