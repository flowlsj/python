# encoding=utf-8
from io import open
f = open("chinese.txt", 'wt', encoding = "utf-8")
f.write(u"这是中文测试")
f.close()

text = open("chinese.txt", encoding = "utf-8").read()
print text
