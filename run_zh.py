import json
import jieba
import opencc

converter = opencc.OpenCC('s2t.json')

with open("raw.json") as f:
    data = json.load(f)

new_data = []

i = 1
for record in data:
    if record['text_lang'] == 'zh-CN':
        print(i)
        i = i + 1
        record['text_lang'] == 'zh-TW'
        record['text'] = converter.convert(record['text'])
        new_data.append(record)
    elif record['text_lang'] == 'zh-TW':
        print(i)
        i = i + 1
        new_data.append(record)

with open('raw_zh.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)

# jieba.enable_paddle()
# strs=["人口密度是單位面積有多少人","而應力是單位面積承受多少力","折疊後在直角處施力，會產生很大的剪應力，就能輕鬆撕開膠帶囉~"]
# for str in strs:
#     # print(str)
#     seg_list = jieba.cut(str,use_paddle=True) # 使用paddle模式
#     print(list(seg_list))
#     # seg_list = jieba.cut(str, cut_all=False)
#     # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#     # seg_list = jieba.cut(str)  # 默认是精确模式
#     # print(", ".join(seg_list))

# # seg_list = jieba.cut(str, cut_all=True)
# # print("Full Mode: " + "/ ".join(seg_list))  # 全模式