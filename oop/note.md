1.变量的命名和使用
   --在Python中使用变量时，需要遵守一些规则和指南，违反这些规则将引发错误，而指南旨在让你变下的代码更容易阅读和理解
   --1.变量名只能包含字母，数字和下划线。变量名可以字母或者下划线打头，但不能以数字打头。
   --2.变量名不能包含空格，但可使用下划线来分隔其中的单词
   --3.不要将Python关键字和函数名用作变量名，既不要使用Python保留用于特殊用途的单词，例如print
   --4.变量名应既简短又具有描述性。
   --5.慎用小写字母l和大写字母O，因为它们可能被人看作成数字1和0
   注释:
        --在大多数编程语言中，注释都是一项很有用的功能，注释能让你使用自然语言在程序中添加说明。
   字符串：
        --name.title():此函数是将头字母转换成大写
        --name.upper():此函数是将所有字母转换成大写形式
        --name.lower():此函数是将所有字母转换成小写形式
        --name.rstrip():此函数是暂时删除字符串中末尾的空白,如果要永久性删除，必须要将删除操作存储在一个变量当中
        --name.rstrip():此函数是剔除结尾的空白处
        --name.strip():此函数是剔除开头的空白处
        
3.列表
   1.列表是什么
     --列表是由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0-9或所有家庭成员姓名的列表，也可以将任何东西加入列表中，
     --其中的元素之间可以没有任何关系。鉴于列表通常包含多个元素，给列表指定一个表示复数的名称是不错的主意
     --列表的索引是从0开始的而不是1
   2.修改、添加和删除元素
        --你创建的大多数列表都是动态的，这意味着列表创建后，将随着程序的运行增删元素
        --修改列表元素
            --可以直接为列表的某一个位置（用下标确认位置）进行直接修改
        --添加列表元素
            --添加列表元素使用:
                --listname.append(元素):在列表的末尾添加一个元素
            --在列表中插入某个元素：
                --listname.insert(下标位置，元素):在下标位置的添加一个元素
            --注意：
                --元素要使用‘’包含起来
        --在列表中删除元素：
            --直接删除：
                --del listname[下标]:删除下标位置的元素
            --弹出元素删除：
                --name = listname.pop(下标位置)：将列表中的某个元素删除并存入一个变量当中
            --根据值删除元素:
                --listname.remove(元素)：指定的删除某个元素
                --注意：方法remove()只删除一个值，如果要删除的值可能在列表中多次出现，就需要使用循环来判断是否删除了这样的值。
   3.组织列表
        --在创建列表中，元素的排列顺序通常是无法预测的，因为你并非总能控制哦用户数据的分析，这虽然大多数情况下都是不可避免的，但你经常需要以特定的顺序呈现信息
        --排序：
            --listname.sort():永久性进行排序，按字母的顺序。
            --listname.sort(reverse = True):永久性对列表进行反顺序排序。
            --sorted(listname):暂时进行排序，按字母的顺序。
            --sorted(listname,reverse):暂时对列表进行反顺序排序呢
            --listname.reverse():此函数是对列表进行反顺序排序
            --len(listname):确认列表的长度
                --注意：Python计算列表时是从一开始的，因此确认长度时，应该不会吧遇到差一的错误
        --索引错误:发生索引错误却找不到解决的办法时，请尝试将列表或其长度打印出来，列表可能与你以为的截然不同，
                  在程序中对其进行处理尤其如此，通过查看列表或其他包含的元素，可帮助你找出这种逻辑错误
                  
   4.操作列表
        --遍历整个列表
            --遍历列表使用for循环：
                --for 变量名 in 列表名:
                    .......
        --使用函数range():
            --Python函数range()让你能够轻松的生成一系列的数字：
                例如：
                    --for value in range(起始值，结尾值加一)：
                        .........
            --使用range()创建数字列表:
                例如：
                    --变量名 = list(range(1,6))：
                    --变量名 = list(range(起始值，结尾值加一，间隔的值)):
                        --简单来说就是：函数range()从起始值开始数，一直加间隔值至到结尾值。
                    --注意:
                        --当遍历的时候，可以使用运算符，加减乘除，幂，取值等都可以
                            加：+, 减:-, 乘:*, 除:/, 求幂：**, 取值:%;
        -对数字进行统计：
            min(listname):找出列表中的最小值
            max(listname):找出列表中的最大值
            sum(listname):求出列表的和
                --附加猜想；
                sum(min,max):可以得出列表中最大与最小值之和
        --列表的切边:
            --要创建切片，可指定要使用的第一个元素和最后一个元素的索引：
                --例如：
                    listname = [元素]
                    print(listname[要使用的起始元素下标，结尾元素下标])
            --切片:总的来说，切片就是把A列表的元素复制到B列表的队列中，而B列表可以指定需要哪些元素;
            --如果没有指定元素，直接[:]复制，将是把所有的元素复制到了B列表当中
        --元组:
            --元组：看起来犹如列表，但是使用圆括号而不是方括号来标示的，定义元组后，就可以使用索引访问元素，就像访问列表一样
            --虽然不能修改元组的元素，但是可以为其赋值

