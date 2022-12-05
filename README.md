# MixerPy

Mixing two input strings together 

## Usage:

### Requirements:
### Android:
- Termux
- PyDroid 3
- QPython

### Linux:
- Thonny
- Geanny
- Vi/Vim/Nvim

To install this module go to the designated terminal and type the needed commands.

Step 1: Update, upgrade and nstall Python3 package

For Termux (Android)
```
pkg update && pkg upgrade -y && pkg install python3
```

For Linux (Debian derivatives)
```
sudo apt update && apt upgrade -y && apt install python3
```

Step 2: Install the Git repository of MixePy
```
git clone https://github.com/Yerenzter/mixer-py.git
```

Step 3: Change the directory to mixer-py
```
cd mixer-py
```

Step 4: Create a new Python 3 file 

```
vim main.py
```
Step 5: Import MixerPy module and start coding

```
import mixer

w1 = "MIXER"
w2 = "ROCKS"

print(mixer.mix(w1, w2))
```
