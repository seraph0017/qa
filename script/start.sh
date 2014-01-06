#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=$DIR:$PYTHONPATH
export ENV=$1
source /usr/local/bin/virtualenvwrapper.sh
workon qa 

uwsgi --socket 127.0.0.1:8077 --chdir /root/maxfile/qa -H /root/.virtualenvs/qa/ --module=qa.wsgi --processes 4 --threads 2 --daemonize /root/maxfile/qa/uwsgi.log
