#!/bin/bash

set -eu

base_sha=${1:-origin/main}
head_sha=${2:-HEAD}

function get_affected() {
  git diff --name-only "$base_sha" "$head_sha" | grep "projects" | cut -d "/" -f3 | uniq -u
}

affected=$(get_affected)

if [ -n "$affected" ]; then
  for i in $affected; do
    make build project="${i}";
  done
else
  echo "no affected projects, skipping build ..."
fi
