# 概述

这是做毕业去向网站的时候整理的数据，高校位置部分调用百度地图API+人工筛查，包含了中国2820所高校、世界大部分国家和地区、中国主要行政区的经纬度位置信息。

# 文件说明

所有文件都放在`data`文件夹中，命名都比较直白了。

* `university_*.json`: 大陆大学的信息
* `country_*.json`: 国家和地区信息
* `city_*.json`: 大陆行政区信息

还有一些中间文件、脚本之类的。


# 注

* [大陆大学数据来源](https://github.com/codeudan/crawler-china-mainland-universities)
* [国家和地区数据来源](http://www.mohrss.gov.cn/SYrlzyhshbzb/zhuanti/jinbaogongcheng/Jbgcbiaozhunguifan/201112/t20111206_47429.html)
* [国家经纬度数据来源](https://www.kaggle.com/eidanch/counties-geographic-coordinates)
