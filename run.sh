nohup ./watch -n120 "python crawl.py file.txt >> file.txt" &
sleep 10
./watch -n60 "cat file.txt | awk 'BEGIN { FS = \"\t\" } (\$1 == \"N\"){print \$5 , \"-->\",  \$4}'"
