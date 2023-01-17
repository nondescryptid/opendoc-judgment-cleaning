# Remove <style> line from the first line in each report.md file
./removestyle.sh
# add date to front matter
for dir in */; do
  python3 frontmatter.py ${dir}/index.md
done
# combine files
./combine.sh