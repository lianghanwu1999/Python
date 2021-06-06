#练习1.导入指定模块工具:from 模块名 import 指定工具名

from ceshi测试模块01 import ceshi01
from ceshi测试模块02 import ceshi02

#不同模块之间导入同名工具时，后一个会覆盖前一个工具（后一个会高亮）覆盖前一个，
# 解决方法：可以利用署名法：在工具后面加上 as 重新定义的署名
from ceshi测试模块01 import ceshi01
from ceshi测试模块02 import ceshi01 as ceshixiaogongjun

#模块搜索顺序
#导入模块不要与系统模块工具包同名，因为系统会先从工作目录中先搜索，没有才会指向系统，
# 如果定义模块名与系统模块名相同，这系统的工具会不能使用。


ceshi01()
ceshi02()
ceshixiaogongjun()