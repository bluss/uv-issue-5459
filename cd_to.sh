#!/bin/bash

# cd to $1 then execute the rest of the command line

cd "$1"
shift
"$@"
