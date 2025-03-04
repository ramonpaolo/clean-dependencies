import os

os.system("sudo rm -rf ~/Library/Caches")
os.system("sudo rm -rf /Library/Caches")
os.system("sudo rm -rf /System/Library/Caches/")

os.system("sudo rm -rf ~/Library/Application Support/MobileSync/Backup")

os.system("sudo rm -rf /var/log")
os.system("sudo rm -rf ~/Library/Application Support/CrashReporter")
os.system("sudo rm -rf ~/.cache")
os.system("sudo rm -rf ~/.gradle/caches")
os.system("sudo rm -rf ~/Library/Developer/Xcode/DerivedData")

os.system("docker system prune -a")

os.system("brew autoremove")
