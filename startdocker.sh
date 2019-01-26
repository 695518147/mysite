#!/usr/bin/env bash
if [[ -n "$1" ]];
then
    cpath=`pwd`
    docker run -it -d -p 80:80 -v $cpath/mysite/data:/usr/src/app/mysite/data $1
    echo "Service Startup Successful。port is 80"
else
    echo 'The parameter must be container ID'
fi