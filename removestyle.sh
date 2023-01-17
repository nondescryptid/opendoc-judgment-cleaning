# Removes first line which is the <style> tag in report.md files
# Note that sed on OSX is slightly different from Linux, and the inline edit requires an extension '' https://david-kerwick.github.io/2017-02-07-using-sed-to-delete-lines-in-a-file-on-macos/
sed -i '' '/<style>.*<\/style>/d' */report.md