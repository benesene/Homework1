#!/usr/bin/env bash

csvcut -c Dest flightdelay2007.csv |sort | uniq -c | sort -nr |awk 'BEGIN{print "Dest""-""Count"};{print $2"-"$1}'| head -4 > top3dest.csv

csvlook top3dest.csv
