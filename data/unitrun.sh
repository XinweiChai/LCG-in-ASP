#!/usr/bin/env bash

# Max CPU time in seconds
ulimit -t 3

mode=$1; shift
name=$1; shift

its=its-ctl

bd=$name.work

sdd_xml="$bd/model.xml"
sdd_ctl="$bd/model.ctl"
bc_file="$bd/model.bc"

export TIME="%e\t%U"

do_time() {
	n="$bd/$1"; shift
	time "$@" 2>&1
	#/usr/bin/time -- "$@" 2>&1
}

if [[ "$mode" == "ph" ]]; then
	do_time ph-reach ph-reach "$@"
elif [[ "$mode" == "an" ]]; then
	do_time pint-reach pint-reach "$@"
elif [[ "$mode" == "priority" ]]; then
	do_time ph-reach ph-reach --coop-priority "$@"
elif [[ "$mode" == "phtest" ]]; then
	do_time ph-reach ph-reach --method test "$@"
elif [[ "$mode" == "sdd-bn" ]]; then
	mkdir -p $bd
	./CNA2PN ../doc/Tcell/reactions "$@" > $bd/output
	tail -n1 $bd/output > $bd/model.ctl
	head -n-1 $bd/output > $bd/model.xml
	do_time its timeout 30m $its --quiet --forward -i $bd/model.xml -ctl $bd/model.ctl
	rm -rf $bd
elif [[ "$mode" == "sdd" ]]; then
	echo -n "exporting to sdd..."
	mkdir -p $bd
	pint ph2sdd.ml --output-xml "$sdd_xml" --output-ctl "$sdd_ctl" "$@" || exit 1
	echo " done"
	do_time its-forward $its --forward -i "$sdd_xml" -ctl "$sdd_ctl"
	#do_time its-back $its --backward -i model.ph.xml -ctl model.ph.ctl
	rm -rf "$bd"
elif [[ "$mode" == "biocham" ]]; then
	echo -n "exporting to biocham..."
	mkdir -p $bd
	pint ph2bc.ml -o "$bc_file" "$@" || exit 1
	echo " done"
	export GLOBALZ=500000
	do_time biocham biocham "$PWD/$bc_file"
else
	echo "unknown mode (ph/an/phtest/sdd/biocham)"
	exit 1
fi


