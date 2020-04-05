# 基于PDFMiner的公司章程语义分割
## 1.语义类型定义

![1](http://m.qpic.cn/psc?/fef49446-40e0-48c4-adcc-654c5015022c/90yfO.8bOadXEE4MiHsPn4iWjOvXq2aa8yYaq0okLZ7GbbaKV660n*vh7jJIIhVPItINxfkMA6MYFkk5ZbX5fA!!/b&bo=JgLWAgAAAAADB9I!&rf=viewer_4)
- chapter (章)  
上图所示中橙色方框包围左上角为chapter处为章
- section (节)  
上图所示中蓝色方框包围左上角为section处为节
- clause (条)  
上图所示中紫色方框包围左上角为clause处为条

## 2.下载
#####   为下载该项目, 请在希望保存该项目的路径启动控制台并执行如下命令:
```
git clone http://47.98.230.217:3000/Doc_SemSeg/Company-Articles-SemSeg.git
```

## 3.环境
![Image text](https://img.shields.io/badge/Python-3.6-green?style=flat)
#####   项目运行所需要的依赖包如下所示：
 - pdfminer
 - numpy
 - logzero
 - opencv-python
 - pdf2image>=1.11.0
 
#####   可以逐一安装上述环境, 也可以在进入到`pdf_analysis`之内后执行如下命令: 
```
pip install -r requirements.txt
```

## 4.配置
本项目支持通过配置的方式启动，配置文件为`conf.cfg`, 可配置的功能如下：
 - `folder`: 默认设置为./example/, 其值为待处理的pdf文件所在目录.
 - `filename`: 默认设置为all, 表示对folder目录下的所有文件做语义分割. 若指定文件则请设置为文件名称.
 - `text_level`: 默认设置为2, 表示对文字区域做二级语义分割. 若对文字区域做一级语义分割则设为1.
 - `save_image`: 默认设置为True, 表示保存语义分割结果的图片. 若不希望保存语义分割结果的图片, 请设置为False.
 - `save_text`: 默认设置为False, 表示不保存语义分析结果的JSON文件. 若希望保存语义分割结果的JSON文件, 请设置为True.

## 5.运行
```python
python main.py
```


