#!/bin/sh

# generate_project.sh is a shell script (it's not python).
# shell scripts are just another way to tell your computer what to do.
# you could perform all of the actions
# in this script manually (on a command line), but these steps should not be
# the focus of the lesson. I put the shell script here so you could ignore
# the details of project setup for now. I'll write a translation/explanation
# of what's happening right above each line.

# Get any updates
#git pull

PROMPT=true

project_path() {
  # Prompt user to edit project path
  read -e -i "${PROJECT_PATH}" -p "Project path: " result1
  # Set project path to whatever the user entered
  PROJECT_PATH="${result1:-$PROJECT_PATH}"
}

project_name() {
  # Prompt user to enter a project name, defaulting to the project name set above
  read -e -i "$PROJECT_NAME" -p "Project name: " result
  # Set project name to whatever the user entered
  PROJECT_NAME="${result:-$PROJECT_NAME}"
}

create_project() {
  PROJECT_PATH="$PROJECT_PATH/$PROJECT_NAME"
  mkdir -p $PROJECT_PATH
  cp -i scripts/template/requirements.txt "${PROJECT_PATH}"
  cp -i scripts/template/README.md "${PROJECT_PATH}"
  cp -i scripts/template/project.backup.py "${PROJECT_PATH}/${PROJECT_NAME}.backup.py"
  sed 's/project/'"${PROJECT_NAME}"'/g' scripts/template/work_here.sh > "${PROJECT_PATH}/work_here.sh"
  printf "Success!\n"
  printf "To start working on your new project, run:\n\n"
  printf "\tcd ${PROJECT_PATH}\n"
  printf "and\n\tsource work_here.sh\n\n"
  PROMPT=false
}

while $PROMPT ; do
  # Create two variables. PROJECT_PATH will be set to the current working directory
  # PROJECT_NAME will be "default"
  # pwd is a command that means "print working directory"
  PROJECT_PATH=$(pwd)
  PROJECT_NAME="default"
  project_name
  project_path
  printf "\nProject will be created at: ${PROJECT_PATH}/${PROJECT_NAME}\n\n"
  read -e -p "Look good? Yes, Edit, Cancel (y/e/c)" result0
  case "$result0" in
    y|Y ) create_project ;;
    e|E ) printf "\nStarting over\n\n" ;;
    c|C ) PROMPT=false ;;
  esac
done

# Note 1: The p flag also creates parent directories as needed, but that's not
# a relevant detail for how I'm using it here. Parent directories are folders
# that hold other folders. The command "mkdir -p parent1/child1/inputs" will
# create: a folder parent1 (if it doesn't exist),
#         a folder child1 inside of parent1 (if it doesn't exist),
#         and a folder inputs inside of child1 (if it doesn't exist).
# The command "mkdir parent1/child1/inputs" will only create the last folder
# (inputs) and it will only do that if the other two folders already exist.
# If they don't, or if the inputs folder already exists,
# "mkdir parent1/child1/inputs" will produce an error message.
