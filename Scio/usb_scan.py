import subprocess
import os

def check_usb():
    output = subprocess.check_output("lsblk -o NAME,TRAN", shell=True)
    data = str(output)
    
    if "usb" in data:
        # Extract the USB drive name (e.g., "sdb1")
        lines = data.splitlines()
        for line in lines:
            if "usb" in line.decode():
                device = line.split()[0].decode()
                mount_point = f"/media/{device}"
                print(f"USB device detected: {mount_point}")
                
                # Now scan the USB for suspicious files
                check_for_suspicious_files(mount_point)


def check_for_suspicious_files(mount_point):
    suspicious_files = ['.exe', '.bat', '.vbs', 'autorun.inf']
    for root, dirs, files in os.walk(mount_point):
        for file in files:
            if any(file.endswith(ext) for ext in suspicious_files):
                print(f"Suspicious file found: {os.path.join(root, file)}")

#~~~~~~~~~~~~~~ Use Antivirus ClamAV to scan drive if files are found: ~~~~~~~~~~~~~~~~~
                scan_usb(mount_point)


def scan_usb(usb_device):
    # Example: Scanning the mounted USB drive with ClamAV
    try:
        subprocess.check_output(f"clamscan -r /media/{usb_device}", shell=True)
        print(f"Scan complete for {usb_device}")
    except subprocess.CalledProcessError as e:
        print(f"Error scanning {usb_device}: {e}")

check_usb()
