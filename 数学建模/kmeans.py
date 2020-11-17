import pandas as pd
import Levenshtein
from sklearn.cluster import KMeans

# 计算商品与其他商品的编辑距离
def calculate_compile_distance(product):
    distances = []
    for meb in data:
        distances.append(Levenshtein.distance(product,meb))
    return distances

if __name__ == '__main__':
    data = []

    # 打开文件，对每一行拆分为单独的商品名加入data中
    with open('basket_row.csv', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.rstrip(',\n')
            line = line.split(',')
            for meb in line:#去重
                if meb not in data:
                    data.append(meb)

    data_F = pd.DataFrame(data)# 转化为DataFrame对象
    data_F.columns = ['shopname']
    for meb in data_F.shopname:# 计算编辑距离向量矩阵
        data_F[meb] = calculate_compile_distance(meb)
    X = data_F.drop('shopname', axis=1)# 提取向量矩阵
    estimator = KMeans(n_clusters=1900)# 设置簇数进行聚类
    estimator.fit(X)

    result = pd.DataFrame(data)# 将商品名与其类别标签整合
    result['类别'] = estimator.labels_

    result_dict = dict()# 按照类别标签为key进行分桶，分到所属的簇中
    for line in result.itertuples():
        result_dict.setdefault(line[2], []).append(line[1])

    result_list = []
    for key, value in result_dict.items():
        if len(value) > 1:# 保存商品数量大于2的簇
            result_list.append(value)

    for line in result_list:#输出聚类结果
        print(line)

    with open('kmeans_printout.txt', 'w') as f:#输出为txt文件
        for s_list in result_list:
            f.write(str(s_list))
            f.write('\n')

    print("end!")