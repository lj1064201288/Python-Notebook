# 1.爬虫简历
- 爬虫定义:网络爬虫是按照一定的规则自动抓取万维网信息的程序或者脚本
- 两大特征:
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤:
    - 下载网页
    - 提取正确的信息
    - 根据一定的规则跳到另外的网页上执行上两步的操作
- 爬虫分类:
    - 通用爬虫
    - 专用爬虫(聚焦爬虫)
- Python网络包简历
    - Python2.x：urllib,urllib2,urllib3,hrrplib,httplib2,requests
    - Python3.x:urllib,urllib3,httplib2,requests
    - Python2:urllib和urllib2配合使用,或者requests
    - Python3:urllib,requests

# 2.urllib
- 包含模块
    - urllib.request:打开和读取
    - urllib.error:包含urllib.request产生的常见的错误,使用try捕捉
    - urllib.parse:包含解析url的方法
    - urllib.robotparse:解析robots.txt文件
- 网页编码问题解决
    - chardet可以自动检测页面文件的编码格式,但是,可能有误
    - 需要安装,conda install chardet
- urlopen 的返回对象
    - geturl:返回请求对象的url
    - info: 请求反馈的meta信息
    - getcode: 返回得到http code
- request.data的用法
    - 访问网络的两种方法
        - get:
            - 利用参数给服务器传递信息
            - 参数为dict,然后parse编码
        - post:
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理的
            - 我们如果想使用post信息,需要用到data参数
            - 使用post,以为着http的请求头可能需更改:
                - Content-Type:application/x-
                - Content-Lenght:数据长度
                - 简而言之,一旦更改请求,请注意其他请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成bytes格式
            - 为了更多的设置请求信息,单纯的通过urlopen函数已经不太好用了
            - 需要利用request.Request类
            
- urllib.error
    - URLError产生的原因:
        - 没网
        - 服务器连接失败
        - 不知道的指定服务器
        - 是OSError的子类
    - HTTPError,是URLError的子类
    - 两者区别:
        - HTTPError是对应的HTTP请求的返回码错误,如果返回错误码是400以上的，引发httpError错误
        - URLError对应的一般是网络出现问题,包括url问题
        - 关系区别: OSError-URLError-HTTPError
        
    
    