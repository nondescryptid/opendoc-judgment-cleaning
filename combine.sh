#!/bin/bash
for dir in */; do
  # Get the subdirectory name
  subdir_name=$(basename $dir)
  # Combine the index.md and report.md files and place them in the 
  cat ${dir}index.md ${dir}report.md > ${subdir_name}.md
  # Remove folders containing the old index.md and report.md files
  rm -r ${dir}
done
