**Neural Style Transfer On Real-Time Camera**

This application is a command-line interactive application built on top of the NST.

**How to use?**

1. Clone this repository

`git clone git@github.com:roncmss/NST-project.git`


2. Retrieve the pre-trained models, run the bash script file with
```
cd NST-project
bash download.sh
```

3. Start the program

`python3 wrapper.py` 



The program will prompt a message to make user choose to apply the model on image or real-time camera.

For the camera-based application, user can press `n` to apply the next model to the video to see different mounted styles. And user can press `p`
to exit.
