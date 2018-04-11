# coding:utf-8
# 绘制一个词云
import sys
from wordcloud import WordCloud,ImageColorGenerator
from collections import Counter
import jieba.posseg as psg
import matplotlib.pyplot as plt

# 对文本分词并标注词性，并缓存到文件
def cut_and_cache(text):
    # 将文本分词，并附带上词性，因为数据量比较大，防止每次运行脚本都花大量时间，所以第一次分词后就将结果存入文件cut_result.txt中
    # 相当于做一个缓存，格式为每个词占一行，每一行的内容为：
    # 词,词性
    words_with_attr = [(x.word, x.flag) for x in psg.cut(text) if len(x.word) >= 2]
    with open('cut_result.txt', 'w+') as f:
        for x in words_with_attr:
            f.write('{0}\t{1}\n'.format(x[0], x[1]))
    return words_with_attr


# 从cut_result.txt中读取带词性的分词结果列表
def read_cut_result():
    words_with_attr = []
    with open('cut_result.txt', 'r') as f:
        for x in f.readlines():
            # 这里解码成utf-8格式，是为了防止后面生成词云的时候出现乱码
            x = x.decode('utf-8')
            pair = x.split()
            if len(pair) < 2:
                continue
            words_with_attr.append((pair[0], pair[1]))
    return words_with_attr


# 　统计在分词表中出现次数排名前topn的词的列表，并将结果输出到文件topn_words.txt中，每行一个词，格式为：
# 词,出现次数
def get_topn_words(words, topn):
    c = Counter(words).most_common(topn)
    top_words_with_freq = {}
    with open('top{0}_words.txt'.format(topn), 'w+') as f:
        for x in c:
            f.write('{0},{1}\n'.format(x[0], x[1]))
            top_words_with_freq[x[0]] = x[1]
    return top_words_with_freq


# 传入文本文件的路径file_path和topn，获取文本文件中topn关键词列表及词频
def get_top_words(file_path, topn):
    # 读取文本文件，然后分词并缓存，只需运行一次，后续运行脚本可注释掉下面两行
    # text = open(file_path).read()
    # words_with_attr = cut_and_cache(text)

    # 从cut_result.txt中读取带词性的分词结果列表
    words_with_attr = read_cut_result()

    # 要过滤掉的词性列表
    stop_attr = ['a', 'ad', 'b', 'c', 'd', 'f', 'df', 'm', 'mq', 'p', 'r', 'rr', 's', 't', 'u', 'v', 'z']

    # 过滤掉不需要的词性的词
    words = [x[0] for x in words_with_attr if x[1] not in stop_attr]

    # 获取topn的词并存入文件topn_words.txt，top_words_with_freq为一个字典，在生成词云的时候会用到，格式为：
    # {'aa':1002,'bb':879,'cc':456}
    top_words_with_freq = get_topn_words(words=words, topn=topn)

    return top_words_with_freq


# 根据传入的背景图片路径和词频字典、字体文件，生成指定名称的词云图片
def generate_word_cloud(top_words_with_freq, font_path, to_save_img_path, background_color='white'):
    # 创建词云对象
    wc = WordCloud(font_path=font_path,  # 设置字体
                   background_color=background_color,  # 词云图片的背景颜色，默认为白色
                   max_words=100,  # 最大显示词数为100
                   max_font_size=80,  # 字体最大字号
                   random_state=50,  # 字体的最多模式
                   width=500,  # 词云图片宽度
                   margin=2,  # 词与词之间的间距
                   height=300)  # 词云图片高度

    # 用top_words_with_freq生成词云内容
    wc.generate_from_frequencies(top_words_with_freq)

    # 用matplotlib绘出词云图片显示出来
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

    # 将词云图片保存成图片
    wc.to_file(to_save_img_path)


def main():
    # 设置环境为utf-8编码格式，防止处理中文出错
    reload(sys)
    sys.setdefaultencoding('utf-8')

    # 获取topn词汇的'词:词频'字典，santi.txt是当前目录下的文本文件
    top_words_with_freq = get_top_words('./merge.txt', 100)

    # 生成词云图片，yahei.ttf是当前目录下微软雅黑字体文件，wordcloud.png是要生成的词云图片名
    generate_word_cloud(top_words_with_freq, './yahei.ttf', './wordcloud.png')

    print 'all is finished!'


if __name__ == '__main__':
    main()
