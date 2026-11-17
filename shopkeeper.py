
import os
import time
import requests
from email.message import Message

BASE_URL = "https://otp-for-prints.onrender.com"

# Temporary folder on the shopkeeper's computer
DOWNLOAD_FOLDER = os.path.join(
    os.environ["TEMP"], "OTP_Printouts"
)

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def retrieve_document():
    otp = input("\nEnter the 6-digit OTP: ").strip()

    if not (otp.isdigit() and len(otp) == 6):
        print("Please enter a valid 6-digit OTP.")
        return

    try:
        print("\nVerifying OTP and downloading document...")

        response = requests.get(
            f"{BASE_URL}/get-file/{otp}",
            timeout=60
        )

        if response.status_code != 200:
            print("Invalid or expired OTP.")
            return

        # Get the original filename
        message = Message()
        message["content-disposition"] = response.headers.get(
            "Content-Disposition", ""
        )
        filename = message.get_filename() or f"document_{otp}"

        filename = os.path.basename(filename)
        filepath = os.path.join(DOWNLOAD_FOLDER, filename)

        with open(filepath, "wb") as file:
            file.write(response.content)

        print("\nDocument downloaded successfully!")
        print("File location:", filepath)

        # Open the document
        os.startfile(filepath)

        print("\nPrint the document using the opened application.")
        input("After printing, close the document and press ENTER here...")

        # Delete local downloaded file
        deleted = False

        for attempt in range(5):
            try:
                os.remove(filepath)
                deleted = True
                break
            except OSError:
                time.sleep(2)

        if deleted:
            print("\nLocal document deleted successfully!")
        else:
            print("\nCould not delete local file. Close the document and try again.")

        # Delete server copy
        if deleted:
            try:
                result = requests.post(
                    f"{BASE_URL}/delete-file/{otp}",
                    timeout=60
                )

                if result.ok:
                    print("Server document deleted successfully!")
                else:
                    print("Server deletion needs to be checked.")

            except requests.RequestException:
                print("Could not confirm server deletion.")

    except requests.RequestException as error:
        print("Connection error:", error)


if __name__ == "__main__":
    print("================================")
    print("       OTP SECURE PRINTOUT")
    print("================================")

    retrieve_document()

    input("\nPress ENTER to exit...")
