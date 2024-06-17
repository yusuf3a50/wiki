#### Linux minto wont start due to graphics drivers issues
```
sudo ubuntu-drivers list
sudo ubuntu-drivers devices
```

to switch to the video drivers you want, you're essentially installing them rather than just enabling them?

`sudo apt-get install xserver-xorg-video-nouveau`
or
`sudo apt-get install nvidia-381`