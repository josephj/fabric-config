#!/bin/bash

if [ -z "$1" ]; then
  echo "Please provide the file path"
  exit 1
fi

cat "$1" | fabric -p write_component-test