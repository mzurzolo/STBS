## Project Notes

#### Assumptions:
1. I will assume you have Anaconda, and you have cloned this repository with `git clone https://github.com/mzurzolo/STBS.git`
2. I will assume you are starting each new project by opening a new terminal window. _If you don't want to open a new terminal window, the command `cd` on its own will bring you back to your home directory, and the command `deactivate` will reset your 'python environment' (more on that later)._

  I will provide a quick command to get you to the project. _example: `cd STBS/Python/Projects/project1`_

  and a 'setup script' to automate some setup tasks. This script will always be called *work_here.sh*, and the command to run it is: `source work_here.sh`

#### Project Layout:
* Each project will be in its own folder, under STBS/Python/Projects
* Each project folder will contain:
  * A setup script for the project: `source work_here.sh`
  * The main program file/the starting point of the project. It will end in .py: `project1.py`
  * A backup of the project file, just in case: `project1.backup.py`
  * Input and output folders, if necessary: `inputs`  `outputs`
  * An instruction page meant to be viewed as a webpage: `README.md`
  * A file that names python packages required for the project: `requirements.txt`
  * A python 'virtual environment' folder: `py3`
    * Virtual environments are great for setting up sandboxes to work in
    * They provide project consistency
    * They're easy to create
    * It doesn't matter if they get deleted (since they can be re-generated so easily)
    * I use them in these lessons to show you how/provide a working example (they're not totally necessary in small projects, but they keep things clean, and it's a good habit to build)
    * I automate their use here so you can ignore it if you want to. Virtual environment setup is one of the steps in work_here.sh
    * I may write up a lesson on environment and package management eventually

#### Documentation:
* Documentation is like a User's/Owner's manual
* Most software projects have documentation
* Good documentation includes quick start guides, examples, and a description of how to use the project (called an API)
* Relevant documentation will be linked in project directions, and in the comments of the projects themselves (comments are lines in a computer program that the computer ignores. They're notes to the programmer. Comments in python start with a # or have triple quotes around them)
