#!/bin/bash

# minimalistic regression tester for REST APIs
old="http://localhost:3000"
new="http://localhost:3001"

OPTS="-b --ignore-stdin"
if [ "$1" = "-v" ]; then
  VERBOSE=true
fi

tail -n +2 requests.csv | while IFS=, read -r id method endpoint payload
do
  if diff <(http $OPTS $method $old$endpoint) <(http $OPTS $method $new$endpoint); then
    if [ "$VERBOSE" = true ]; then
      printf "%-70s%s\n" "$id: $method $base$endpoint"  PASSED
    fi
  else
    printf "%-70s%s\n" "$id: $method $base$endpoint"  FAILED
  fi
done
