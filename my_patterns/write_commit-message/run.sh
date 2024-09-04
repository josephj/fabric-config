#!/bin/bash

$> echo -e "$(git branch --show-current)\n$(git --no-pager diff --staged)" | fabric -p write_commit-message
