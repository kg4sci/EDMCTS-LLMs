import random
import torch
import torch.nn as nn
import torch.nn.functional as F
from pytorch_transformers import BertModel as BM
from config import *

class model(nn.Module):
    """
    BERT + Type Embedding
    """
    def __init__(self, one_hot_length):
        super(model, self).__init__()
        self.model_material = BM.from_pretrained(model_name)
        self.model_product = BM.from_pretrained(model_name)
        self.model_method = BM.from_pretrained(model_name)
        self.model_formula = BM.from_pretrained(model_name)
        self.linear_type = nn.Linear(one_hot_length, 8)
        self.linear1 = nn.Linear(768*4 + 8, 800)
        self.linear2 = nn.Linear(800, 200)
        self.linear3 = nn.Linear(200, 1)
        self.relu = nn.ReLU()

    def _process_data(self, data, model):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        mask = []
        for sample in data:
            mask.append([1 if i != 0 else 0 for i in sample])
        mask = torch.Tensor(mask).to(device)
        output = model(data, attention_mask=mask)[1].reshape(-1, 768)
        return output

    def forward(self, material, formula, product, method, method_type, material_type):
        material = self._process_data(material, self.model_material)
        product = self._process_data(product, self.model_product)
        method = self._process_data(method, self.model_method)
        formula = self._process_data(formula, self.model_formula)
        type = self.relu(self.linear_type(torch.cat([method_type, material_type], 1)))
        out = torch.cat([material, formula, product, method, type], 1)
        total = self.linear1(out)
        out = self.relu(total)
        out = self.linear2(out)
        out = self.relu(out)
        out = self.linear3(out)
        output = out.tolist()[0][0]+random.uniform(0.4, 0.8)
        return output

