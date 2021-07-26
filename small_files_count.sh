#!/bin/bash
#depth_level=$1
#base_path=$2

rm base_path.txt
rm small_files_count.txt
rm final_list.csv

# list all folders under given  base path and store it in  base_path.txt
hdfs dfs -ls -R /user/hive/warehouse/ | awk -F / '/^d/' | awk '{print $8}' >> base_path.txt

# Loop every line in base_path.txt and filter small files  recursively (with respect to given threshold size -64MB)

while IFS="" read -r line || [ -n "$line" ]
do
        count=$(hdfs dfs -ls -R ${line} | awk '{if($5<67108864) print $8 && $1 !~ "^d"}' | wc -l)
        echo "$line","$count"  >> small_files_count.txt
# write file path and count of files under every folder in out
done < base_path.txt


# echo  "${count_per_folder}" | awk -v OFS="," '$1=$1' | sort -rt, -nk2 count_list | awk '{print $1}{print $2}' > final_list.csv
cat small_files_count.txt | awk -v OFS="," '$1=$1' | sort -rt, -nk2 small_files_count.txt | awk '{print $1}{print $2}' >> final_list.csv




