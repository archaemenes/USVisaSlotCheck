
#!/usr/bin/bash
DIR='/home/archaemenes/software/automation' # add your working directory
PYTHON='/home/archaemenes/anaconda3/envs/vfs/bin/python' # add python path
stamp=`date +"%d%m%Y_%H.%M"`

echo "#########################################" &&
date && echo -n "___START" && echo '' &&
#cp $DIR/sendText.txt $DIR/slots_df/"$stamp"__slot.txt &&
#cp $DIR/full_page_screenshot.png $DIR/screenshots/"$stamp"__ss.png &&
cp $DIR/output.txt $DIR/log.txt &&
$PYTHON $DIR/notification.py &&
#convert full_page_screenshot.png -crop 481x440+137+133 fpso.png
#tesseract $DIR/full_page_screenshot.png stdout > $DIR/tes.txt &&
tesseract $DIR/full_page_screenshot.png stdout| sed 's/"\|//g'| sed "s/'\|‘//g" > $DIR/tes.txt 
head -26 $DIR/tes.txt|grep -i "VAC" |sed 's/\./,/g'|grep -i "ju."| grep ",.24" > $DIR/output.txt 
truncate -s -1 $DIR/output.txt 
cat $DIR/log.txt | sed 's/2024.*//g' > $DIR/pl.txt 
cat $DIR/output.txt | sed 's/2024.*//g' > $DIR/nl.txt 
grep -vwf $DIR/pl.txt $DIR/nl.txt > $DIR/sendText.txt 
$PYTHON $DIR/bot.py 
cp $DIR/sendText.txt $DIR/slots_df/"$stamp"__slot.txt 
cp $DIR/full_page_screenshot.png $DIR/screenshots/"$stamp"__ss.png 
date &&
echo -n "  ___SCRIPT_DONE" &&
echo '' &&
echo "___________________________________________" &&
echo ''
