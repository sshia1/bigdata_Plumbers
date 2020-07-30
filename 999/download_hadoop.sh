#!/bin/sh
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
wget http://mirror.cc.columbia.edu/pub/software/apache/hadoop/common/hadoop-3.1.3/hadoop-3.1.3.tar.gz
