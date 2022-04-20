import os

cameraCommand = "python3 neural_style_transfer_video.py --models models"

if __name__ == "__main__":
    print("************ Welcome to our Neural Style Transfer Demonstration ************")
    print("Apply to image: 1\nApply to camera feed: 2")
    userChoice = int(input("Make your choice: "))
    if userChoice == 1:
        print("image")
    elif userChoice == 2:
        os.system(cameraCommand)
    else:
        # Dummy change
        raise ValueError("you suck!")
