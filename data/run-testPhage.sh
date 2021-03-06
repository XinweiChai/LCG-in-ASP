#!/usr/bin/env bash

# Date: Wed Apr 18 16:43:42 JST 2018
# Generated by:
# sh run-generator.sh testPhage 'cl cro cll n' 'cl cro cll n'

# File: testPhage.an
# Inputs: cl cro cll n
# Outputs: cl cro cll n

an="testPhage.an"
outputs="cl cro cll n"
mode=${1}

echo -n "Start time: " && date
echo 'Model: testPhage.an'
echo 'Inputs: cl cro cll n'
echo 'Outputs: cl cro cll n'

(echo -n "Start time: " && date) >&2
(echo 'Model: testPhage.an') >&2
(echo 'Inputs: cl cro cll n') >&2
(echo 'Outputs: cl cro cll n') >&2

for cl in 0 1; do
for cro in 0 1; do
for cll in 0 1; do
for n in 0 1; do

init="cl=$cl, cro=$cro, cll=$cll, n=$n"
echo "--- $init"
for z in $outputs; do
  echo "# $z=1"
  ./unitrun.sh $mode "$cl$cro$cll$n" --no-debug --initial-state "$init" -i $an $z=1
  [ $? -eq 137 ] && echo '*** Killed ***'
done

done
done
done
done

echo -n "End time: " && date
(echo -n "End time: " && date) >&2

