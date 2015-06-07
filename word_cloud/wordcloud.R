library("jiebaR")

##  接受默认参数，建立分词引擎
mixseg = worker()

##  相当于：
##       worker( type = "mix", dict = "inst/dict/jieba.dict.utf8",
##               hmm  = "inst/dict/hmm_model.utf8",  ### HMM模型数据
##               user = "inst/dict/user.dict.utf8") ### 用户自定义词库


mixseg <= "江州市长江大桥参加了长江大桥的通车仪式"

## 相当于 segment( "江州市长江大桥参加了长江大桥的通车仪式" , mixseg ) 
## 或者 mixseg["江州市长江大桥参加了长江大桥的通车仪式"]


mixseg <= "./internet.txt" 

## segment( "./internet.txt" , mixseg )