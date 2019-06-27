## Python Resources

#### Recommended Python Distribution
[Anaconda](https://www.anaconda.com/distribution/) is a quick, easy way to get python and a really useful collection of packages.

#### Anaconda install guide:
##### This guide assumes you already followed [linux guide 1.a.](../Linux/README.md)
1. Get the linux installer for x86_64. Click [here](https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh) to start the download.
2. Open a terminal
  ![terminal](Pictures/terminal.png)
  ![terminal2](Pictures/terminal2.png)
3. Run these commands:
  * `sudo apt-get update`
  * `sudo apt-get -y install libbz2-1.0:amd64`
    * These commands will install packages you need to install anaconda. You can paste things into a terminal with right click + paste (ctrl-v doesn't work)

  * `chmod +x Downloads/Anaconda3-2019.03-Linux-x86_64.sh`
    * This command will make the anaconda installer runnable

  * `bash Downloads/Anaconda3-2019.03-Linux-x86_64.sh`
    * This will run the installer
    * You will be prompted to accept a license (type yes, hit enter), choose a default install location (hit enter), and run conda init (type yes, hit enter)
    * After the installer is done, it will tell you to open a new terminal for the changes to take effect. When you open a new terminal you should see:

      __(base) pi@raspberrypi:~ $__

4. Make Chromium your default browser. Here are pictures to show you how:
![default_browser1](Pictures/default_browser1.png)
![default_browser2](Pictures/default_browser2.png)
![default_browser3](Pictures/default_browser3.png)
![default_browser4](Pictures/default_browser4.png)
![default_browser5](Pictures/default_browser5.png)

  * Jupyter Lab is a great IDE (Integrated Development Environment) to start with, and it runs inside a web browser. Run the command: `jupyter lab` to launch it.

#### Next Steps:

This website, and all the guides and projects displayed here, live in a code repository hosted by github. That means that this content is Version Controlled (the edit history is tracked) and can be easily downloaded and updated.

##### To download all projects and guides, open a terminal and run this command:
`git clone https://github.com/mzurzolo/STBS.git`

##### When that command finishes, you should see a new folder named STBS. You can run `ls` to check.
##### To get the most updated version of the projects:
1. Change directory to STBS: `cd ./STBS`
2. Get any updates: `git pull`

#### Continue to [python project notes](Projects/README.md)
