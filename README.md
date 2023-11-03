# hadoop-word-counter

Simple Word Counter using Hadoop MapReduce.

## Requirements

1. [Python 3](https://www.python.org/)
2. [Apache Hadoop](https://hadoop.apache.org/releases.html)
3. [Apache Hadoop Streaming Library](https://jar-download.com/artifacts/org.apache.hadoop/hadoop-streaming/3.3.6)

## How to Use

1. Copy the sample data directory that contains many `txt` files for word counting to HDFS. Make sure to replace `/home/hadoop` with the actual location in your local machine.

```sh
hdfs dfs -copyFromLocal /home/hadoop/text_data /user/hadoop/text_data
```

2. Run this command to run Hadoop MapReduce.

```sh
hadoop jar $HADOOP_HOME/lib/hadoop-*streaming*.jar \
-file /home/hadoop/mapper.py -mapper /home/hadoop/mapper.py \
-file /home/hadoop/reducer.py -reducer /home/hadoop/reducer.py \
-input /user/hadoop/text_data/* -output /user/hadoop/result_output
```

3. Check the result.

```sh
hdfs dfs -cat result_output/part-00000
```
