import os
os.system("clear && figlet PROJECT")
# High Intensty
IBlack="\[\033[0;90m\]" # Black
IRed="\[\033[0;91m\]" # Red
IGreen="\[\033[0;92m\]" # Green
IYellow="\[\033[0;93m\]" # Yellow
IBlue="\[\033[0;94m\]" # Blue
IPurple="\[\033[0;95m\]" # Purple
ICyan="\[\033[0;96m\]" # Cyan
IWhite="\[\033[0;97m\]" # White
print("""

\033[0;94mQuelles sont les caractéristiques de cette cellule\033[0;97m ?
\033[0;96m1|forme
  \033[0;92mA|inrégulière
  \033[0;92mB|régulière
\033[0;96m2|vacuoles-succulentes
  \033[0;92mA|Grandes
  \033[0;92mB|Petites
""")
R=input("\033[0;97m--->> \033[0;91m")
if R == "1-B 2-A" :
    print("\033[0;95mCellule de plante")
elif R == "1-A" :
    print("\033[0;92mcellule bactérienne")
elif R == "1-B 2-B" :
    print("\033[0;96mCellule animale")
else :
    print("ERROR 404")


