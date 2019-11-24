#!/bin/sh

ANACONDA_VERSION=Anaconda3-2019.03-Linux-x86_64.sh
sudo apt-get update && sudo apt-get -y install libbz2-1.0:amd64 libgl1:amd64 libx11-dev:amd64

wget https://repo.anaconda.com/archive/$ANACONDA_VERSION && \
chmod +x $ANACONDA_VERSION &&\
bash $ANACONDA_VERSION -b &&
. ~/anaconda3/bin/activate && conda init && . ~/.bashrc
