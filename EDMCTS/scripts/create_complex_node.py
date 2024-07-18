from openai import OpenAI
import pandas as pd
import numpy as np
import math
import random
from ast import literal_eval
import csv #导入csv模块
import json


client = OpenAI(
base_url="https://35api.huinong.co/v1",#中转api，如果直接用openai的key则不需要加这一行
api_key="sk-rOS72qSe5p7CamiGBaD9546b33Aa46D58bFbE1951f8b8734"
)

#标记当前prompt里是否存在这一属性，1为存在，0为不存在
existence_index = []
#标记属性名称
attribute_index = []
#标记属性的value函数
value_index = []
# initial_prompt = "Generate a list of top-5 alloy for {material} to produce {product}. 
# You should use alloy with the following options CO. For each options in CO, 
# you should use the corresponding Au. Let's think step by step. 
# Provide scientific explanations for each of the regulation methods. 
# Finally, return a python list named $final_answer which contains the top-5 regulation methods."
answer_alloy_corpus = pd.DataFrame()
materials = ["Cu", "Cu/C", "CuOx", "CuSx", "CuNx", "Cu-M", "CuMOx", "Cu-MOF", "Cu(Ox)-M(OH)x", "CuMSx", "CuPx", "M+CuOx", "Cu-MXene", "Cu-MOx", "Cu molecular complex", "CuI", "CuSex", "CuOx-MOx", "Cu-MSx"]
products = ["carbon monoxide", "formate", "ethylene", "ethanol"]

fstring_text = (
        "Generate a list of top-5 {method_label} "
        "for {material_label} to produce {product}. "
        "{candidate_statement}"
        "{method_statement}"
        "{extension_1_statement}"
        "{extension_2_statement}"
        "Provide scientific explanations for each of the regulation methods. "
        "Finally, return a python list named $final_answer which contains the top-5 regulation methods."
        r"\n\nTake a deep breath and let's think step-by-step. Remember, you need to return a python list named final_answer!"
    )

candidate_statement = (
        "For example: {candidate_list}. "
    )
method_statement = (
        "You should use {method_label} with the following options {extension_1}. "
    )
extension_text_1 = (
        "For each options in {extension_1}, "
        "you should use the corresponding {extension_2}. "
    )
extension_text_2 = (
        "For each options in {extension_2}. "
        "you should use the corresponding {extension_3}. "
    )


def parse_answer(answer: str, num_expected=None):
    """Parse an answer into a list."""
    final_answer_location = answer.lower().find("final_answer")
    if final_answer_location == -1:
        final_answer_location = answer.lower().find("final answer")
    if final_answer_location == -1:
        final_answer_location = answer.lower().find("final")  # last ditch effort
    if final_answer_location == -1:
        final_answer_location = 0
    list_start = answer.find("[", final_answer_location)
    list_end = answer.find("]", list_start)
    try:
        answer_list = literal_eval(answer[list_start : list_end + 1])  # noqa:E203
    except Exception:
        answer_list = answer[list_start + 1 : list_end]  # noqa:E203
        answer_list = [ans.replace("'", "") for ans in answer_list.split(",")]
    #print(answer_list)
    return [json.dumps(ans).replace('"', "").replace("'", "").strip() for ans in answer_list]

