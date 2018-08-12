import  string, urlib2

def badu_tibeba(url,begin_page,end_page):
    for i in range(begin_page, end_page+1):
        sName = string.zfill(i,5)+'.html'
        print(正在下载第' + str(i) + '个网页，并将其存储为' + sName+'.....)
        f = open(sName,'w++')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()
        bdurl = str(raw_input(u'tieba.baidu.com/p/2296017831?pn='))
