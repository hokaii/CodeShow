import pandas as pd
from apyori import apriori

def deprive_bracket_specification(trade_name):
    # 提取商品名（中文字符），从左到右，第一个中文字符开始，第一个非中文字符结束
    # unicode编码中文的范围是4e00~9fa5
    trade_name_not_specification = list()

    start = 0
    # 左边第一个中文字符开始
    for char in trade_name:
        if not ('\u4e00' <= char <= '\u9fff'):
            start += 1
        else:
            break

    # 右边第一个非中文字符结束
    for char in trade_name[start:]:
        if '\u4e00' <= char <= '\u9fff':
            trade_name_not_specification.append(char)
        else:
            break

    return ''.join(trade_name_not_specification)

if __name__ == '__main__':
    f = pd.read_csv('sales_detail.csv', encoding='utf-8', sep='\t', header=None)#打开文件
    tip_shopname = f.loc[:, [0, 5]]# 订单号列和商品名列
    tip_shopname.columns = ['tip', 'shopname']

    tip_shopname.shopname = tip_shopname.shopname.apply(func=deprive_bracket_specification)# 去除规格

    grouping_by_grocery_list = []
    for meb in tip_shopname.groupby('tip'):# 按订单号分篮
        grouping_by_grocery_list.append(list(meb[1].shopname))

    #for meb in grouping_by_grocery_list:
    #    print(meb)

    # 进行频繁项集及关联规则的发现，最大长度为5
    result = apriori(grouping_by_grocery_list, min_support=0.0002, min_confidence=0.7, min_lift=10, max_length=5)

    result_list = []
    for meb in result:# 将结果保存为列表
        result_list.append(meb)

    for meb in result_list:# 查看发现的频繁项集各项信息
       print(meb)

    with open('aprior_printout.txt', 'w') as f:#将频繁项集信息输出为txt文件
        for s_list in result_list:
            f.write(str(s_list))
            f.write('\n')

    print("End!")