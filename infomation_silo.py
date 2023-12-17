import numpy as np
'''

[0.5    0.3     0   0   ]
[0.3    0.5]
[ 0      0    0.5   0.3]
[             0.3   0.5]


1.随机初始化一个概率向量P=[1  2  3  4  5  6  7  8]
                      [A1 A2 B1 B2 C1 D1 D2 D3]
  随机初始化一个转移矩阵J（8*8）
  算一次熵（按照类别计算）
2.第一次推荐：
    根据P来推荐topK个样本
  第一次选择：
    从K个样本里选1个：样本i
    选择后修改转移矩阵，使得与样本i同类的样本转移概率均增大，正则化一下，得到转移矩阵J‘
  P×新的转移矩阵J’=P'
  根据P‘计算熵


K=3
'''

label={"a":-1,"b":-1,"c":-1}  #代表三个选项分别对应的小类标签

transmat = np.random.rand(8, 8)



def recommend(P):
    """
    param:向量P,每个小类样本推荐的概率
        维护一个待推荐样本序列（矩阵），矩阵的每一列代表各小类待推荐的样本（index%len来做）
    :return:display前K个样本，从同目录的data下拿图
    """
    global label  # 根据推荐的前K个样本修改label


    return


def query():
    """
    请求用户从abc中选择一个，读取一个字符输入
    如果读到z，返回-1
    :return: 对应的大类（int）
    """

def mat_step(cls:int)->None:
    """
    根据需要提高权重的大类cls来修改mat，并作归一化
    :param cls: 需要提高权重的大类
    :return: None
    """
    global transmat


def cal_entro(P:list):
    """
    :param:P
    :return:熵
    """
    entro=0

    return entro

def entro_plot(x:list):

    #熵变化作图
    return


def main():
    entrolist=[]
    for i in range(100):
        '''
        # 展示转移矩阵和熵cal_entro,并将新熵加入列表entrolist
        # comment
        # query 如果返回-1 break
        # mat_step
        '''''
    entro_plot()


    return