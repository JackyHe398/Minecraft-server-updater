# JackyHe398 v1.0(.sh)-2021-0916
# JackyHe398 v1.0(.py)-2021-1121
# JackyHe398 v1.0(.py)-2021-1205
import os
line = "=============================================================="

print(f""+ line + "\n      PLEASE CLOSE THE SERVER BEFORE RUNNING THE COMMAND      \n" + line)
print(f"\n\n================Starting to update the server.================\n***You are not able to undo after entering the version you want to download.***\nPress Enter to Get the Newest Version\nVersion:",end="")
version = input()

jar_path = os.getcwd() + "\\server.jar"
if os.path.isfile(jar_path):
    os.remove(jar_path)
os.chdir('BuildTools')

if version == "":
    os.system("java -jar BuildTools.jar")
else:
    os.system("java -jar BuildTools.jar --rev " + version)

os.rename('spigot-'+ version +'.jar','server.jar')
os.system("MOVE server.jar \"" + os.getcwd() + "\\..\"")


print("press anykey to continue")
input()

