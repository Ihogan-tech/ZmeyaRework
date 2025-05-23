import tkinter as tk
import subprocess
import style
import os

PATH, THISFILE = os.path.split(os.path.dirname(os.path.realpath(__file__)))
def customPath(dirName):
    path = os.path.join(os.getcwd(), dirName)
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    os.chmod(path, 511)
    return path

def display_settings(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()

    # Title Label
    title_label = tk.Label(main_frame, text="Settings", **style.LABEL_STYLES)
    title_label.pack(pady=style.PAD_Y)

    # Update Signatures Function
    def update_signatures():

        try:
            subprocess.run([PATH+"\\Zmeya_Backend\\ClamAV\\freshclam.exe"], check=True)
            update_main_frame("Signature update successful.")
        except subprocess.CalledProcessError as e:
            update_main_frame(f"Signature update failed: {str(e)}")

    # Update Signatures Button
    btn_update_signatures = tk.Button(main_frame, text="Update Signatures", command=update_signatures, **style.BUTTON_STYLES)
    btn_update_signatures.pack(pady=style.PAD_Y)

