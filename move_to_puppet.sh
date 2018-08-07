#!/bin/bash
target="puppet*"
for fileName in `ls openstackStack | grep puppet`; do
        echo $fileName
        `mv openstackStack/$fileName puppet`
done
cd puppet
for fileName in `ls .`; do
        cd $fileName
        git pull
        echo "git pull in project"$fileName
        cd ..\

done
