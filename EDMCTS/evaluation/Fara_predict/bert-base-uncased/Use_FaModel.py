import numpy as np
from collections import defaultdict
from model import *
import torch
import torch.nn as nn
import torch.nn.functional as F
from pytorch_transformers import BertModel as BM
from data_loader import _preprocess_sample
from torch.autograd import Variable
import json


class Use_FaModel(object):

    def __init__(self,model_path):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.material_type_mapping = np.load(model_path + '/material_type_mapping.npy', allow_pickle=True).item()
        self.control_method_type_mapping = np.load(model_path + '/control_method_type_mapping.npy', allow_pickle=True).item()
        one_hot_len = len(self.material_type_mapping) + len(self.control_method_type_mapping)
        self.model_import = model(one_hot_len)
        self.model_import.load_state_dict(state_dict=torch.load(model_path + '/model.pt'))
        self.model_import.to(self.device)

    def predict(self, material_type, formula, material, product, control_method_type, control_method):

        with torch.no_grad():
            sample_str = {
                "formula": formula,
                "material_type": material_type,
                "control_method_type": control_method_type,
                "material": material,
                "first_product": product,
                "control_method": control_method}

            sample = _preprocess_sample(json.dumps(sample_str), self.material_type_mapping,
                                        self.control_method_type_mapping)
            material = Variable(torch.LongTensor(sample[0]).reshape(1, -1)).to(self.device)
            formula = Variable(torch.LongTensor(sample[1]).reshape(1, -1)).to(self.device)
            product = Variable(torch.LongTensor(sample[2]).reshape(1, -1)).to(self.device)
            method = Variable(torch.LongTensor(sample[3]).reshape(1, -1)).to(self.device)
            method_type = Variable(torch.FloatTensor(sample[4]).reshape(1, -1)).to(self.device)
            material_type = Variable(torch.FloatTensor(sample[5]).reshape(1, -1)).to(self.device)
            output = self.model_import(material, formula, product, method, method_type, material_type)
            #print(output)
            predict_result = min(output, 1)
            return predict_result




if __name__ == '__main__':
    model_path = "trained_model"
    U = Use_FaModel(model_path)
    result = U.predict("E", "formula", "Cu", "CO", "composite", "Strain Engineering")
    print(result)

