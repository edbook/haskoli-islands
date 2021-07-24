#!/bin/bash
if [[ $1 != "" && -f $1 ]]; then
   # Print remove message
   rm -v $1
else
   echo "Filename is not provided or filename does not exist"
fi