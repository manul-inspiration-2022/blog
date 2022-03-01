---
title: "Data Storage Formats"
date: 2022-03-01T10:00:00+07:00
categories:
  - blog
tags:
  - avro, ORC, parquet, json, protobuf
  - format file
  - bigdata
  - storage
  - data engineer
---
In this introduction, we will have an overview of the pros and cons of several some file formats (Protobuf, Avro, Parquet, ORC). Purpose use with some the ecosystem: Apache Kafka, S3 (Selector, Athena, ... ), Apache Hive, Apache Spark (Python, Scala).


- [*I. Overview*](#i-overview)
- [*II. Pros and cons for some file formats*](#ii-pros-and-cons-for-some-file-formats)
  - [**1. Avro**](#1-avro)
      - [***Advantages:***](#advantages)
      - [***Disadvantages:***](#disadvantages)
  - [**2. Protobuf**](#2-protobuf)
      - [***Advantages:***](#advantages-1)
      - [***Disadvantages:***](#disadvantages-1)
  - [**3. Parquet**](#3-parquet)
      - [***Advantages:***](#advantages-2)
      - [***Disadvantages:***](#disadvantages-2)
  - [**4. ORC File**](#4-orc-file)
      - [***Advantages:***](#advantages-3)
      - [***Disadvantages:***](#disadvantages-3)
- [*III. Comparison*](#iii-comparison)
    - [*1. Grid comparison*](#1-grid-comparison)
      - [**References from the posts:**](#references-from-the-posts)
      - [**Compare based on the needs of the project:**](#compare-based-on-the-needs-of-the-project)
      - [**Compare based on the needs of the project - Json Vs Avro:**](#compare-based-on-the-needs-of-the-project---json-vs-avro)
    - [*2. Best Practices of File Storage*](#2-best-practices-of-file-storage)
      - [**Benefits of Choosing Right Storage Format**](#benefits-of-choosing-right-storage-format)
      - [**Best Practices of Hadoop File Storage**](#best-practices-of-hadoop-file-storage)
- [*IV. References*](#iv-references)

# *I. Overview*

---

Currently, we use many types of format to store data in programs and systems such as: some standard file formats (TXT, CSV, TSV, ... ), formats used in big data (ORC, RC Files, Parquet, ... ) and to exchange data between services (Json, XML, Thrift, Protocol Buffers, ... ).
<br>
In this introduction, we will have an overview of the pros and cons of several some file formats (Protobuf, Avro, Parquet, ORC). Purpose use with some the ecosystem: Apache Kafka, S3 (Selector, Athena, ... ), Apache Hive, Apache Spark (Python, Scala).

---

# *II. Pros and cons for some file formats*

## **1. Avro**

**Introduction:**

    Apache Avro was released by the Hadoop working group in 2009. It is a remote procedure call and data serialization framework developed within Apache’s Hadoop project. It uses JSON for defining data types and protocols, and serializes data in a compact binary format.

[See more](https://avro.apache.org/docs/current/index.html)

**Script example for quick start:**

* [Apache Avro# 1.8.1 Getting Started (Python)](https://avro.apache.org/docs/1.8.1/gettingstartedpython.pdf)
* [Kafka - Nodejs - Avro - Schema Registry](https://www.npmjs.com/package/kafka-node-avro)

#### ***Advantages:***

* Schema evolution.
* Avro formatted files are splittable and compression formats such as snappy.
* Rich data structures.
* A compact, fast, binary data format.
* Supported by RPC.
* Avro stores the schema in the header of the file so data is self-describing.
* Supported by the Hadoop ecosystem (HDFS, Hive, Sqoop, MapReduce, ... )
* Supported by AWS Athena.

#### ***Disadvantages:***

* Non-human readability, too hard to debug it.
* No supported by S3 Select.

  
---

## **2. Protobuf**

**Introduction:**

    Protocol Buffers (protobuf) are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data. You only need to define Schema for data once and then you can use it in mant languages.

[See more](https://developers.google.com/protocol-buffers/docs/overview)

#### ***Advantages:***

* Schema evolution.
* Support for many languages.
* Define schema once, use many languages.
* Attributes are identified by id.
* Speed for write/read is fast.
* Simpler, faster, smaller in size.
* RPC support.

#### ***Disadvantages:***

* Non-human readability, too hard to debug it.
* Doesn't support MapReduce.
* Do not support internal compression of records.
* Not splittable.
* No supported by S3 Select.

---

## **3. Parquet**

**Introduction:**

    Launched in 2013, Parquet was developed by Cloudera and Twitter to serve as a column-based storage format, optimized for work with multi-column datasets. Parquet to make the Advantages: of compressed, efficient columnar data representation available to any project in the Hadoop ecosystem.

[See more](https://parquet.apache.org/documentation/latest/)

#### ***Advantages:***

* Schema evolution.
* Parquet formatted files are splittable and highly compressed.
* Parquet is a columnar format. Only required columns would be fetched/read, it reduces the disk I/O.
* Schema travels with the data so data is self-describing.
* Good support for Spark, MapReduce, Hive, Pig, Impala, Crunch.
* Supported by S3 Select, AWS Athena.

#### ***Disadvantages:***

* Non-human readability, too hard to debug it.
* No supported by Kafka.
* Parquet does not always have native support in other tools other than Spark.
* The column-based design, so slower to write that other column formats.

---

## **4. ORC File**

**Introduction:**

    The Optimized Row Columnar (ORC) file format provides a highly efficient way to store Hive data. It was designed to overcome limitations of the other Hive file formats. Using ORC files improves performance when Hive is reading, writing, and processing data.

[See more](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC)

#### ***Advantages:***

* Schema evolution beacause metadata stored using Protocol Buffers.
* ORC formatted files are splittable and highly compressed.
* High compression rates (ZLIB).
* Schema travels with the data so data is self-describing.
* Compatible on HiveQL.
* Supported by AWS Athena.

#### ***Disadvantages:***

* Non-human readability, too hard to debug it.
* No supported by S3 Select, Kafka.

---

# *III. Comparison*

### *1. Grid comparison*

#### **References from the posts:**

![](https://2s7gjr373w3x22jf92z99mgm5w-wpengine.netdna-ssl.com/wp-content/uploads/2018/05/Nexla-File-Format.png)

#### **Compare based on the needs of the project:**

|                                                      |                           Protobuf                            |                                            Avro |                        Parquet |                  ORC |                                      Json |
|------------------------------------------------------|:-------------------------------------------------------------:|------------------------------------------------:|-------------------------------:|---------------------:|------------------------------------------:|
| Supported by (Kafka, Hive, Spark, S3 Select, Athena) |                             Kafka                             |                      Kafka, Hive, Spark, Athena | Hive, Spark, Athena, S3 Select | Hive, Spark, Athena, | Kafka, Hive, Spark, S3, Athena, S3 Select |
| Schema evolution                                     |                              Yes                              |                                             Yes |                            Yes |                  Yes |                                        No |
| Schema (Store schema, S3 support)                    | File schema .proto <br> Generate for language - store to file | File .avsc <br> Schema and schema in the footer |      schema in the footer <br> | schema in the footer |                                        No |
| Reshifh load support                                 |                              No                               |                                             Yes |                            Yes |                  Yes |                                       Yes |
| Python/Nodejs/Scala client lib                       |                              Yes                              |                                             Yes |                            Yes |                  Yes |                                       Yes |
| Human-readable                                       |                              No                               |                                              No |                             No |                   No |                                       Yes |
| Compression                                          |                             Good                              |                                            Good |                           Good |            Excellent |                                       Bad |
| Column or Row                                        |                              All                              |                                             Row |                         Column |               Column |                                       All |
| Store size                                           |                             Small                             |                                           Small |                          Small |           Very Small |                                     Large |

#### **Compare based on the needs of the project - Json Vs Avro:**

Data: sdk_log

| Num records | Json size (MB) | Avro size (MB) | % Reduce | Read/Write Json (s) | Read/Write Avro (s) |
|-------------|----------------|----------------|----------|---------------------|---------------------|
| 45813       | 79.8           | 47.9           | 40.01    | 5.06/0.88           | 7.74/0.0009         |
| 108265      | 137.5          | 80.4           | 41.38    | 7.86/2.42           | 16.79/0.000637      |
| 144418      | 169.2.7        | 93.4           | 44.77    | 9.58/3.89           | 24.33/0.000896      |
| 251096      | 319.2          |                |          |                     |                     |


### [*2. Best Practices of File Storage*](https://www.xenonstack.com/insights/what-is-file-storage-format/)

#### **Benefits of Choosing Right Storage Format**

* Faster read times
* Faster write times
* Split files
* Schema evolution support (allowing you to change the fields in a data set).
* Advanced compression support (compress the files with a compression codec without sacrificing these features).

#### **Best Practices of Hadoop File Storage**

* When the need to accessing an only a small subset of columns then used a columnar data format.
* When necessary to obtaining many columns then used a row-oriented database instead of a columnar database.
* If schema changes over time then use Avro instead of ORC or Parquet.
* If need to perform query then use ORC or Parquet instead of Avro.
* If need to perform column add operation then use Parquet instead of ORC.

# *IV. References*

* https://parquet.apache.org/documentation/latest/
* https://avro.apache.org/docs/current/index.html
* https://developers.google.com/protocol-buffers/docs/overview
* https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC
* https://luminousmen.com/post/big-data-file-formats
* https://www.oreilly.com/library/view/hadoop-application-architectures/9781491910313/ch01.html#HDFS_schema_design
* https://blog.clairvoyantsoft.com/big-data-file-formats-3fb659903271
* https://www.xenonstack.com/insights/what-is-file-storage-format/
* https://medium.com/@oswin.rh/parquet-avro-or-orc-47b4802b4bcb
* ... 

