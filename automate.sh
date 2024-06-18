#!/bin/bash
DIR='/home/archaemenes/software/automation'
iterations=20162
for ((i=1; i<=iterations; i++));
do
	bash $DIR/scriptsNew.sh >> $DIR/mainLog.txt
	echo ""
	echo ">" "ITERATIONS:" && echo -n "$i" 
	echo ""
	sleep 60
	#bash $DIR/countdown.sh
       	#echo ""
done
