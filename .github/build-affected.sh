#!/bin/bash

set -euox pipefail

head_sha=${1:-HEAD}
for i in $( git diff --name-only "$head_sha" origin/main | grep "src/projects" | cut -d "/" -f3 | uniq -u); do
  make build project="${i}";
done
