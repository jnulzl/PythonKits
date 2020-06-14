## Pdf页面提取工具

	本工具可以根据输入的txt文件(具体格式说明见下面)按顺序提取并合并特定的pdf页面。

## 使用说明

- 调用命令

    打开`pdfSplitAndMerge.bat`，按如下格式输入(可直接复制进去修改需要输入的地方)：

    ```shell
    pdfSplitAndMerge.exe --input_pdf 输入pdf路径 --input_txt txt文件路径 --mode 输出模式
    ```
    
    输入:
    ```shell
    pdfSplitAndMerge.exe --input_pdf data/python_autowork.pdf --input_txt test.txt --mode 1
    ```
- 参数说明

	1 `--input_pdf`
	
	**调用命令**中`--input_pdf`后面跟的是需要提取的`pdf`文件路径，例如上述的：`data/Python编程快速上手_让繁琐工作自动化.pdf`

	2 `--input_txt`
	
  **调用命令**中`--input_txt`后面跟的是输入`txt`文件路径，例如上述的：`test.txt`(名字可随意取)，其格式说明如下：

    `test.txt`内容可以有许多行，但必须是**两列**，例如：

    ```python
  17-26 目录
  6 致谢
  4 内容提要
  8-16 前言
  28-41 第一部分
  68-82 第一部分
    ```
	
	**其中, 第一列表示页码，第二列表示该页码对应的名字**

	**注意：**

	**A: 第一列的页码只有两种写法，即:*`num`*或者*`num1-num2(num2不能小于num1)`***

	**B: 行与行之间的关系是独立的。即：排在后面行的页码不一定非要大于排在前面行的页码**

	**C: `test.txt`中的页码是从`pdf`文件首页(包括封面,封面算第1页)算起的页码**

	3 `--mode`
	
	**调用命令**中`--mode`后面跟的是输出模式:

	A: `1`表示根据`test.txt`中的顺序合并成一个`pdf`文件

	B: `2`表示根据`test.txt`中的顺序合并成一个`pdf`文件，同时对`test.txt`中第二列的每个`title`都单独生成一个`pdf`文件
