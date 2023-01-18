# 🌸 scripts for combining/renaming/whatever files from OpenDoc's court judgment repos
relevant opendoc repos:
- [opendoc-state-court-judgments](https://github.com/opendocsg/opendoc-state-court-judgments)
- [opendoc-family-court-and-juvenile-court-judgments](https://github.com/opendocsg/opendoc-family-court-and-juvenile-court-judgments)
- [opendoc-supreme-court-judgments](https://github.com/opendocsg/opendoc-supreme-court-judgments)

sample directory structure for reference:
```
.
├── 2022_SGDC_252
│   ├── index.md
│   └── report.md
├── 2022_SGDC_253
│   ├── index.md
│   └── report.md
├── 2022_SGDC_254
│   ├── index.md
│   └── report.md
```
I've included some sample folders of judgments here for you to try out. 

## industrious little workers
I've separated these tasks into different scripts instead of one giant script in case you want to use some of them but not the others.

```frontmatter.py```
- parses frontmatter using pyyaml
- extracts date of judgment from ```subtitle```
- adds date of judgment as ```date: YYYY-MM-DD```
  
> Issue: The content of report.md is not written with YAML so I run into problems when I combine index+report first into one file, then try to use yaml.load_all() as it says stuff like "expected \<block end>, not \<scalar>". Hence I run ```frontmatter.py``` on index.md files before running ```combine.sh```. Please let me know if you have a better idea of how to implement this such that sequence of commands isn't an issue... :")

```removestyle.sh```
- uses ```sed``` to search for a line containing ```<style>``` and delete it. I used to just delete the first line as it's the case for report.md files (style tag is in the first line), but there's the risk that I accidentally run it multiple times and delete more things. So I decided to not be lazy and use regex instead.

```combine.sh``` 
- takes a judgment folder and combines the index.md file (containing front matter) and report.md (containing the judgment's text) into one file
- names the combined file with the original folder's name (e.g. 2022_SGDC_253.md)
- deletes old folders 

```all.sh```
- just runs all of the above scripts on the current directory 


# 🍳 still cooking
- [ ] something that adds the level of court to the "tags" section of each judgment (e.g. "SGDC", "SGHC")
-  [x] removing ```<style>``` line from each report.md file
-  [ ] figure out how to read and write front matter even when both index+report.md have been combined