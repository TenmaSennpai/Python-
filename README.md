# Python-
Python 连接数据库
1.	安装Access 2019，选64位，安装后激活，https://msdn.itellyou.cn/  
2.	安装ODBC驱动工具，选64位，安装  
Microsoft Access Database Engine 2016 Redistributable  
https://www.microsoft.com/en-us/download/details.aspx?id=54920
![Image](https://raw.githubusercontent.com/TenmaSennpai/PythonAccess/master/1.png)
![Image](https://raw.githubusercontent.com/TenmaSennpai/PythonAccess/master/2.png)
3.	安装pyodbc，打开powershell输入「pip install pyodbc」
4.	运行control进入「控制面板-管理工具-ODBC数据源（64位）-驱动程序」  
    记下需要的驱动程序的名称，之后会作为「DBdriver」的值  
    新建一个数据库文件，并创建一个表，文件的绝对路径作为「DBfile」的值  
5.	然后根据之前的信息更改python源代码，注意SQL里字符串用单引号「‘’」来表示

