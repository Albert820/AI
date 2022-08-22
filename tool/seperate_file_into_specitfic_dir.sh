#!/bin/zsh

root_dir=$(pwd)
#echo $root_dir
imagedir="$root_dir/image"
labeldir="$root_dir/label"
yamldir="$root_dir/yaml"
label_viz_dir="$root_dir/label_viz"

### Check for dir, if not found create it using the mkdir ##
[ ! -d "$imagedir" ] && mkdir -p "$imagedir"
[ ! -d "$labeldir" ] && mkdir -p "$labeldir"
[ ! -d "$yamldir" ] && mkdir -p "$yamldir"
[ ! -d "$label_viz_dir" ] && mkdir -p "$label_viz_dir"

search_dir=$(pwd)

#echo $labeldir

for entry in "$search_dir"/*
do 
#   echo $entry
   image_no=$(echo "$entry" | awk -F'/' '{print $8}')
#   echo $image_no
   cp "$entry/label.png" "$labeldir"/"${image_no}.png"
   cp "$entry/img.png" "$imagedir/${image_no}.png"
   cp "$entry/info.yaml" "$yamldir/${image_no}.yaml"
   cp "$entry/label_viz.png" "$label_viz_dir/${image_no}.png"
#  echo "$entry"
done

#labelme_json_to_dataset ./*
