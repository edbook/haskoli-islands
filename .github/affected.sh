#!/bin/bash

set -eu

base_sha=${1:-origin/main}
head_sha=${2:-HEAD}

function get_affected() {
  git diff --name-only "$base_sha" "$head_sha" | grep "projects" | cut -d "/" -f3 | uniq -u
}

function build_affected() {
  affected=$(get_affected)

  if [ -n "$affected" ]; then
    for i in $affected; do
      make build project="${i}";
    done
  else
    echo "no affected projects, skipping build ..."
  fi
}

while getopts 'pb' flag; do
  case "${flag}" in
    p) is_print="${OPTARG}" ;;
    b) is_build="${OPTARG}" ;;
    *) print_usage
       exit 1 ;;
  esac
done

