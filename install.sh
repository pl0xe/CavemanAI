# "This code is provided on an 'as-is' basis, 
# without any warranty of fitness for purpose 
# or non-infringement. I am not legally 
# responsible for the use or misuse of this code."

# pl0x <3

#!/bin/bash

if ! command -v ollama >/dev/null 2>&1; then
  echo "The 'ollama' command does not exist."
  curl -fsSL https://ollama.com/install.sh | sh
else
  echo "The 'ollama' command exists."
fi

if grep -q "llama3.1" <<< $(ollama list); then
  echo "llama3.1 found!"
else
  echo "llama3.1 not found."
  ollama pull llama3.1
fi

if grep -q "caveman" <<< $(ollama list); then
  echo "caveman found!"
else
  echo "caveman not found."
  echo "creating model caveman."
  ollama create caveman -f ./CavemanAI/Modelfile
fi

python3 -m pip install requirements.txt

echo "Make sure to add the 'discord.token' file into the src directory that contains your discord token"
