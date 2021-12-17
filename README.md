# Hadoop Non-English Words Count per file

## The comprehensive guide to run mapreduce algorithm written in python on hadoop environment

#### In this repo for demonstration, counting of non english word is done for each english traslation of non english songs.

#### Which outputs results as below
```
"Song File Name" "Count of non-english words"
Song1 74
Song2 9
TestSong 2
Song3 45
```

#### For this songs need to be uploaded on HDFS which is hadoop distributed file system.

#### Before that you need to format and start hadoop dfs and yarn, which can be done from following commands
```
1. hdfs namenode -format -force
2. start-all.cmd
```

#### Then create directory in dfs to upload songs dataset in them
```
1. hdfs dfs -mkdir /songs
2. hdfs dfs -put D:\Data\songs / (copy local /songs folder to dfs /songs folder)
3. hdfs dfs -ls /songs 
```

#### Run mapper and reducer by specifying input and output path
##### Make sure to delete ouput directory from hdfs if its already present
```
hadoop jar D:\hadoop-streaming-3.3.1.jar -input  /songs -mapper "python D:\mapper.py" -reducer "python D:\reducer.py" -output /output/
```

#### Check output
```
hdfs dfs -ls /output/
hdfs dfs -cat /output/part-00000
```

```
Song1 74
Song2 9
TestSong 2
Song3 45
```

