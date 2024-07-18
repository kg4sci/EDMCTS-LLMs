import torch
from data_loader import _preprocess_data
from model import *
from torch import optim
from torch.autograd import Variable
import numpy as np
import time
import os
import shutil


def remove_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def validate(val_loader, train_model, criterion):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(device)
    train_model.to(device)
    train_model.eval()
    val_loss = []
    with torch.no_grad():
        for batch_idx, (material, formula, product, method, method_type, material_type, target) in enumerate(val_loader):
            material = Variable(material).to(device)
            formula = Variable(formula).to(device)
            product = Variable(product).to(device)
            method = Variable(method).to(device)
            method_type = Variable(method_type).to(device)
            material_type = Variable(material_type).to(device)
            target = Variable(target.view(-1, 1)).to(device)
            output = train_model.forward(material, formula, product, method, method_type, material_type)
            loss = criterion(output, target)
            val_loss.append(loss.item())
        return np.mean(val_loss)


def train(path):
    train_loader, test_loader, material_type_mapping, control_method_type_mapping = _preprocess_data()
    np.save(path + "material_type_mapping.npy", material_type_mapping)
    np.save(path + "control_method_type_mapping.npy", material_type_mapping)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    one_hot_len = len(material_type_mapping) + len(control_method_type_mapping)
    train_model = model(one_hot_len)
    train_model.to(device)
    train_model.train()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(train_model.parameters(), lr=1e-5)
    best_valid_loss = 100
    early_stop = 0
    Loss = []
    for i in range(epoch):
        for batch_idx, (material, formula, product, method, method_type, material_type, target) in enumerate(train_loader):
            material = Variable(material).to(device)
            formula = Variable(formula).to(device)
            product = Variable(product).to(device)
            method = Variable(method).to(device)
            method_type = Variable(method_type).to(device)
            material_type = Variable(material_type).to(device)
            target = Variable(target.view(-1, 1)).to(device)
            output = train_model.forward(material, formula, product, method, method_type, material_type)
            loss = criterion(output, target)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            if ((batch_idx + 1) % accumulation_steps) == 1:
                # print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss:{:.6f}'.format(
                #     i + 1, batch_idx, len(train_loader), 100. *
                #     batch_idx / len(train_loader), loss.item()
                # ))
                running_loss = loss.item()
                Loss.append(running_loss)
            if batch_idx == len(train_loader) - 1:
                print('labels:', target)
                print('pred:', output)

        val_loss = validate(test_loader, train_model, criterion)
        # print('val_loss:' + str(val_loss))
        if val_loss < best_valid_loss:
            best_valid_loss = val_loss
            torch.save(train_model.state_dict(), path + 'model.pt')
            early_stop = 0
        else:
            early_stop += 1
        if early_stop >= 10:
            break
    np.save(path + "loss.npy", Loss)
    return best_valid_loss

if __name__ == '__main__':
    best_valid_loss = 100
    for i in range(100):
        t = str(time.time()).replace('.', '_')
        print(str(t))
        os.mkdir(str(t))
        path = str(t) + '/'

        best_valid_loss_epoch = train(path)
        if best_valid_loss_epoch < best_valid_loss:
            best_valid_loss = best_valid_loss_epoch
            with open(path + 'result.txt', 'w+') as f:
                f.write(str(best_valid_loss))
        else:
            remove_folder(path)



