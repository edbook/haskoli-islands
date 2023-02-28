#!/bin/bash

set -euox pipefail

base_sha=${1:-origin/main}
head_sha=${2:-HEAD}

affected=$( git diff --name-only "$base_sha" "$head_sha" | grep "src/projects" | cut -d "/" -f3 | uniq -u)
echo "Affected projects:"
echo
echo "$affected"

for i in $affected; do
  make build project="${i}";
done
