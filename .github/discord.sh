#!/bin/bash

content=''

print_usage() {
  printf "Usage: webhook -w <webhook_url> -c <content>\n"
}

while getopts 'c:w:' flag; do
  case "${flag}" in
    c) content="${OPTARG}" ;;
    w) webhook="${OPTARG}" ;;
    *) print_usage
       exit 1 ;;
  esac
done

curl --location --request POST "$webhook" \
  --header 'Content-Type: application/json' \
  -d "$content"
