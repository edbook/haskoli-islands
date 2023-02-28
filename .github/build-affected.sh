#!/bin/bash

set -euox pipefail

base_sha=${1:-BASE_SHA}
head_sha=${2:-HEAD_SHA}

for i in $( git diff --name-only "$base_sha" "$head_sha" | grep "src/projects" | cut -d "/" -f3 | uniq -u); do
  make build project="${i}";
done
