#!/bin/bash

L_VIRTUAL_ENV="`basename \"$VIRTUAL_ENV\"`"

echo $L_VIRTUAL_ENV

if [ "$L_VIRTUAL_ENV" != "flask" ]; then
    . flask/bin/activate
fi

flask --app web_main --debug run


