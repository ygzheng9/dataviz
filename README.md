# dataviz
R, python, D3 for data visualization

## word cloud --- 2015/06/07
1. jiebaR:
    + input: single document for analysis
    + output: all splited word, have duplication, next step will count
2. python:
    + output: each word with count, csv for D3 comsume
3. D3:
    + d3.csv: read csv, the first line is the structure.
    + word_cloud
    + tool_tips


## plant chrod --- 2015/06/07
1. generate relation
    1. pivot(comp, vendor, log(amt))
    2. calculate the distance -- condensed
    3. squared distance
    3. turn distance opposit to relation
    5. save to txt file
2. draw chrod
    1. trun txt file to js object
    2. fire chrod


## plant cluster --- 2015/06/07
1. calculate plant distance based on (vendor count, log(po count), log(amt))
2. calculate linkage and draw dendrogram
    1. 82 too much
    2. sort by amt, and only using top 20
3. cluster info: fcluster, leaves_list


## vendor amount -- 2015/06/07
1. po count vs amt
2. log(po count) vs amt
3. vendor count vs amt
4. log(vendor count) vs amt

