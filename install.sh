#!/bin/bash

echo "[+] Updating system..."

sudo apt update

echo "[+] Installing dependencies..."

sudo apt install python3 python3-pip git curl -y

echo "[+] Installing Python packages..."

pip3 install -r requirements.txt

echo "[+] Installing Ollama..."

curl -fsSL https://ollama.com/install.sh | sh

echo "[+] Pulling AI model..."

ollama pull mistral

echo "[+] Installing Sherlock..."

git clone https://github.com/sherlock-project/sherlock.git

pip3 install -r sherlock/requirements.txt
echo "[+] Installation completed."
