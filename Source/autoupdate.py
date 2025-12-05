import subprocess
import os

def update_system():
    commands = [
         "apt update",
	 "apt list --upgradable",
	 "DEBIAN_FRONTEND=noninteractive apt upgrade -y",
         "apt autoremove -y"
    ]
    for cmd in commands:
        process = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(process.stdout)
        if process.stderr:
            print("Error:", process.stderr)

def check_and_reboot():
    if os.path.exists("/var/run/reboot-required"):
        print("Reboot is required. Restarting now...")
        subprocess.run("reboot", shell=True)
    else:
        print("No reboot needed.")

if __name__ == "__main__":
    update_system()
    check_and_reboot()