4.if语句
    --if语句的语法:
        --if 条件表达式:
            ....
    --条件测试:
        --bool值:
            --True and False
                --解释：当条件表达式为True时，则执行该语句，当条件表达式为False时，则跳过该语句
    --程序判断:
        --在程序当中，只有真或者假。
        --检查多个条件：
            --and：
                --条件表达式 and 条件表达式：
                    当两个为真时，才为真
            --in：
                --变量名 in 列表名:查找变量是否在列表中
                --特定值 in 列表名:查找特定值是否在列表中
            --or:
                --条件表达式 or 条件表达式:
                    当一个为真时，就为真
    --if-elif-else结构:
        if 条件表达式：
            ....
        elif 条件表达式:
            ....
        else:
            ....
    --确认列表是否为空:
        if listname:
            如果为空这不执行
5.字典
    --字典的格式:
        dictname = {'键值':'对于键的说明'}
    --访问字典:
        print(dictname['键值'])
        --显示的是键值的说明
    --添加键-值对:
        a['添加的键名'] = 添加键的说明
    --修改字典的值:
        a['键名'] = 修改后的说明
    --删除键-值对:
        del dictname['键名']
            --注意：删除键后，键的说明也永远消失了
    --注意：
        --对于较长的列表和字典，大多数编译器都有以类似方式设置其格式的功能，对于较长的字典，还有其他一些可行的格式设置方式，
        --因此在你的编译器或者其他源代码中，你可能会看到稍微不同的格式设置方式.
    --遍历字典：
        --遍历字典的所有键-值对:
            key,value：                   
                for key,value in dictname.items():
                        ......
                        ......
        --遍历字典的所有键:
            key:
                for 变量名 in dictname.keys():
                        print(变量名)
        --遍历字典的所有值对:
            value:
                for 变量名 in dictname.values():
                        print(变量名)
    --嵌套:
        --字典列表:
            --可以创建多个字典后然后将字典名放入列表当中，例如:
                  dictname_one = {...}
                  dictname_two = {....}
                  dictname_three = {.....}
                  listname = [dictname_one, dictname_two, dictname_three]
            --我们还可以在字典中存储列表,例如:
                   dictname = {'键':'值对',
                                'listname':[元素1,元素2]}
            --还可以在字典中存储字典，例如:
                   dictname = {'键':{'键':'值对'}}
                   
