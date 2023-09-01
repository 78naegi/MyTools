# 翻译艾丝蒂尔线时写的简单脚本
# 定义原版txt和翻译后txt文件
original_file = r'D:\MyTools\temp\yak11030.txt'
translated_file = r'D:\MyTools\temp\yak11030_translated.txt'
# 定义原文单词，需要替换的单词和替换后的单词
original_word = 'エステルさん'
old_word = '艾丝蒂尔'
new_word = '艾丝蒂尔小姐'

# 打开原版txt和翻译后txt文件
with open(original_file, 'r', encoding='utf-8') as f1, open(translated_file, 'r', encoding='utf-8') as f2:
    # 读取文件内容并按行存储到列表中
    original_lines = f1.readlines()
    translated_lines = f2.readlines()


# 遍历每一行原版txt文件内容
for i in range(len(original_lines)):
    # 判断该行是否需要替换，若需要，将需要替换的单词替换为新单词
    if original_lines[i].find(original_word)!=-1 and translated_lines[i].find(new_word)==-1:
        translated_lines[i] = translated_lines[i].replace(old_word, new_word)

# 将替换后的内容写入翻译后txt文件
with open(translated_file, 'w', encoding='utf-8') as f:
    f.writelines(translated_lines)
