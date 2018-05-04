#!/usr/bin/env bash
# Basic range in for loop
# run bash filename
for value in {0..19}
do
    sh run-generator.sh 'model'$value 'n1 n2' 'n6 n7 n8 n9 n10'
    sh run-model$value.sh an > run-model$value.out
done
echo All done
