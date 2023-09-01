# 定义原版txt和翻译后txt文件
original_file = r'部分文本\original\c10_a01.txt'
translated_file = r'部分文本\translation\c10_a01.txt'
# 定义原文单词，需要替换的单词和替换后的单词
original_word = ['アンジェリーク','アンジェ','チェスター','クレリア','コレット','アルトワーズ',
                 'クロエ','ホーネット','優しい女性の声','透き通った女性の声','物静かな声',
                 '元気な声','ミリアム','ミネット','ポチ','冒険者の女','アストレイリア','村人・男','村人・女']

new_word = ['安琪莉可','安琪','切斯特','克蕾莉娅','柯蕾特','阿尔托瓦兹',
            '克罗艾','蜂兵','温柔的女性声音','清脆的女性声音','斯文的声音',
            '精神的声音','米莉亚姆','米内特','波奇','冒险者女性','阿斯特雷利亚','男村民','女村民']

# 打开原版txt和翻译后txt文件
with open(original_file, 'r', encoding='utf_8_sig') as f1, open(translated_file, 'r', encoding='utf_8_sig') as f2:
    # 读取文件内容并按行存储到列表中
    original_lines = f1.readlines()
    translated_lines = f2.readlines()

# 遍历每一行原版txt文件内容
for i in range(len(original_lines)):
    # 判断该行是否需要替换，若需要，将需要替换的单词替换为新单词
    for j in range(len(original_word)):
        if original_lines[i]==original_word[j]+'\n' and translated_lines[i]!=new_word[j]+'\n':
            translated_lines[i] = new_word[j]+'\n'

# 将替换后的内容写入翻译后txt文件
with open(translated_file, 'w', encoding='utf_8_sig') as f:
    f.writelines(translated_lines)
