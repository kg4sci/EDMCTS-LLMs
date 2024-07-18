"""
all the config parameter
"""
from transformers import AutoTokenizer
raw_csv_path = r"D:\PycharmProjects\Catalyst_V1\FaModel\data\20240108-Cu-based.xlsx"
checkpoint_token = 'allenai/scibert_scivocab_uncased'
tokenizer = AutoTokenizer.from_pretrained(checkpoint_token)
model_name = './bert-base-uncased'
str_index = ['material', 'formula', 'first_product', 'control_method', 'control_method_type', 'material_type', 'first_product_faraday_efficiency']
str_max_len = [10, 5, 5, 30]
accumulation_steps = 4
epoch = 400
