import os
import subprocess

ROB_PORT = "/dev/ttyUSB0"
folder_path = "ROB-Firmware"
all_items = os.listdir(folder_path)
files_to_upload = [f for f in all_items if os.path.isfile(os.path.join(folder_path, f))]


def upload_files(port, files):
    for file in files:
        print(f"Uploading {file} to ROB-FIRMWARE...")
        try:
            subprocess.run(
                [
                    "mpremote",
                    "connect",
                    port,
                    "fs",
                    "cp",
                    "micropython/" + file,
                    f":{file}",
                ],
                check=True,
            )
            print(f"✅ {file} uploaded successfully.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to upload {file}: {e}")


def delete_files(port, files):
    for file in files:
        try:
            print(f"Deleting {file} from {port}...")
            subprocess.run(["mpremote", "connect", port, "rm", file], check=True)
            print(f"✅ {file} deleted.")
        except subprocess.CalledProcessError:
            print(
                f"❌ Failed to delete {file}. It may not exist or there was a connection issue."
            )


if __name__ == "__main__":
    selection = int(
        input(
            "ROB-FIRMWARE 3.0 FIRMWARE MANAGER\n 1. Upload Firmware \n 2. Delete Firmware \n"
        )
    )
    if selection == 1:
        upload_files(ROB_PORT, files_to_upload)
    elif selection == 2:
        delete_files(ROB_PORT, files_to_upload)