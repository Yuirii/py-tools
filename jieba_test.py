# encoding=utf-8
import jieba
import jieba.posseg
import jieba.analyse
# jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持
# strs=["我来到北京清华大学","乒乓球拍卖完了","中国科学技术大学"]
# for str in strs:
#     seg_list = jieba.cut(str,use_paddle=True) # 使用paddle模式
#     print("Paddle Mode: " + '/'.join(list(seg_list)))
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))

# #test mode
class Person:
    name = []
    phone = []
    context = []*32
    pass

# 检测是否为地址
uu = ["辽宁", "吉林", "黑龙江", "江苏", "浙江", "安徽", "福建", "江西", "山东", "内蒙", "新疆", "西藏", "台湾", "河南", "河北", "山西", "湖北", "湖南", "广东",
      "广西", "海南", "四川", "贵州", "云南", "陕西", "甘肃", "宁夏", "青海", "北京", "上海", "重庆", "天津", "深圳" , "广州" , "西安"]
def is_Address(adstr):
    getit = 0
    for m in uu:
        if adstr.find(m) >= 0:
            getit = 1

    if getit == 1:
        return True
    else:
        return False

while 1:
    string = input('请输入：').replace('\r', '').replace('\n', '').replace('\t', '').replace(' ','').replace(',','').replace('，','')
    while string != 'q':
        string = string
    print(type(string))
    person_per = Person()
    try:
        #
        #根据词性，结巴分词提取人名和电话号码，问题在地址怎么综合。考虑不用结巴方式。
        words = jieba.posseg.cut(string)
        # print(type(words))
        # for i in words:
        #     if is_Address(i):
        #         address = ''
        #         address = i
        # print("address:", address)
        index = 0
        for word, flag in words:
            # print('%s %s' % (word, flag))
            if flag == "nr" and word!="阿玛尼":
                person_per.name = word
            if flag == "m" and len(word)==11:
                person_per.phone = word
            if flag != "nr" and len(word)!=11:
                person_per.context[index] = word
                print('%d %s' % (index, person_per.context[index]))
                index += 1
        #
        print("name",person_per.name)
        print("phone",person_per.phone)
        context1 = ''.join([str(i) for i in person_per.context])
        print("context", context1)

    except:
        print("error")
