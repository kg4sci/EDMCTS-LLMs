import random
import math
import pandas as pd

#从构建好的节点里引入
attribute_index = []

def initial_value():
    n_existence_index = []
    for i in range(len(attribute_index)):
        ex_index = [0]
        eex_index = []
        if len(attribute_index[i]) == 1:
            n_existence_index.append(ex_index)
            continue
        for j in range(len(attribute_index[i][1])):
            eex_index.append(0)
        ex_index.append(eex_index)
        n_existence_index.append(ex_index)
    #print(n_existence_index)
    return(n_existence_index)

# def forward_stop():

def select_1(material_label, method_label, product, attribute_index, model_index):
    #final_index = 0
    if model_index == 1:
        final_index = random.randint(0, len(attribute_index)-1)
    elif model_index == 2:
        if method_label == "alloy":
            if material_label == "Cu":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 0.5), (1, 0.3), (2, 0.2)]
                elif product == "formate":
                    probability_distribution = [(1, 1)]
                elif product == "ethylene" or product == "ethanol":
                    probability_distribution = [(0, 1)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu-M":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 0.4), (1, 0.4), (2, 0.2)]
                elif product == "formate":
                    probability_distribution = [(1, 0.6), (2, 0.4)]
                elif product == "ethylene" or product == "ethanol":
                    probability_distribution = [(0, 0.4), (1, 0.3), (2, 0.3)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
        elif method_label == "defect":
            if material_label == "Cu":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 0.3), (1, 0.3), (2, 0.15), (3, 0.15), (4, 0.1)]
                elif product == "formate":
                    probability_distribution = [(0, 0.3), (1, 0.3), (2, 0.2), (3, 0.2)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.45), (1, 0.45), (4, 0.1)]
                elif product == "ethanol":
                    probability_distribution = [(0, 0.3), (1, 0.3), (2, 0.2), (3, 0.2)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu/C":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 0.25), (1, 0.25), (2, 0.25), (3, 0.25)]
                elif product == "formate":
                    probability_distribution = [(0, 0.3), (1, 0.3), (2, 0.2), (3, 0.2)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.15), (1, 0.15), (2, 0.3), (3, 0.3), (4, 0.1)]
                elif product == "ethanol":
                    probability_distribution = [(0, 0.2), (1, 0.2), (2, 0.3), (3, 0.3)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuOx":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 0.35), (1, 0.35), (2, 0.15), (3, 0.15)]
                elif product == "formate":
                    probability_distribution = [(0, 0.4), (1, 0.4), (2, 0.1), (3, 0.1)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.15), (1, 0.15), (2, 0.3), (3, 0.3), (4, 0.1)]
                elif product == "ethanol":
                    probability_distribution = [(0, 0.3), (1, 0.3), (2, 0.2), (3, 0.2)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuSx":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 0.25), (1, 0.25), (2, 0.25), (3, 0.25)]
                elif product == "formate":
                    probability_distribution = [(0, 0.45), (1, 0.45), (2, 0.05), (3, 0.05)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.5), (1, 0.5)]
                elif product == "ethanol":
                    probability_distribution = [(0, 0.35), (1, 0.35), (2, 0.15), (3, 0.15)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuNx":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 0.5), (1, 0.5)]
                elif product == "formate":
                    probability_distribution = [(0, 0.4), (1, 0.4), (2, 0.1), (3, 0.1)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.15), (1, 0.15), (2, 0.35), (3, 0.35)]
                elif product == "ethanol":
                    probability_distribution = [(0, 0.225), (1, 0.225), (2, 0.225), (3, 0.225), (4, 0.1)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu-M":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 0.25), (1, 0.25), (2, 0.25), (3, 0.25)]
                elif product == "formate":
                    probability_distribution = [(0, 0.35), (1, 0.35), (2, 0.15), (3, 0.15)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.25), (1, 0.25), (2, 0.2), (3, 0.2), (4, 0.1)]
                elif product == "ethanol":
                    probability_distribution = [(0, 0.15), (1, 0.15), (2, 0.35), (3, 0.35)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuMOx":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 0.15), (1, 0.15), (2, 0.35), (3, 0.35)]
                elif product == "formate":
                    probability_distribution = [(0, 0.4), (1, 0.4), (2, 0.1), (3, 0.1)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.25), (1, 0.25), (2, 0.2), (3, 0.2), (4, 0.1)]
                elif product == "ethanol":
                    probability_distribution = [(0, 0.35), (1, 0.35), (2, 0.15), (3, 0.15)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
        elif method_label == "atomic level dispersion":
            if material_label == "Cu/C":
                if product == "ethylene":
                    probability_distribution = [(2, 1)]
                elif product == "ethanol":
                    probability_distribution = [(0, 0.5), (2, 0.5)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu-M":
                if product == "carbon monoxide":
                    probability_distribution = [(1, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu-MOF":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 1)]
                elif product == "formate":
                    probability_distribution = [(1, 0.5), (2, 0.5)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.5), (2, 0.5)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu-MXene":
                if product == "formate":
                    probability_distribution = [(0, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu-MOx":
                if product == "formate":
                    probability_distribution = [(0, 1)]
                elif product == "ethanol":
                    probability_distribution = [(2, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu molecular complex":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 1)]
                elif product == "formate":
                    probability_distribution = [(0, 0.6), (2, 0.4)]
                elif product == "ethylene":
                    probability_distribution = [(0, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
        elif method_label == "surface/interface modification":
            if material_label == "Cu":
                if product == "carbon monoxide":
                    probability_distribution = [(2, 1)]
                elif product == "formate":
                    probability_distribution = [(0, 0.3), (2, 0.4), (3, 0.3)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.35), (1, 0.15), (2, 0.4), (3, 0.1)]
                elif product == "ethanol":
                    probability_distribution = [(0, 0.5), (3, 0.5)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuOx":
                if product == "carbon monoxide":
                    probability_distribution = [(2, 0.5), (3, 0.5)]
                elif product == "formate":
                    probability_distribution = [(3, 1)]
                elif product == "ethylene":
                    probability_distribution = [(3, 1)]
                elif product == "ethanol":
                    probability_distribution = [(0, 1)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuSx":
                if product == "formate":
                    probability_distribution = [(0, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
        elif method_label == "composite":
            if material_label == "Cu":
                if product == "ethylene":
                    probability_distribution = [(0, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu/C":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 0.5), (1, 0.5)]
                elif product == "formate":
                    probability_distribution = [(0, 1)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.7), (1, 0.3)]
                elif product == "ethanol":
                    probability_distribution = [(0, 1)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuOx":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 1)]
                elif product == "formate":
                    probability_distribution = [(0, 1)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.4), (1, 0.3), (2, 0.3)]
                elif product == "ethanol":
                    probability_distribution = [(0, 1)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuSx":
                if product == "carbon monoxide":
                    probability_distribution = [(1, 0.5), (2, 0.5)]
                elif product == "formate":
                    probability_distribution = [(0, 0.5), (1, 0.5)]
                elif product == "ethanol":
                    probability_distribution = [(1, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu-M":
                if product == "carbon monoxide":
                    probability_distribution = [(1, 1)]
                elif product == "formate":
                    probability_distribution = [(1, 1)]
                elif product == "ethylene":
                    probability_distribution = [(1, 1)]
                elif product == "ethanol":
                    probability_distribution = [(1, 1)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuMOx":
                if product == "ethylene":
                    probability_distribution = [(1, 1)]
                elif product == "ethanol":
                    probability_distribution = [(1, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu(Ox)-M(OH)x":
                if product == "carbon monoxide":
                    probability_distribution = [(3, 1)]
                elif product == "formate":
                    probability_distribution = [(0, 1)]
                elif product == "ethylene":
                    probability_distribution = [(3, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "M+CuOx":
                if product == "carbon monoxide":
                    probability_distribution = [(1, 1)]
                elif product == "formate":
                    probability_distribution = [(1, 1)]
                elif product == "ethylene":
                    probability_distribution = [(1, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu-MOx":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 0.5), (2, 0.5)]
                elif product == "formate":
                    probability_distribution = [(0, 1)]
                elif product == "ethylene":
                    probability_distribution = [(1, 0.5), (2, 0.5)]
                elif product == "ethanol":
                    probability_distribution = [(0, 1)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu molecular complex":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 1)]
                elif product == "ethanol":
                    probability_distribution = [(1, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuI":
                if product == "ethylene":
                    probability_distribution = [(1, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuSex":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuOx-MOx":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 0.4), (2, 0.6)]
                elif product == "formate":
                    probability_distribution = [(2, 1)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.3), (2, 0.7)]
                elif product == "ethanol":
                    probability_distribution = [(2, 1)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu-MSx":
                if product == "carbon monoxide":
                    probability_distribution = [(1, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
        elif method_label == "structure control":
            if material_label == "Cu":
                if product == "carbon monoxide":
                    probability_distribution = [(2, 0.2), (3, 0.2), (4, 0.2), (7, 0.2), (8, 0.2)]
                elif product == "formate":
                    probability_distribution = [(2, 0.2), (4, 0.2), (5, 0.2), (7, 0.2), (8, 0.2)]
                elif product == "ethylene":
                    probability_distribution = [(2, 0.15), (3, 0.1), (4, 0.15), (5, 0.15), (6, 0.1), (7, 0.15), (8, 0.2)]
                elif product == "ethanol":
                    probability_distribution = [(4, 0.5), (5, 0.5)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu/C":
                if product == "carbon monoxide":
                    probability_distribution = [(3, 0.3), (4, 0.4), (8, 0.3)]
                elif product == "formate":
                    probability_distribution = [(4, 0.2), (5, 0.5), (8, 0.3)]
                elif product == "ethanol":
                    probability_distribution = [(8, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuOx":
                if product == "carbon monoxide":
                    probability_distribution = [(4, 0.25), (5, 0.25), (6, 0.25), (8, 0.25)]
                elif product == "formate":
                    probability_distribution = [(4, 0.6), (3, 0.2), (8, 0.2)]
                elif product == "ethylene":
                    probability_distribution = [(1, 0.2), (2, 0.1), (3, 0.2), (4, 0.2), (7, 0.1), (8, 0.2)]
                elif product == "ethanol":
                    probability_distribution = [(3, 0.3), (4, 0.4), (8, 0.3)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuSx":
                if product == "carbon monoxide":
                    probability_distribution = [(4, 1)]
                elif product == "formate":
                    probability_distribution = [(3, 0.3), (4, 0.4), (7, 0.3)]
                elif product == "ethylene":
                    probability_distribution = [(4, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuNx":
                if product == "ethylene":
                    probability_distribution = [(4, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu-M":
                if product == "carbon monoxide":
                    probability_distribution = [(0, 125), (1, 0.125), (3, 0.125), (4, 0.125), (5, 0.125), (6, 0.125), (7, 0.125), (8, 0.125)]
                elif product == "formate":
                    probability_distribution = [(0, 125), (1, 0.125), (3, 0.125), (4, 0.125), (5, 0.125), (6, 0.125), (7, 0.125), (8, 0.125)]
                elif product == "ethylene":
                    probability_distribution = [(0, 0.25), (4, 0.25), (5, 0.25), (6, 0.25)]
                elif product == "ethanol":
                    probability_distribution = [(2, 0.4), (4, 0.3), (8, 0.3)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuMOx":
                if product == "formate":
                    probability_distribution = [(4, 1)]
                elif product == "ethylene":
                    probability_distribution = [(4, 1)]
                elif product == "ethanol":
                    probability_distribution = [(4, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu-MOF":
                if product == "formate":
                    probability_distribution = [(3, 1)]
                elif product == "ethylene":
                    probability_distribution = [(4, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu(Ox)-M(OH)x":
                if product == "carbon monoxide":
                    probability_distribution = [(4, 1)]
                elif product == "formate":
                    probability_distribution = [(4, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuMSx":
                if product == "carbon monoxide":
                    probability_distribution = [(4, 1)]
                elif product == "formate":
                    probability_distribution = [(4, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuPx":
                if product == "carbon monoxide":
                    probability_distribution = [(4, 1)]
                elif product == "formate":
                    probability_distribution = [(4, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "M+CuOx":
                if product == "carbon monoxide":
                    probability_distribution = [(4, 1)]
                elif product == "ethylene":
                    probability_distribution = [(4, 0.5), (8, 0.5)]
                elif product == "ethanol":
                    probability_distribution = [(1, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu-MOx":
                if product == "carbon monoxide":
                    probability_distribution = [(4, 1)]
                elif product == "formate":
                    probability_distribution = [(4, 0.3), (5, 0.4), (6, 0.3)]
                elif product == "ethylene":
                    probability_distribution = [(4, 0.5), (8, 0.5)]
                elif product == "ethanol":
                    probability_distribution = [(4, 1)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "Cu molecular complex":
                if product == "carbon monoxide":
                    probability_distribution = [(4, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuSex":
                if product == "formate":
                    probability_distribution = [(4, 1)]
                elif product == "ethylene":
                    probability_distribution = [(4, 1)]
                else:
                    final_index = random.randint(0, len(attribute_index)-1)
                    return final_index
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]
            elif material_label == "CuOx-MOx":
                if product == "carbon monoxide":
                    probability_distribution = [(4, 0.5), (8, 0.5)]
                elif product == "formate":
                    probability_distribution = [(0, 0.5), (4, 0.5)]
                elif product == "ethylene":
                    probability_distribution = [(2, 0.5), (4, 0.5)]
                elif product == "ethanol":
                    probability_distribution = [(4, 1)]
                final_index = random.choices(population=[item for item, _ in probability_distribution], 
                    weights=[probability for _, probability in probability_distribution], 
                    k=1)
                return final_index[0]            
        final_index = random.randint(0, len(attribute_index)-1)
    return final_index

def select_2(material_label, method_label, product, attribute_index, model_index, index_1):
    if model_index == 1:
        final_index = random.randint(0, len(attribute_index[index_1][1])-1)
    elif model_index == 2:
        if method_label == "defect":
            if material_label == "CuOx-MOx":
                if product == "carbon monoxide":
                    if index_1 == 3:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
        elif method_label == "defect":
            if material_label == "Cu/C":
                if product == "carbon monoxide":
                    if index_1 == 0:
                        probability_distribution = [(1, 0.4), (2, 0.3), (3, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 1:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 0:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu-M":
                if product == "carbon monoxide":
                    if index_1 == 1:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu-MOF":
                if product == "carbon monoxide":
                    if index_1 == 0:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 1:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 0:
                        probability_distribution = [(4, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0] 
            elif material_label == "Cu-MXene":
                if product == "formate":
                    if index_1 == 0:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu-MOx":
                if product == "formate":
                    if index_1 == 0:
                        probability_distribution = [(4, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu molecular complex":
                if product == "carbon monoxide":
                    if index_1 == 0:
                        probability_distribution = [(0, 0.6), (2, 0.4)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 0:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 0:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
        elif method_label == "surface/interface modification":
            if material_label == "Cu":
                if product == "carbon monoxide":
                    if index_1 == 2:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 0:
                        probability_distribution = [(5, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 2:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 3:
                        probability_distribution = [(4, 0.4), (5, 0.3), (6, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 0:
                        probability_distribution = [(0, 0.4), (1, 0.3), (4, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 2:
                        probability_distribution = [(0, 0.2), (1, 0.2), (2, 0.2), (3, 0.2), (4, 0.2)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 3:
                        probability_distribution = [(3, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 0:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 3:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuOx":
                if product == "carbon monoxide":
                    if index_1 == 2:
                        probability_distribution = [(5, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 3:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate": 
                    if index_1 == 3:
                        probability_distribution = [(3, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 3:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 0:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuSx":
                if product == "formate":
                    if index_1 == 0:
                        probability_distribution = [(3, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
        elif method_label == "composite":
            if material_label == "Cu":
                if product == "ethylene":
                    if index_1 == 0:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu/C":
                if product == "carbon monoxide":
                    if index_1 == 0:
                        probability_distribution = [(0, 0.4), (3, 0.3), (6, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 1:
                        probability_distribution = [(10, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate": 
                    if index_1 == 0:
                        probability_distribution = [(0, 0.35), (1, 0.35), (3, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 0:
                        probability_distribution = [(0, 0.35), (3, 0.25), (6, 0.35)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 1:
                        probability_distribution = [(10, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 0:
                        probability_distribution = [(0, 0.25), (2, 0.25), (5, 0.25), (7, 0.25)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuOx":
                if product == "carbon monoxide":
                    if index_1 == 0:
                        probability_distribution = [(0, 0.4), (6, 0.3), (7, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate": 
                    if index_1 == 0:
                        probability_distribution = [(7, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 0:
                        probability_distribution = [(1, 0.125), (2, 0.125), (3, 0.125), (4, 0.125), (5, 0.125), (6, 0.125), (7, 0.125), (8, 0.125)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 1:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 2:
                        probability_distribution = [(4, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 0:
                        probability_distribution = [(0, 0.5), (1, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuSx":
                if product == "carbon monoxide":
                    if index_1 == 1:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 2:
                        probability_distribution = [(5, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate": 
                    if index_1 == 0:
                        probability_distribution = [(5, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 1:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu-M":
                if product == "carbon monoxide":
                    if index_1 == 1:
                        probability_distribution = [(0, 0.15), (1, 0.15), (2, 0.15), (7, 0.15), (8, 0.15), (9, 0.15), (13, 0.1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 1:
                        probability_distribution = [(0, 0.125), (3, 0.125), (4, 0.125), (5, 0.125), (6, 0.125), (8, 0.125), (9, 0.125), (12, 0.125)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 1:
                        probability_distribution = [(0, 0.2), (1, 0.2), (2, 0.2), (9, 0.2), (11, 0.2)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 1:
                        probability_distribution = [(0, 0.5), (1, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuMOx":
                if product == "ethylene":
                    if index_1 == 1:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu-MOF":
                if product == "ethylene":
                    if index_1 == 1:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 1:
                        probability_distribution = [(3, 0.5), (9, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu(Ox)-M(OH)x":
                if product == "carbon monoxide":
                    if index_1 == 3:
                        probability_distribution = [(0, 0.5), (1, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 0:
                        probability_distribution = [(4, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 3:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "M+CuOx":
                if product == "carbon monoxide":
                    if index_1 == 1:
                        probability_distribution = [(5, 0.5), (8, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 1:
                        probability_distribution = [(5, 0.3), (9, 0.3), (11, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 1:
                        probability_distribution = [(0, 0.5), (1, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu-MOx":
                if product == "carbon monoxide":
                    if index_1 == 0:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 2:
                        probability_distribution = [(0, 0.25), (3, 0.25), (5, 0.25), (7, 0.25)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 0:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 1:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 2:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 0:
                        probability_distribution = [(5, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu molecular complex":
                if product == "carbon monoxide":
                    if index_1 == 0:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 1:
                        probability_distribution = [(5, 0.5), (9, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuI":
                if product == "ethylene":
                    if index_1 == 1:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuSex":
                if product == "carbon monoxide":
                    if index_1 == 0:
                        probability_distribution = [(4, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuOx-MOx":
                if product == "carbon monoxide":
                    if index_1 == 0:
                        probability_distribution = [(4, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 2:
                        probability_distribution = [(5, 0.5), (7, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 2:
                        probability_distribution = [(5, 0.4), (12, 0.3), (13, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 0:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 2:
                        probability_distribution = [(0, 0.2), (1, 0.2), (2, 0.2), (5, 0.2), (6, 0.2)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 2:
                        probability_distribution = [(3, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu-MSx":
                if product == "carbon monoxide":
                    if index_1 == 1:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
        elif method_label == "structure control":
            if material_label == "Cu":
                if product == "carbon monoxide":
                    if index_1 == 2:
                        probability_distribution = [(1, 0.5), (3, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 3:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(0, 0.25), (6, 0.25), (10, 0.25), (15, 0.25)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 7:
                        probability_distribution = [(6, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 2:
                        probability_distribution = [(3, 0.5), (6, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(6, 0.4), (11, 0.3), (13, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 5:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 7:
                        probability_distribution = [(0, 0.4), (1, 0.3), (5, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(0, 0.4), (2, 0.3), (3, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 2:
                        probability_distribution = [(0, 0.5), (1, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(2, 0.1), (3, 0.1), (4, 0.1), (8, 0.1), (9, 0.1), (10, 0.1), (11, 0.1), (12, 0.1), (15, 0.1), (16, 0.1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 5:
                        probability_distribution = [(0, 0.5), (5, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 6:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 7:
                        probability_distribution = [(0, 0.4), (1, 0.3), (2, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(0, 0.4), (1, 0.3), (3, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 4:
                        probability_distribution = [(0, 0.4), (9, 0.3), (16, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 5:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu/C":
                if product == "carbon monoxide":
                    if index_1 == 3:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(2, 0.3), (9, 0.4), (11, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 4:
                        probability_distribution = [(11, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 5:
                        probability_distribution = [(4, 0.5), (5, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 8:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuOx":
                if product == "carbon monoxide":
                    if index_1 == 4:
                        probability_distribution = [(7, 0.25), (9, 0.25), (10, 0.25), (17, 0.25)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 5:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 6:
                        probability_distribution = [(0, 0.5), (3, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 3:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(2, 0.1), (4, 0.2), (8, 0.2), (10, 0.1), (11, 0.1), (15, 0.2), (17, 0.1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 1:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 2:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 3:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(0, 0.1), (2, 0.1), (6, 0.1), (8, 0.1), (9, 0.1), (10, 0.1), (11, 0.1), (13, 0.1), (14, 0.1), (17, 0.1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 7:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(1, 0.5), (2, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 3:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(11, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuSx":
                if product == "carbon monoxide":
                    if index_1 == 4:
                        probability_distribution = [(6, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 3:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(0, 0.2), (3, 0.2), (9, 0.2), (11, 0.2), (13, 0.2)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 7:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 4:
                        probability_distribution = [(0, 0.3), (3, 0.3), (13, 0.4)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuNx":
                if product == "ethylene":
                    if index_1 == 4:
                        probability_distribution = [(11, 0.5), (17, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu-M":
                if product == "carbon monoxide":
                    if index_1 == 0:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 1:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 3:
                        probability_distribution = [(0, 0.5), (1, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(0, 0.125), (3, 0.125), (6, 0.125), (8, 0.125), (9, 0.125), (10, 0.125), (12, 0.125), (12, 0.125)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 5:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 6:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 7:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(0, 0.3), (1, 0.4), (2, 0.3)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 0:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 1:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 3:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(3, 0.2), (7, 0.1), (9, 0.1), (10, 0.2), (11, 0.2), (13, 0.1), (14, 0.1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 5:
                        probability_distribution = [(0, 0.5), (5, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 6:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 7:
                        probability_distribution = [(0, 0.5), (5, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(0, 0.5), (2, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 0:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(17, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 5:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 6:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 2:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(0, 0.3), (8, 0.3), (9, 0.4)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuMOx":
                if product == "formate":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu-MOF":
                if product == "formate":
                    if index_1 == 3:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu(Ox)-M(OH)x":
                if product == "carbon monoxide":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuMSx":
                if product == "carbon monoxide":
                    if index_1 == 4:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 4:
                        probability_distribution = [(6, 0.5), (9, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuPx":
                if product == "carbon monoxide":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "M+CuOx":
                if product == "carbon monoxide":
                    if index_1 == 4:
                        probability_distribution = [(8, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 4:
                        probability_distribution = [(6, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 1:
                        probability_distribution = [(1, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu-MOx":
                if product == "carbon monoxide":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 4:
                        probability_distribution = [(3, 0.5), (10, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 5:
                        probability_distribution = [(5, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 6:
                        probability_distribution = [(0, 0.5), (1, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 4:
                        probability_distribution = [(8, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(2, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "Cu molecular complex":
                if product == "carbon monoxide":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuSex":
                if product == "formate":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 4:
                        probability_distribution = [(9, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
            elif material_label == "CuOx-MOx":
                if product == "carbon monoxide":
                    if index_1 == 0:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 8:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "formate":
                    if index_1 == 0:
                        probability_distribution = [(0, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    if index_1 == 4:
                        probability_distribution = [(7, 0.5), (9, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethylene":
                    if index_1 == 2:
                        probability_distribution = [(3, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                    elif index_1 == 4:
                        probability_distribution = [(14, 1)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]
                elif product == "ethanol":
                    if index_1 == 4:
                        probability_distribution = [(11, 0.5), (12, 0.5)]
                        final_index = random.choices(population=[item for item, _ in probability_distribution], 
                            weights=[probability for _, probability in probability_distribution], 
                            k=1)
                        return final_index[0]       
        final_index = random.randint(0, len(attribute_index[index_1][1])-1)
    return final_index