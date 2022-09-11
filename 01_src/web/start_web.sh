#!/bin/bash

L_VIRTUAL_ENV="`basename \"$VIRTUAL_ENV\"`"

echo $L_VIRTUAL_ENV

if [ "$L_VIRTUAL_ENV" != "aa_flask" ]; then
    . aa_flask/bin/activate
fi

flask --app web_main  --debug run --host=0.0.0.0


