#!/bin/sh
# bash script to check for Hadoop status, whether running or not

JPS_OUTPUT=$(jps)
# echo "${JPS_OUTPUT}"

SUB='NodeManager'
if [[ "$JPS_OUTPUT" == *"$SUB"* ]]; then
  echo "Hadoop is RUNNING!"
else
  echo "Hadoop is NOT RUNNING!"
fi
