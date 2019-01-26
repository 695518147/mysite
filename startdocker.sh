#!/usr/bin/env bash
echo $cpath/mysite
if [$1 == ''];
then
    echo 'The parameter must be container ID'
fi
cpath=`pwd`

docker run -it -d -p 80:80 -v $cpath/mysite/data:/usr/src/app/mysite/data $1
echo "Service Startup Successful。port is 80"


