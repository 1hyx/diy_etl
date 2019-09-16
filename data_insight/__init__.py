# _*_ coding = utf-8 _*_
__author__ = 'hu yuxin'
# 数据库小白 突发奇想折磨一下自己
date = '2019/9/16'
# 边学习边编程而已，偶尔话痨，应该会有很多笔记

"""
自定义数据清洗和加载的方法 第一步，能够连接到所有的数据库
所以这里先写一个全能的connector，其实就是每个都写一个方法，说什么全能，全都是泪罢了。 
实在连接不上的我也没有啥办法，只能走一步算一步

入秋了，咱先拉个清单，就所有的数据库 参考自：https://zh.wikipedia.org/wiki/%E6%95%B0%E6%8D%AE%E5%BA%93
关系型数据库
MySQL
MariaDB（MySQL的代替品[2]，维基媒体基金会项目已从MySQL转向MariaDB[3]）
Percona Server（MySQL的代替品[4][5]）
PostgreSQL
Microsoft Access
Microsoft SQL Server
Google Fusion Tables
FileMaker
Oracle数据库
Sybase
dBASE
Clipper
FoxPro
foshub
非关系型数据库
BigTable（Google）
Cassandra
MongoDB
CouchDB
键值数据库
Apache Cassandra（为Facebook所使用[6]）：高度可扩展[7]
Dynamo
LevelDB（Google）
"""

# 其实有一个设想，一般etl的处理都是在本库里进行的，如果本库的处理性能不够，能不能以低代价的方式进行数据库转库，或者数据表转库
# 不希望以另外开辟内存的方式进行转库，而是一个本库给另一个库授权的机制，同时使用我们都能懂的语言

