#!/bin/bash

GITHUB_WORKSPACE="$1"
REMOTE_BASE_DIR="$2"
REMOTE_SUB_DIR="$3"

echo "#### Moving ${GITHUB_WORKSPACE}/_build/* to ${GITHUB_WORKSPACE}/${REMOTE_SUB_DIR} ####"
set -x -e
mkdir -p "${GITHUB_WORKSPACE}/${REMOTE_SUB_DIR}"; mv "${GITHUB_WORKSPACE}/_build/*" "$_"

echo "#### Project list: ${GITHUB_WORKSPACE}/${REMOTE_SUB_DIR} ####"
set -x -e
ls -d "${GITHUB_WORKSPACE}/${REMOTE_SUB_DIR}/*"

echo "REMOTE_BASE_DIR: $REMOTE_BASE_DIR"
echo "REMOTE_SUB_DIR: $REMOTE_SUB_DIR"

set -x -e
rsync \
  -navhizP \
  --stats \
  --progress \
  --relative "${GITHUB_WORKSPACE}/./${REMOTE_SUB_DIR}" \
  staging:"${REMOTE_BASE_DIR}/"
