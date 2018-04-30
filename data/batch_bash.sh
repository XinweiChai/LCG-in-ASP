#!/usr/bin/env bash
# Basic range in for loop
for value in {0..99}
do
    sh run-generator.sh 'model'$value 'n1 n2 n3 n4 n5' 'n1 n2 n3 n4 n5'
    sh run-model$value.sh an > run-model$value.out
done
echo All done
