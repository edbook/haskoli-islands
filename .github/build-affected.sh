#!/bin/bash

head_sha=${1:-HEAD}
for i in $(git diff --dirstat=files origin/main "$head_sha" | grep "src/projects" | cut -d "/" -f3); do
  make build project=${i};
done