def initiaize_tree_attribute(input_path):
    method_classification = pd.read_csv(input_path)
    extension_1 = method_classification["extension_1"]
    extension_2 = method_classification["extension_2"]
    extension_3 = method_classification["extension_3"]
    i = 0
    while i < len(extension_1) - 1:
        a1 = extension_1[i]
        att_index = [a1]
        attt_index = []
        if pd.notnull(extension_2[i]):
            #print(extension_2[i])
            extension2_list = extension_2[i].split(';')
            #print(extension2_list)
            if len(extension2_list) == 1:
                #说明该extension1下有extension3
                if pd.isnull(extension_3[i]):
                    att2_index = [extension_2[i]]
                    att_index.append(att2_index)
                    i = i + 1
                    while pd.isnull(extension_3[i]):
                        att2_index = [extension_2[i]]
                        att_index.append(att2_index)
                        i = i + 1
                    while True:
                        #print(extension_1[i])
                        att2_index = [extension_2[i]]
                        #print(extension_2[i])
                        att2_index.append(extension_3[i].split(';'))
                        att_index.append(att2_index)
                        i = i + 1
                        #print(extension_1[i])
                        if i >= len(extension_1) or pd.notnull(extension_1[i]):
                            break
                else:
                    while True:
                        #print(extension_1[i])
                        att2_index = [extension_2[i]]
                        #print(extension_2[i])
                        att2_index.append(extension_3[i].split(';'))
                        att_index.append(att2_index)
                        i = i + 1
                        #print(extension_1[i])
                        if i >= len(extension_1) or pd.notnull(extension_1[i]):
                            break
            else:
                #说明没有extension3
                att_index.append(extension_2[i].split(';'))
                i = i + 1
            attt_index.append(att_index)
        else:
            i = i + 1
        att_index.append(attt_index)
        attribute_index.append(att_index)
    print(attribute_index)
    #print(existence_index)

def initiaize_tree_existence(attribute_index):
    n_existence_index = []
    #print(attribute_index[1][1][0])
    for i in range(len(attribute_index)):
        #extension1的属性存在为0
        ex_index = [0]
        #extension2的存在集合
        eex_index = []
        if len(attribute_index[i]) == 1:
            #只有extension 1
            n_existence_index.append(ex_index)
            continue
        else:
            for j in range(len(attribute_index[i][1])): #遍历extension2
                #extension2的属性存在为0
                eeex_index = []
                if len(attribute_index[i][1][j]) == 1:
                    #只有extension 2
                    eex_index.append([0])
                else: 
                    #该extension2下有一些extension3
                    eeex_index = [0]
                    eeeex_index = []
                    for k in range(len(attribute_index[i][1][j][1])): #遍历attribute_index[i][1][j]下的extension3集合
                        eeeex_index.append(0)
                    eeex_index.append(eeeex_index)
                    eex_index.append(eeex_index)
            ex_index.append(eex_index)
        n_existence_index.append(ex_index)
    print(n_existence_index)
    return(n_existence_index)
    

def fstr(fstring_text, vals):
    """Evaluate the provided fstring_text."""
    ret_val = eval(f"""f'''{fstring_text}'''""", vals)
    return ret_val

def ask(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",#选择模型
        messages=[
            {"role":"system","content":""},#指定模型的角色
            {"role":"user","content":prompt}#加入自己的prompt
        ],
    )
    ans = response.choices[0].message.content
    return ans #模型的回复


def create_initial_node(material_label, method_label, product):
    #attribute_1从extension_1里选择一个
    #attribute_2从extension_2里选择一个
    index_1 = random.randint(0, len(attribute_index)-1)
    #print(index_1)
    #print(existence_index)
    attribute_1 = attribute_index[index_1][0].lstrip()
    vals_1 = {
            "method_label": method_label,
            "extension_1": attribute_1
        }
    if len(attribute_index[index_1]) == 1:
        existence_index[index_1][0] = 2
        #为2 后面没有列表即全部选中
        vals = {
            "method_label": method_label,
            "material_label": material_label,
            "product": product,
            "candidate_statement": "",
            "method_statement": fstr(method_statement, vals_1),
            "extension_1_statement": "",
            "extension_2_statement": ""
        }
    else:
        if len(existence_index[index_1][1]) == 1:
            existence_index[index_1][0] = 2
            #为2 后面列表只有1个，直接全部选中
        else:
            existence_index[index_1][0] = 1
            #为1 代表后面的列表有元素被选中
        index_2 = random.randint(0, len(attribute_index[index_1][1])-1)
        attribute_2 = attribute_index[index_1][1][index_2][0].lstrip()
        vals_2 = {
            "extension_1": attribute_1,
            "extension_2": attribute_2
        }
        if len(attribute_index[index_1][1][index_2]) == 1: #没有extension3
            #print(index_1)
            #print(index_2)
            existence_index[index_1][1][index_2][0] = 2
            vals = {
                "method_label": method_label,
                "material_label": material_label,
                "product": product,
                "candidate_statement": "",
                "method_statement": fstr(method_statement, vals_1),
                "extension_1_statement": fstr(extension_text_1, vals_2),
                "extension_2_statement": ""
            }
        else: #有extension3
            if len(attribute_index[index_1][1][index_2][1]) == 1:
                existence_index[index_1][1][index_2][0] = 2
            else:
                existence_index[index_1][1][index_2][0] = 1
            index_3 = random.randint(0, len(attribute_index[index_1][1][index_2][1])-1)
            attribute_3 = attribute_index[index_1][1][index_2][1][index_3].lstrip()
            existence_index[index_1][1][index_2][1][index_3] = 1
            vals_3 = {
                "extension_2": attribute_2,
                "extension_3": attribute_3
            }
            vals = {
                "method_label": method_label,
                "material_label": material_label,
                "product": product,
                "candidate_statement": "",
                "method_statement": fstr(method_statement, vals_1),
                "extension_1_statement": fstr(extension_text_1, vals_2),
                "extension_2_statement": fstr(extension_text_2, vals_3)
            }
    template_prompt = fstr(fstring_text, vals)
    print(template_prompt)
    #answer = ask(template_prompt)
    #print(answer)
    #print(parse_answer(answer))
    answer = "a, b, c, d, e"
    return answer


