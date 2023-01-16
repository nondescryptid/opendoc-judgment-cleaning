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
## industrious little workers
```combine.sh``` 
- takes a judgment folder and combines the index.md file (containing front matter) and report.md (containing the judgment's text) into one file
- names the combined file with the original folder's name (e.g. 2022_SGDC_253.md)
- deletes old folders 


# 🍳 still cooking
- something that adds the level of court to the "tags" section of each judgment (e.g. "SGDC", "SGHC")
- removing ```<style>``` bits 