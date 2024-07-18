import json
from config import *
import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader,TensorDataset,random_split

def _preprocess_data():
    token_file = []
    raw_data = pd.read_excel(raw_csv_path).dropna(subset=['first_product_faraday_efficiency'])
    material_type = np.unique(raw_data['material_type'].values)
    material_type_mapping = {index_id: int(i) + 0 for i, index_id in enumerate(np.unique(material_type))}
    method_type = np.unique(raw_data['control_method_type'].values)
    control_method_type_mapping = {index_id: int(i) + 0 for i, index_id in enumerate(np.unique(method_type))}
    for _, one_line in raw_data.iterrows():
        one_json = one_line.to_json()
        token_file.append(_preprocess_sample(one_json, material_type_mapping, control_method_type_mapping))

    all_dataset = TensorDataset(torch.LongTensor([i[0] for i in token_file]),
                                torch.LongTensor([i[1] for i in token_file]),
                                torch.LongTensor([i[2] for i in token_file]),
                                torch.LongTensor([i[3] for i in token_file]),
                                torch.FloatTensor([i[4] for i in token_file]),
                                torch.FloatTensor([i[5] for i in token_file]),
                                torch.FloatTensor([i[6] for i in token_file]))
    train_len = int(len(all_dataset) * 0.8)
    test_len = len(all_dataset) - train_len
    train_dataset, test_dataset = random_split(all_dataset, [train_len, test_len])
    train_loader = DataLoader(dataset=train_dataset,
                              batch_size=3,
                              shuffle=True)
    test_loader = DataLoader(dataset=test_dataset,
                             batch_size=1,
                             shuffle=True)


    return train_loader, test_loader, material_type_mapping, control_method_type_mapping




def _preprocess_sample(sample_str, material_type_mapping, control_method_type_mapping):
    """
    preprocess each sample with the limitation of maximum length and pad each sample to maximum length
    :param sample_str: Str format of json data, "Dict{'token': List[Str], 'label': List[Str]}"
    :return: sample -> Dict{'token': List[int], 'label': List[int], 'token_len': int}
    """
    #print(material_type_mapping)
    raw_sample = json.loads(sample_str)
    sample = [[] for n in range(len(str_index))]
    for key_ in raw_sample.keys():
        if key_ in str_index:
            if key_ == 'first_product_faraday_efficiency':
                sample[str_index.index(key_)].append(raw_sample[key_] / 100)
            elif key_ in ['control_method_type', 'material_type']:
                # 两个type只进行one-hot特征化
                mapping = eval(key_ + '_mapping')
                initial_encode = np.zeros([1, len(mapping)])
                #print(control_method_type_mapping)
                #print(material_type_mapping)
                initial_encode[0, mapping[raw_sample[key_]]] = 1
                sample[str_index.index(key_)] = initial_encode.tolist()[0]

            else:
                sample[str_index.index(key_)] = tokenizer.encode(raw_sample[key_],
                                                                 max_length=str_max_len[str_index.index(key_)],
                                                                 pad_to_max_length=True)


    return sample

if __name__ == '__main__':
    _preprocess_data()



