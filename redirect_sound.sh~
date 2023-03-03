#!/bin/bash
output="$(pacmd list-sinks |grep " * index:" -A 1 |grep name |cut -d "<" -f 2 |cut -d ">" -f 1)"
echo "Using output ${output}"
input="$(pacmd list-sources |grep "${output}.monitor" -B 1 |grep index |cut -d : -f 2 |tr -d " ")"
echo "Using input ${input}"
pacmd set-default-source "${input}"
