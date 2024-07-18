# 本文件用于上传文件，并取得微调ID

# 导入库
import os
import openai
# 导入API KEY
client = openai.OpenAI(
    base_url="https://35api.huinong.co/v1",#中转api，如果直接用openai的key则不需要加这一行
    api_key="sk-TvFbWNTb4cR3ULcAD17f0b457c4d4285BfD5A1F287CfE6F1"
)

# 上传训练文件
training_file = openai.File.create(
  file = open("mydata.jsonl","rb"),
  purpose="fine-tune"
)

# 打印微调ID
print(training_file.id)