#!/bin/bash

GITHUB_WORKSPACE="$1"
REMOTE_BASE_DIR="$2"
REMOTE_SUB_DIR="$3"

mv "${GITHUB_WORKSPACE}/_build/*" "${GITHUB_WORKSPACE}/."
rm -r "${GITHUB_WORKSPACE}/_build"

mkdir -p "${GITHUB_WORKSPACE}/${REMOTE_SUB_DIR}"; mv _build/* "$_"

echo "REMOTE_BASE_DIR: $REMOTE_BASE_DIR"
echo "REMOTE_SUB_DIR: $REMOTE_SUB_DIR"

rsync \
  -navhizP \
  --stats \
  --progress \
  --relative "${GITHUB_WORKSPACE}/./${REMOTE_SUB_DIR}" \
  staging:"${REMOTE_BASE_DIR}/"
