#!/bin/bash
#depth_level=$1
#base_path=$2

rm base_path.txt
rm small_files_count.txt
rm final_list.csv
rm small_file_list.txt
# list all folders under given  base path and store it in  base_path.txt
hdfs dfs -ls  /user/hive/warehouse/*/ | awk -F / '/^d/' | awk '{print $8}' >> base_path.txt

# Loop every line in base_path.txt and filter small files  recursively (with respect to given threshold size -64MB)

while IFS="" read -r line || [ -n "$line" ]
do

        file_name=$(hdfs dfs -ls -R ${line} | awk '{if($5<3145728) print $8}')
        echo "$file_name" >> small_file_list.txt
#write the small file names in small_file_list.txt
        count=$(hdfs dfs -ls -R ${line} | awk '{if($5<3145728) print $8 && $1 !~ "^d"}' | wc -l)
        echo "$line","$count"  >> small_files_count.txt
# write file path and count of files under every folder in out
done < base_path.txt


# echo  "${count_per_folder}" | awk -v OFS="," '$1=$1' | sort -rt, -nk2 count_list | awk '{print $1}{print $2}' > final_list.csv
cat small_files_count.txt | awk -v OFS="," '$1=$1' | sort -rt, -nk2 small_files_count.txt | awk '{print $1}{print $2}' >> final_list.csv



/user/hive/warehouse/dump_1/partition_1,1
/user/hive/warehouse/dump_1/partition_2,1
/user/hive/warehouse/dump_2/partition_1,1
/user/hive/warehouse/dump_2/partition_2,1
/user/hive/warehouse/dump_3/partition_1,1
/user/hive/warehouse/dump_3/partition_2,1
hadoop@ubuntu:~/scripts$
hadoop@ubuntu:~/scripts$
hadoop@ubuntu:~/scripts$
hadoop@ubuntu:~/scripts$ cat small_file_list.txt
/user/hive/warehouse/dump_1/partition_1/googleplaystore.csv
/user/hive/warehouse/dump_1/partition_2/googleplaystore.csv
/user/hive/warehouse/dump_2/partition_1/googleplaystore.csv
/user/hive/warehouse/dump_2/partition_2/googleplaystore.csv
/user/hive/warehouse/dump_3/partition_1/googleplaystore.csv
/user/hive/warehouse/dump_3/partition_2/googleplaystore.csv
hadoop@ubuntu:~/scripts$ nano test.sh

