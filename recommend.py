import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import string
import matplotlib
import warnings
# label = {"a": -1, "b": -1, "c": -1}  # 代表三个选项分别对应的小类
# cls_relation = [[0, 1], [2, 3], [4], [5, 6, 7]]


# 忽略 MatplotlibDeprecationWarning
warnings.filterwarnings("ignore", category=matplotlib.MatplotlibDeprecationWarning)


# 根据概率推荐k个
def random_select_indices(P, K):
    """
    从概率列表P中随机选择K个元素对应的下标
    :param P: 概率列表
    :param K: 要选择的元素个数
    :return: 选择的元素对应的下标列表
    """
    # 归一化概率列表
    normalized_probabilities = [prob / sum(P) for prob in P]

    # 使用numpy.random.choice进行随机选择，replace=False表示不重复选择
    selected_indices = np.random.choice(range(len(P)), size=K, replace=False, p=normalized_probabilities)

    return selected_indices


# 小类对应的大类
def find_rows(matrix, value):
    rows_with_value = [index for index, row in enumerate(matrix) if value in row][0]
    return rows_with_value


# 获取待推荐小类的长度
def count_images_in_cls(cls):
    """
    读取splits文件，返回cls子目录下的图片数量
    :param cls: 子目录的编号
    :return: cls子目录下的图片数量
    """
    cls_images_count = 0

    # 读取splits文件
    with open("splits.txt", "r") as splits_file:
        for line in splits_file:
            # 按#分割每一行的内容
            parts = line.strip().split("#")

            # 检查是否有足够的元素，并且cls匹配
            if len(parts) == 3 and parts[0] == str(cls):
                cls_images_count += 1

    return cls_images_count


def read_splits_and_match(index_list, key_list):
    """
    读取splits文件，根据给定的index和key进行匹配，返回匹配成功的文件名列表
    :param index_list: 匹配的索引列表
    :param key_list: 匹配的键列表
    :return: 匹配成功的文件名列表
    """
    imgs = []
    for i in key_list:
        with open("splits.txt", "r") as splits_file:
            for line in splits_file:
                parts = line.strip().split("#")
                temp=max(index_list[i]%count_images_in_cls(i),1)
                if i == int(parts[0]) and temp == int(parts[1]):

                    imgs.append(parts[2].replace('\n',''))
        index_list[i]+=1
    return imgs

def show_images(imgs):
    """
    打开并展示图片，按顺序标注为a、b、c、d...
    :param imgs: 图片文件路径列表
    """
    # 字母表
    alphabet = list(string.ascii_lowercase)

    # 创建一个新的图形
    fig, axs = plt.subplots(1, len(imgs), figsize=(15, 5))  # 调整 figsize 以适应图片显示

    # 遍历imgs列表
    for i, (img_path, ax) in enumerate(zip(imgs, axs)):
        # 读取图片
        img = Image.open(img_path)

        # 显示图片
        ax.imshow(img)
        ax.axis('off')

        # 获取图片的宽度和高度
        width, height = img.size

        # 标注字母在图片下方微调位置并调大字号
        ax.text(width / 2, height + 80, alphabet[i], fontsize=48, color='black', ha='center')

    # 展示所有图片
    plt.show()


def recommend(P, indexes, k=3):
    """
    param:向量P,每个小类样本推荐的概率
        维护一个待推荐样本序列（矩阵），矩阵的每一列代表各小类待推荐的样本（index%len来做）
    :return:display前K个样本，从同目录的data下拿图
    """
    global label  # 根据推荐的前K个样本修改label

    # 需要推荐的小类
    top_k_cls = random_select_indices(P, k)

    # print(top_k_indices)
    # 根据需要推荐的小类修改label对应的小类
    letters = list(label.keys())
    for i in range(k):
        label[letters[i]] = top_k_cls[i]
    # print(label)

    imgs=read_splits_and_match(indexes, top_k_cls)

    show_images(imgs=imgs)

# 测试
# recommend(P=[1,1,1,4,3,2,5], indexes=[1,1,1,1,1,1,1,1], k=2)
