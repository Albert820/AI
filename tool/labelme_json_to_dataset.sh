#!/bin/zsh

search_dir=/home/cheng/ZED_lab/20220217/svo_left_json
for entry in "$search_dir"/*
do
   labelme_json_to_dataset $entry
#  echo "$entry"
done

#labelme_json_to_dataset ./*
