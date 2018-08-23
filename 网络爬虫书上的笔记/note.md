# 1.基本库的使用
## 使用urllib
   - request: 它是最基本的HTTP请求模块,可以用来模拟发送请求.
               就像是在浏览器输入网址然后回车一样,只需要给库方法传入URL以及额外得到参数,就可以模拟实现这个过程了
   - error: 异常处理模块,如果出现请求错误,我们可以补货这些异常,然后进行重试或者其他操作保证程序不会意外终止
   - parse: 一个工具模块,提供了许多URL处理方法,比如拆分,解析,合并
   - robotparse:主要用来识别网站robots.txt文件,然后判断哪些网站可以爬,哪些网站不可以爬,用的比较少
    
## 发送请求
- 使用urllib的request模块,可以方便的实现请求的返送并得到相应
   - urlopen() 
        - 利用urlopen()方法,可以完成最基本的简单网页的GET请求抓取
        - urllib.request.urlopen(url, data=None, [timeout,]*, capath=None, cadefault=False,context=None)
        - 可以发现,除了第一个参数可以传递URL之外,还可以传递其他内容,比如data(附加的数据)、timeout(超时时间)
        - deta参数
            - data参数是可选的,如果要添加参数,并且如果它是 字节流编码格式的内容,即bytes()方法转化.
              另外如果传递了这个参数,则他的请求则不再是get方式,而是post方式
        - timeout参数
            - timeout参数用于设置超时时间,单位为秒,意思就是如果请求超出了设置的时间,还没有得到相应,就会抛出异常.
              如果不指定时间参数,就会使用全局默认时间,它支持http,https,ftp请求
   - Request
        - url参数:
            - 这是必传参数,其他都是可选参数,用于请求url
        - data参数:
            - 如果传入第二个参数,必须传bytes(字节流)类型的,如果她是字典,需要先用urllib.parse模块里的urlencode()编码
        - headers参数:
            - 他是请求头,可以在构造请求时通过headers参数直接构造,也可以通过调用请求实例的add_header()方法添加
            - 请求头最常用的用法就是通过User-Agent来伪装浏览器,默认的是python-urllib,我们可以通过他来修改浏览器,比如装成火狐
        - host参数:
            - 请求的是host或者ip地址
            - 可以加入到headers当中组成字典
        - unverifiable参数
            - 表示这个请求是否是无法验证的,默认为false,意思就是说用户没有足够的权限来选择接受这个请求的结果
        - method参数
            - 用来指示请求使用的方法,比如post,get,head,delete,put等
   