def create_leaf_node(answer, index, material_label, method_label, product, options):
    answer_list = parse_answer(answer)
    fl = len(answer_list)
    if fl < 5:
        for ai in range(5-fl):
            answer_list.append('')
    if index == 7:
        print(answer_list)
    else:
        #随机选择下一个next_attribute，且前文没有
        index_1 = random.randint(0, len(attribute_index) - 1)
        while existence_index[index_1][0] == 2:
            index_1 = random.randint(0, len(attribute_index) - 1)
        #print("extension 1 is successfully chosen! It's " + str(attribute_index[index_1][0]))
        attribute_1 = ""
        if len(attribute_index[index_1]) == 1:
            existence_index[index_1][0] = 2
        else:
            index_2 = random.randint(0, len(attribute_index[index_1][1])-1)
            attribute_2 = attribute_index[index_1][1][index_2][0].lstrip()
            #print(existence_index[index_1][1][index_2])
            while existence_index[index_1][1][index_2][0] == 2:
                index_2 = random.randint(0, len(attribute_index[index_1][1])-1)
            #print("extension 2 is successfully chosen!")
            #print(index_1)
            #print(index_2)
            attribute_2 = ""
            if len(attribute_index[index_1][1][index_2]) == 1:
                existence_index[index_1][1][index_2][0] = 2
            else:
                if len(attribute_index[index_1][1][index_2][1]) == 1:
                    existence_index[index_1][1][index_2][0] = 2
                else:
                    existence_index[index_1][1][index_2][0] = 1
                index_3 = random.randint(0, len(attribute_index[index_1][1][index_2][1])-1)
                while existence_index[index_1][1][index_2][1][index_3] == 1:
                    index_3 = random.randint(0, len(attribute_index[index_1][1][index_2][1])-1)
                existence_index[index_1][1][index_2][1][index_3] = 1
            #更新extension_1的exsitence
            if existence_index[index_1][0] == 0:
                if len(existence_index[index_1][1]) == 1 and existence_index[index_1][0] == 2:
                    existence_index[index_1][0] = 2
                else:
                    existence_index[index_1][0] = 1
            else:
                element_flag = 0
                for element in existence_index[index_1][1]:
                    if len(element) == 1:
                        continue
                    if element[0] == 0:
                        if len(element[1]) == 1:
                            if element[1][0] == 1:
                                element[0] == 2
                        else:
                            element1_flag = 0
                            for element_1 in element[1]:
                                if element_1 == 1:
                                    element1_flag = 1
                                    break
                            if element1_flag == 1:
                                element[0] = 1
                    else:
                        element2_flag = 0
                        for element_2 in element[1]:
                            if element_2 == 0:
                                element2_flag = 1
                                break
                        if element2_flag == 0:
                            element[0] = 2
                    if element[0] != 2:
                        element_flag = 1
                        break
                if element_flag == 0:
                    existence_index[index_1][0] = 2
        #print(existence_index)
        #重新制定template
        extension_1_template = ""
        extension_2_template = ""
        i_flag = 0
        for i in range(len(existence_index)):
            if existence_index[i][0] != 0:
                if i_flag == 0:
                    attribute_1 = attribute_1 + attribute_index[i][0].lstrip()
                    i_flag = 1
                else:
                    attribute_1 = attribute_1 + " or " + attribute_index[i][0].lstrip()
                if len(existence_index[i]) != 1:
                    j_flag = 0
                    attribute_2 = ""
                    for j in range(len(existence_index[i][1])):
                        if existence_index[i][1][j][0] != 0:
                            if j_flag == 0:
                                attribute_2 = attribute_2 + attribute_index[i][1][j][0].lstrip()
                                j_flag = 1
                            else:
                                attribute_2 = attribute_2 + " or " + attribute_index[i][1][j][0].lstrip()
                            if len(existence_index[i][1][j]) != 1:
                                k_flag = 0
                                attribute_3 = ""
                                for k in range(len(existence_index[i][1][j][1])):
                                    if existence_index[i][1][j][1][k] == 1:
                                        if k_flag == 0:
                                            attribute_3 = attribute_3 + attribute_index[i][1][j][1][k].lstrip()
                                            k_flag = 1
                                        else:
                                            attribute_3 = attribute_3 + " or " + attribute_index[i][1][j][1][k].lstrip()
                                vals_3 = {
                                    "extension_2": attribute_index[i][1][j][0],
                                    "extension_3": attribute_3
                                }
                                extension_2_template = extension_2_template + " " + fstr(extension_text_2, vals_3)

                    vals_2 = {
                        "extension_1": attribute_index[i][0],
                        "extension_2": attribute_2
                    }
                    extension_1_template = extension_1_template + " " + fstr(extension_text_1, vals_2)
        vals_1 = {
            "method_label": method_label,
            "extension_1": attribute_1
        }
        answer_string = answer_list[0]
        for i in range(1, len(answer_list)):
            answer_string += ", " + answer_list[i]
        val_can = {
            "candidate_list": answer_string
        }
        candidate_template = fstr(candidate_statement, val_can)
        if options == "montecarlo":
            vals = {
                "method_label": method_label,
                "material_label": material_label,
                "product": product,
                "candidate_statement": candidate_template,
                "method_statement": fstr(method_statement, vals_1),
                "extension_1_statement": extension_1_template,
                "extension_2_statement": extension_2_template
            }
        elif options == "base":
            vals = {
                "method_label": method_label,
                "material_label": material_label,
                "product": product,
                "candidate_statement": "",
                "method_statement": fstr(method_statement, vals_1),
                "extension_1_statement": extension_1_template,
                "extension_2_statement": extension_2_template
            }
        template_prompt = fstr(fstring_text, vals)
        print(template_prompt)
        if index == 5:
            #print("yesyes")
            new_answer = ask(template_prompt)
            #print(new_answer)
            return new_answer
            #new_answer = "a, b, c, d, e"
        else:
            new_answer = "a, b, c, d, e"
            return new_answer