6.用户输入和while循环：
    --函数input()的工作原理
        --函数input()让陈谷暂停运行，等待用户输入一些文本，获取用户输入后，Python将其存储在一个变量中，以方便使用
                input("提示用户需要输入" + 用户需要输入的内容）
                    --注意:print输出时，提示的内容在下一步不会执行，相当于C语言里面的print与scanf融合，当又有不同
                    --不同之处只可意会不可言传
    --使用int()来获取数值的输出:
       int():
           因为在Python里面，用户输入的任意值都会被默认为字符串，而int()可以将字符串转换为数字来进行使用
    --while循环:
        --for循环用于针对集合中的每个元素的一个代码块，而while循环不断运行，直到指定的条件不满足为止
        --while让用户选择退出，例如:
                while num != 'quit':
                    .....
             --此程序如果没有输出quit，则无限循环
        --while使用标志，例如:
                while 条件表达式或者变量:
                    .....
                --只要条件表达式或者变量为True时，则循环，当为False时，者结束循环
                --注意：循环内部可以添加指定条件使条件表达式或者变量为True或者为假False  
    --break：
        break是无条件退出循环，可以用于while与for，break只能结束上一个执行的循环，而且是包含break之内的。
    --continue:
        要返回到循环的开头，并根据天剑测试结果决定是否继续执行循环，可使用continue语句，他不想break语句那样不再执行以下的代码并退出整个循环
    --使用while循环来处理列表和字典:
        --for循环是一种遍历列表的有效当时，但在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素。
        --要在遍历列表的同事对其进行修改，可使用while循环，通过将while循环的同列表和字典结合起来使用，可收集、存储组织大量输入，供以后查看和显示
7.函数：
    --函数是带名字的代码块，用于完成具体的工作
    --要执行函数定义的特定任务，可调用函数，函数可以解决多出循环的情况，可使你无需反复编写完成该任务的代码，而只需要调用该函数即可
    --定义函数:
        def 函数名:
            ...
    --向函数传递信息:
        变量名 =  函数名称()
    --实参与形参:
        def 函数名(形参):
            ...
        变量名 = 函数名称(实参)
    --传递实参：
        --鉴于函数的定义可能包含多个形参，因此函数调用中也可以包含多个实参。向函数传递实参等等方式有很多，可使用位置实参。
        --这要求实参的顺序与形参相同，也可以使用关键字实参，其中每个实参都由变量名和值组成，还可以使用列表和字典
    --位置实参:
        --你调用函数时,python必须将函数调用中的每个实参都关联到函数定义中的一个形参，为此最简单的关联方式是基于实参的顺序，这种关联方式被称为位置实参
        --def functionname(形参1，形参2):
            ......
        变量名 = functionname(实参1，实参2)
            --注意：如果是：
                   def functionname(形参1，形参2)
                        ....
                    变量名 = functionname(实参2，实参1)
                    将会出错，或者得到的不是你预想的结果
    --关键字实参:
        --关键字实参是传递给函数的名称-值对，直接让实参与形参一一对应的关联起来，传递时就不会混淆
        --def functionname(形参1,形参2):
                ....
        变量名 = functionname(实参2='指定的实参',实参1='指定的实参')
    --默认值:
        --编写函数时，可给每个形参指默认值，在调用函数中给形参提供了实参时，Python将使用指定的实参值，否者将使用形参的默认值。
        --使用默认值可简化函数调用，还可以清楚地指出函数的典型用法
    --注意:使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行，使用对你来说最容易理解的调用方式即可。
    --return返回值:
        --函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或者一组值。
        例子:
            def functionname()；
                ...
                return 变量、布尔值或者表达式
        --return也可以通过函数的内建方式返回字典或者列表。
    --传递任意数量的实参:
        --例子：
            def functionname(*topping)
                ....
             变量名 = functionname(任意实参,也可以多个)
    --结合使用位置实参和任意数量实参:
        --例子:
            def functionname(size, *topping):
                    ....
            变量 = functionname(size,任意实参或者多个实参)
            --注意：任意形参必须写在最后面，否者会出错
    --将函数存储在模块当中:
        --导入整个模块:
            --要让函数导入，首先要创建模块
                --要在编写程序的文件当中创建一个模块：
                    --例如：创建一个名为making_pizza.py的模块里面编写程序，在此文件当中创建一个pizza.py的文件
                        调用模块:
                            import pizza
                            .....
                            .....
        --import module_name:调用模块中的某个函数
        --from module_name import function_name: 调用某个模块中的函数
        --from module_name import function_name_0,function_name_1:调用某个模块中的多个函数
        --from module_name import function_name as fn:使用as给函数指定取名
        --import module as m:使用as给模块指定取名
        --from module import *:导入模块中所有函数
8.类与面向对象程序设计语言
    --面向对象编程是最有效的软件编写方法之一，在面向对象编程中，你编写表示现实中的事物和情景的类，并基于这些类来创建对象。
    --编写类时，你定义一大类对象都有的通用行为，基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性
    --使用面向对象编程可模拟现实情景，其逼真程度达到了令人惊讶的地步
    --根据类来创建对象被称为实例化，这让你能够使用类的实例。
    --创建类和使用类:
        class 类名():
            def __init__(self,...):
                ...
                ...
            def sit(self):
                ...
            def roll(self):
                ....
        对象 = 类名('参数１','参数2', ...)
    --方法__init__()
        --__init__是一个特殊的方法，每当根据类名创建新实例时，Python都会自动的运行它。
        --在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突
    -根据类创建实例:
        --可将类视为有关如何创建实例的说明:
        --要访问属性，可以使用句点表示法
            实例 = 类名
            实例.属性 = self.属性
        --调用方式
            要调用方法，可指定实例的名称和调用的方法，并用句点分隔他们。
            这种语法很有用，如果给属性和方法指定了合适的描述性名称
                --例如
                    name,age,sit()和roll_over()
            即便是从未见过的代码块，我们也能轻松的推断出她是做什么的。      
    --创建多个实例:
        --可按需求根据类创建任意数量的实例。
    --使用类和实例:
        __init__()这个方法的第一个形参为self，方法__init__()接受形参的值，并将它们存储在根据这个类创建的实例的属性中
        --可以直接使用self:
            实例.属性 = self.属性
    --给属性指定默认值:
        --类中的每个属性都必须有初始值，哪怕这个值是０或空字符串。
        --在有些情况下，如设置默认值时，在方法__init__()内指定这种初始值是可行的，如果你对某个属性这样做了，就无需包含为它提供初始值的形参
        --例如:
            __init__(self, 属性1, 属性2, ...):
                self.属性1 = 属性1
                self.属性2 = 属性2
                self.属性3 = 0
    --修改属性的值:
        --可以以三种不同的方式修改属性的值:
            --直接通过实例进行修改
                要修改属性的值，最简单的方式是直接访问它
                   例如:
                        实例 = 类名('参数１','参数2', ...)
                        实例.属性 = 5
                有时候需要想这样直接访问属性，但其他时候需要编写属性进行更新的方法
            --通过方法进行设置
                如果有更新属性的方法，将大有脾益，这样就无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新
                    例如:
                         类():
                            方法(self,属性):
                                self.属性 = 属性
            --通过方法进行递增
                有时候需要将属性值递增到特定的量,而不是将其设置为全新的值.
                    例如:
                        类()：
                            方法(self,属性):
                                self.属性 += 属性
    --注意:
        你可以使用各类于上面的方法来控制用户修改属性值的方式，但能够访问程序的人都可以通过直接访问属性来将修改任何值.
        要确保安全，处理进行检查外，还需特别注意细节.
    --继承
        --编写程序的时候，并非总是要从空白开始.
        --如果需要编写类是另一个现成类的特殊版本,可使用继承.
        --一个类继承另一个类时,它将自动获得另一个类所有的属性和方法.
        --原有的类称为父类,而新类被称为子类.
        --子类继承其父类所有的属性和方法,同时还可以定义自己的属性和方法.
        --子类的方法__init__()
            创建子类的实例时,python首先需要完成的任务是个父类的所有属性赋值,为此,子类的方法__init__()需要父类施以援手
            父类必须包含在当前文件中,且位于子类前面,在定义子类的时候必须在括号内指定父类的名称.
            方法__init__()接受创建子类实例所需的信息
        --特殊函数super():
            super()是一个特殊的函数,它可以帮助Python将子类与父类关联起来
            父类也被称为超类,名称super因此得名
            在python2.7中
            函数super()需要两个实参:
                子类名的对象self,为帮助Python将父类与子类关联起来，这些实参必不可少的。
        --给子类定义属性和方法
            让一个类继承另一个类后,可添加区分子类和父类所需的新属性和方法
        --重写父类的方法:    
            对于父类的方法,只要它不符合子类模拟的实物的行为,都可以对其进行重写.
            为此,可在子类中定义一个这样的方法,即它与要重写的父类方法同名.
            这样，python将不会考虑这个父类方法,而只关注你在子类中定义的相应方法
        --将实例用作属性:
            使用代码模拟实物时,你可能会发现自己给类添加的细节越来越多:
                属性和方法清单以及文件都越来越长
            在这样的情况下,可能需要将类的一部分作为一个独立的类提取出来,可以将大型类拆分成多个协同工作的小类
    --导入类:
        --导入单个类语法:
            from modulename import class
        --导入类是一种有效的编程方式.如果在程序中包含整个类是很长.
        --通过这个类移到一个模块中,并导入该模块，依然可以使用其所有功能,但主程序文件变得整洁而易于阅读了.
        --还能让你将大部分逻辑存储在独立的文件中,确定类像希望等等那样工作后,就可以不用管这些文件,而专注与主程序的高级逻辑了
    --在一个模块中存储多个类
        --虽然同一个模块中的类之间应存在某种相关性,但可根据需要在一个模块中存储任意数量的类
    --从一个模块中导入多个类:
        --导入多个类的语法:
            from modulename import class1, classs2, ...  
    --导入整个模块:
        --导入整个模块语法:
        import module
        --导入模块后,可以使用据点表示访问需要的类,这种导入方法很简单,代码也易于阅读
    --导入所有模块中的所有类:
        --导入模块中的所有类语法:
            from modulename import *
        --这种方式不推荐
--9.文件和异常:
    --文件和保存数据可让你的程序使用起来更加容易,用户将能够选择输入什么样的数据,以及在什么时候输入.
    --用户使用你的城西做一些工作后,可将程序关闭,以后再接着往下做.
    --异常可以应对文件不存在的情形,以及处理其他可能导致程序崩溃的问题,可以使程序在面对错误的数据是更健壮.
    --读取整个文件:
        --读取文件的语法:
            with open('文件名.文件类型') as 对象:
                变量 = 对象(object).read()
        --函数open():
            函数open()接受一个参数,要打开的文件名称.
        --关键字with在不在需要访问文件后将其关闭.
            --正常情况下时候open()函数后要使用close()函数进行关闭文件,否则会溢出,但是with关键字可以完全替代close()函数.
        --read()函数:
            read()函数到达文件末尾是返回一个空字符串,而将这个空字符串显示出来是就是一个空行,
            要删除末尾的空行,可在print语句中使用rstrip()
    --文件路径:
        --文件路径语法:
            with open('directory/filename') as file_object
            --注意:
                Linux系统是'/',而Windows是'\'
                另外,由于反斜杠在python中被视为转义标记,为在Windows中确保万无一失,应以原始字符串的方式指定路径,即在开头的单引号前加上r
    --逐行读取:
        --读取文件时,常常需要检查其中的每一行:可能要在文件中查找特定的信息,或者要以某种方式修改文件中的文本.
            还可以这样读取:
                filename = '文件名.文件类型'
                with open(filename) as object:
    --创建一个包含文件各行内容的列表:
        --使用关键字with时,open()返回的文件对象只在with代码块内可用.
        --如果要在with代码块外访问文件的内容,可在with代码块内将文件的各行存储在一个列表中,并在with代码外使用该列表:
            可以立即处理文件的各个部分,也可推迟到程序后面再处理
        --方法reading():
            从文件中读取每一行,并将其存储在一个列表中.
        --注意:
            读取文本文件时,Python将其中的所有文本都解读为字符串.如果你读取的是数字,并要将其作为数值使用.
            就必须使用函数int()将其转换为整数,或使用float()函数转换成浮点型.
    --文件的操作:
        --写入空文件夹语法：
            filename = '文件名.文件类型'
            with open('filename', 'w') as object
            object.write("内容")
        --读取文件的语法:
            filename = '文件名.文件类型'
            with open('filename', 'r') as object
        --在文件末尾追加数据:
            filename = '文件名.文件类型'
            with open('filenam', 'a') as object
        --以二进制写入文件与二进制读取文件:
            filename = '文件名.文件类型'
            with open('filename', 'wb') as object
            with open('filename', 'rb') as object
    --异常:
        --异常是使用try--except代码处理的.
        --格式语法:
            try:
                需要执行的语句
                如果没有异常,直接执行
                如果出现异常,异常从当前模块中扔出去尝试解决异常
            except 异常类型1:
                解决方案1:
            except　异常2,异常3,...:
                解决方案2
                解决方案3
            except 所有异常:
                解决方案
            else:
                如果没有异常,执行
            finally:
                不管有没有异常都要处理的语句
        --注意:
            出except以外,必须存在一个,else跟finally有没有都可以
        ZeroDivisionError:表示０不能作为除数
        FileNotFoundError:表示文件未找到
        AssertError:表示断言失败
        SyntaxError:表示语法错误
        NameError:表示访问一个不存在等等变量
        RuntimeError:运行错误
        TypeError:类型错误
        SystemError:系统编译错误
        ValueError:传入一个无效的参数
        OsError:系统打开错误
        KeyError:表示查找一个不存在的键
        ImportError:模块导入错误
        AttributeError:访问未知的属性错误
    --分析文本:
        方法split():
            以空格为分隔符将字符串拆成多个部分,并将这些部分都存储到一个列表中.
            结果是一个包含字符串中所有单词的列表,虽然有些单词可能包含标点.
    --存储数据:
        模块json:
            函数json.dump(): 
                语法:
                    json.dump('file','object')
                作用:
                    将数据对象存储到文件中,以json类型进行保存
            函数json.load():
                语法:
                    对象 = json.load(filename)
                作用:
                    读取文件中的数据并存储到对象中
    重构:
        重构可以让代码更加清晰,更易于理解,更容易扩展.
--10.测试代码:
    --使用python模块unittest中的工具来测试代码,核实一系列输入都将得到预期的输出.
    --测试函数:
        --单元测试:
            单元测试用于核实函数的某个方面没有问题,测试用例是一组单元测试,这些单元测试一起核实函数在各种情形下行为都符合要求.
            良好的测试用例考虑到了函数可能收到等等各种输入,包含针对所有这些情形的测试.
        --全覆盖式测试:
            用例包含一整套单元测试,涵盖了各种可能的函数使用方式.
            对于大型项目,要实现全覆盖可能很难,通常最初只要针对代码重要的行为编写测试即可,等项目被广泛使用时在考虑全覆盖
        --模块unittest：
            要为函数编写试用例,可先导入模块unittest以及要测试的函数,在创建一个继承unittest.TestCase的类,并编写一系列方法对函数行为的不同方面进行测试
            语法:
                import unittesr
                from filename　import function_name
                    class_name(unittest.TestCase):
                        测试方法:
                            对象 = 被测试函数(被测试的内容)
                    unittest.main()
            用法:
                首先要导入模块unittest和要测试的函数,在创建一个类,用于包含一些列针对函数的单元测试.
                在创建一个方法,用于测试函数的一个方面,并存储在对象里面进行返回.
                在使用unttest.assertEqual的一个功能:一个断言方法,断言方法用来合适得到的结果是否与期望的结果一致.
            如果测试成功:
                者会显示Ran 1 test in 0.000s  ok
            如果测试失败:
                者会显示Ran 1 test in 0.000s  FAILED(error=1)
    --测试类:
        Python在unttest.TestCase类中提供了很多断言方法.
        断言方法检查人为应该满足条件的是否确实满足,如果该条件满足,你对程序行为的假设就得到了确认,就可以确信其中没有错误.
        如果认为应该满足的条件实际上不满足,Python将引发异常
        unittest module中的断言方法:
            assertEqual(a,b)                   核实 a == b
            assertNotEqual(a,b)　               核实　a != b
            assertTrue(x)                       核实x为真
            assertFalse(x)                      核实x为假
            assertIn(item,list)                 核实item在list中
            assertNot(iten,list)                核实item不在list中
    --方法setUp():
        unittest.TestCase的类中包含了方法setUp(),可以只需创建这些对象一次,并在每个测试方法中使用它们.
        方法setUp()只做两件事,创建一个调查对象,创建一个答案列表.
            存储这两样东西的变量名包含前缀self(即存储在属性中),因此可在类的任何地方使用.
            这样让两个测试方法都更简单,因为它们都不用创建调查对象和答案.
    --注意:
        运行测试用例时,每完成一个单元测试,Python都打印一个字符:测试通过时打印一个据点;测试引发错误是打印一个E;测试导致断言失败时打印一个F
        这就是你运行测试用例时,在输出的第一行中看到的句点和字符数量各不相同的原有.
        如果测试用例包含很多单元测试,需要运行很长时间,就可通过观察这些结果来获悉有多少个测试通过了
        
        
        