#initiaize_tree_attribute("data/method_classification_composite.csv")
#attribute_index = [['carbon', [['reduced graphene oxide'], [' graphene'], [' carbon nanotube']]], ['metal', [['Cu'], [' Ag'], [' Au'], [' Zn'], [' Bi'], [' Pd'], [' Cd'], [' Co'], [' In'], [' Ni'], [' Pb'], [' Sb'], [' Sn']]], ['metal oxide', [['EOx', ['CuO', ' Cu2O', ' CuxO', ' Cu/CuO', ' Cu/Cu2O', ' Cu/CuxO', ' Cu2O/CuO']], ['EOx+MOx', ['CuO/SnO2', ' CuO/ZnO', ' CuO/ZnOx', ' CuO/InOx', ' CuO/Co3O4', ' CuO/Sb2O3', ' CuO/ZrO2', ' CuO/In2O3', ' Cu2O/ZnO', ' Cu2O/AgOx']], ['E+MOx', ['Ag/Cu2O', ' Au/Cu2O', ' Cu/CeO2', ' Cu/In2O3', ' Cu/TiO2', ' Cu/ZnO', ' Cu/ZnOx', ' Ag/CuO', ' Cu/SnO2', ' Ni/Cu2O', ' Sn/Cu2O', ' Ag/Cu2O']]]], ['metal sulfide', [['CuS'], [' Cu2S'], [' Cu1.96S']]], ['MOF'], ['molecular complex'], ['metal iodide'], ['metal nitride'], ['metal selenide']]
attribute_index = [['composition control', [['content', ['uniform Cu-Ag bimetallic electrocatalysts with concisely tuned atomic ratio', ' porous In-Cu bimetallic oxide catalysts with various Cu/In ratios', ' controlling the Cu/Bi molar ratio', ' Nitrogen-doped mesoporous carbon supported CuSb (Cu: 5.9 wt%, Sb: 0.49 wt%)', ' Ag15Cu85 (15 at% Ag, 85 at% Cu)']], ['substance', ['CuxOyCz\xa0nanostructured electrocatalysts derived from a Cu-based MOF as porous self-sacrificial template', ' Nanostructured CuxPd100-x', ' a sulfur-doped Cu2O-derived Cu catalyst', ' bimetallic Bi3Cu1\xa0catalyst', ' mesoporous foams with Cu10Sn surface composition']]]], ['phase control', [['a chloride (Cl)-induced bi-phasic cuprous oxide (Cu2O) and metallic copper (Cu) electrode (Cu2OCl)'], ['Phase and structure modulating of bimetallic CuSn nanowires'], ['phase-blended Ag-Cu2O'], ['The phase-separated CuPd and Cu3Pd'], ['the selectivity, the reversibility, and the reactivity for CO or HCOOH production strongly depended on the microcrystalline phase']]], ['facet control', [['Cu', ['Cu (001)', ' Cu (100)', ' Cu (100)(110)', ' Cu (100)(110)(111)', ' Cu (100)(111)', ' Cu (110)', ' Cu (111)', ' Cu (111)(200)', ' Cu (220)', ' Cu (200)', ' Cu (310)']], ['Cu2O', ['Cu2O (100) (111)', ' Cu2O (100)', ' Cu2O (110)', ' Cu2O (511)', ' Cu2O (111)', ' Cu2O (111)(211)']]]], ['size control', [['edge', ['Cu nanocubes with 44nm edge length']], ['pore', ['two types of distinct pores (~320 nm and ~20 nm) and adjustable alloy compositions', ' mesoporous Cu catalysts with the particular surface pore size of\xa0between 50 and 100 μm pore diameters']], ['diameter', ['irregular Cu nanoparticles of around 20\u2005nm in diameter']], ['thickness', ['the catalytic selectivity of the Cu/p-Sn catalysts shifted from CO to HCOOH as the thickness of the Sn pattern increased from 3 to 50 nm', ' Polycrystalline Cu with an average thickness of ~950 nm was coated via sputtering, while Cu2O and CuO films were electrodeposited onto gas diffusion layer with average thickness of ~840 nm and ~850 nm, respectively', ' hollow Au-Cu nanoparticles of size ranging from 50 nm to 100 nm with a wall thickness of 4.95 ± 0.81 nm']], ['ligament', ['nanoporous copper (NPC) film with a ligament size of 35 ± 6 nm\xa0']], ['ligand side groups', ['changing the size of ligand side groups']], ['size', ['The catalyst with nanowires less than 2.3 µm', ' Cu cubes of 44 nm', ' CuO nanorods in the ~10 nm size range', ' metallic copper (Cu) and silver (Ag) nanoparticles with a narrow size distribution (<10%)', ' Cu2-xS nanosheets (C-nano-0, 100 nm lateral dimension, 14 nm thick)', ' Cu nanoparticle size (ranging from 25–80 nm)']]]], ['morphology control', [['array'], ['cube'], ['film'], ['foam'], ['prism'], ['surface construction'], ['hollow'], ['heterostructure'], ['hierarchical structure'], ['microstructure', ['microsphere', ' microbrush', ' rice spike-like microstructure']], ['nanostructure', ['nanostructure', ' nanobundle', ' nanocone', ' nanocoral', ' nanocrystal', ' nanocube', ' nanofiber', ' nanofibrous', ' nanoflower', ' nanoneedle', ' nanoparticle', ' nanorod', ' nanoplate', ' nanopore', '  nanopyramidal', ' nanosheet', ' nanosphere', ' nanowire']]]], ['3D structure', [['3D hierarchical structure'], ['3D electrode'], ['3D interconnected structure'], ['3D porous structure'], ['3D Self-Supporting Aerogels'], ['3D array structure'], ['3D dendritic structure'], ['3D morphology of copper growth on CNT sheets'], ['3D architecture of the electrodeposited Cu-Pd bimetallic catalysts'], ['3D cuboids form with flat and smooth faces'], ['3D nanocones']]], ['core-shell structure', [['Hierarchical Sn-Cu/SnOx Core/Shell Catalyst'], ['Ag Core/Porous Cu Shell Nanoparticles'], ['The catalyst Cu1Sn1 with a CuSn alloy core and a SnO shell structure doped with a small amount of Cu'], ['3D core-shell porous-structured Cu@Sn hybrid electrodes'], ['Cu(core)/CuO(shell) Catalyst'], ['a series of Ag@Cu NPs are tuned from the Ag core, Cu modified Ag, to the Cu outer shell']]], ['dendritic structure', [['nanodendrites'], ['An electrode design with dendritic morphological features'], ['micro-structured dendritic'], ['dendritic structures with low porosity'], ['from round to flower-like shapes accompanied by a decrease in branch size of the dendritic structure'], ['needle-like dendritic structure'], ['dendritic catalysts on mesh supports'], ['porous dendritic structure']]], ['porous structure', [['mesoporous', ['mesoporous nanoribbons', ' mesoporous nanostructures', ' rich mesoporous structure', ' Planar Mesoporous']], ['nanoporous', ['nanoporous\xa0film', ' nanoporous hollow tandem', ' submicron-sized nanoporous']], ['porous', ['Interconnected Porous Aerogel', ' Highly Porous', ' porous aerogel', ' ordered porous', ' porous nanoparticle', ' porous nanosphere', ' porous film', ' porous foam', ' particles form a porous octahedral structure', ' The nanocatalyst exhibits porous/sponge-like morphology']]]]]
# print(attribute_index)
initiaize_tree_existence(attribute_index)
#print(create_leaf_node(test_vals, 'a', 2))
ii = 0
csv_file = open('output_base_data/answer_structure_corpus.csv','a', newline='',encoding='utf-8') # 调用open()函数打开csv文件，传入参数：文件名“demo.csv”、写入模式“w”、newline=''、encoding='utf-8'。
writer = csv.writer(csv_file) # 用csv.writer()函数创建一个writer对象。
for material_label in materials:
    for product in products:
        existence_index = initiaize_tree_existence(attribute_index)
        # print(attribute_index)
        #print(ii)
        ii += 1
        # if ii <= 85:
        #     continue
        answer_final = create_initial_node(material_label, "structure control", product)
        tree_index = 1
        while tree_index < 5:
            tree_index += 1
            print("Now this is list " + str(ii)+ " and the tree'deepth is " + str(tree_index))
            new_answer = create_leaf_node(answer_final, tree_index, material_label, "structure control", product, "base")
            answer_final = new_answer
        #full_answer.append(answer_final)
        final_list = parse_answer(answer_final)
        fl = len(final_list)
        if fl < 5:
            for ai in range(5-fl):
                final_list.append('')
        print(final_list)
        writer.writerow([material_label, product, "structure control", final_list[0], final_list[1], final_list[2], final_list[3], final_list[4], answer_final]) # 调用writer对象的writerow()方法
csv_file.close() # 写入完成后，关闭文件