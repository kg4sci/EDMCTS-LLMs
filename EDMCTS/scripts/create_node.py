from openai import OpenAI
import pandas as pd
import numpy as np
import math
import random
from ast import literal_eval
import csv #导入csv模块
import json
from optimization import select_1, select_2


client = OpenAI(
base_url="https://35api.huinong.co/v1",#中转api，如果直接用openai的key则不需要加这一行
api_key="sk-370NTtQbjaVJzzxxD281Ed2013Ee40279dB23c1218A5A742"
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
#materials = ["Cu", "Cu/C", "CuOx", "CuSx", "CuNx", "Cu-M", "CuMOx", "Cu-MOF", "Cu(Ox)-M(OH)x", "CuMSx", "CuPx", "M+CuOx", "Cu-MXene", "Cu-MOx", "Cu molecular complex", "CuI", "CuSex", "CuOx-MOx", "Cu-MSx"]
#materials = ["Cu-MOF", "Cu(Ox)-M(OH)x", "CuMSx", "CuPx", "M+CuOx", "Cu-MXene", "Cu-MOx", "Cu molecular complex", "CuI", "CuSex", "CuOx-MOx", "Cu-MSx"]
#materials = ["Cu", "Cu-M"]
materials = ["Cu/C"]
#products = ["ethylene", "ethanol"]
products = ["ethanol"]
#products = ["carbon monoxide", "formate", "ethylene", "ethanol"]
fstring_text = (
        "Generate a list of top-5 {method_label} "
        "for {material_label} to produce {product}. "
        "{material_statement}"
        "When recommending the regular method {method_label}, you need to take into account the specificity of the material {material_label} and the product {product}. "
        "{candidate_statement}"
        "{method_statement}"
        "{extension_statement}"
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

def parse_answer(answer: str, num_expected=None):
    """Parse an answer into a list."""
    if answer is None:
        answer_list = ['', '', '', '', '']
        return [json.dumps(ans).replace('"', "").replace("'", "").strip() for ans in answer_list]
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

# def initiaize_tree_attribute(input_path):
#     method_classification = pd.read_csv(input_path)
#     extension_1 = method_classification["extension_1"]
#     extension_2 = method_classification["extension_2"]
#     for i in range(len(extension_1)-1):
#         a1 = extension_1[i]
#         att_index = [a1]
#         if pd.notnull(extension_2[i]):
#             att_index.append(extension_2[i].split(';'))
#         attribute_index.append(att_index)
#     print(attribute_index)

def initiaize_tree_attribute(input_path):
    method_classification = pd.read_csv(input_path)
    extension_1 = method_classification["extension_1"]
    extension_2 = method_classification["extension_2"]
    att_index = [extension_1[0]]
    attt_index = [extension_2[0]]
    i = 1
    #print(len(extension_1))
    while i < 12:
    # while i < 21:
    # while i < 45:
    # while i < 56:
        if pd.notnull(extension_1[i]) or i == 11:
        # if pd.notnull(extension_1[i]) or i == 20:
        # if pd.notnull(extension_1[i]) or i == 44:
        # if pd.notnull(extension_1[i]) or i == 55:
            att_index.append(attt_index)
            attribute_index.append(att_index)
            att_index = [extension_1[i]]
            attt_index = [extension_2[i]]
        else:
            attt_index.append(extension_2[i])
        i = i + 1
    print(attribute_index)

def initiaize_tree_existence(attribute_index):
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
    

def fstr(fstring_text, vals):
    """Evaluate the provided fstring_text."""
    ret_val = eval(f"""f'''{fstring_text}'''""", vals)
    return ret_val

def ask(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",#选择模型
        messages=[
            {"role":"system","content":"You are a helpful chemistry expert with extensive knowledge of catalysis. You will give recommendations for regulation methods, which refer to the structural regulation manner of the catalysts. Make specific recommendations for regulation methods, including the detailed regulation manner of the catalyst. Make sure to follow the formatting instructions. Do not provide disclaimers or notes about your knowledge of catalysis."},#指定模型的角色
            {"role":"user","content":prompt}#加入自己的prompt
        ],
    )
    ans = response.choices[0].message.content
    return ans #模型的回复


def create_initial_node(material_label, method_label, product):
    #attribute_1从extension_1里选择一个
    #attribute_2从extension_2里选择一个
    #index_1 = random.randint(0, len(attribute_index)-1)
    index_1 = select_1(material_label, method_label, product, attribute_index, 2)
    print(index_1)
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
            "extension_statement": ""
        }
    else:
        if len(existence_index[index_1][1]) == 1:
            existence_index[index_1][0] = 2
            #为2 后面列表只有1个，直接全部选中
        else:
            existence_index[index_1][0] = 1
            #为1 代表后面的列表有元素被选中
        index_2 = select_2(material_label, method_label, product, attribute_index, 2, index_1)
        attribute_2 = attribute_index[index_1][1][index_2].lstrip()
        existence_index[index_1][1][index_2] = 1
        vals_2 = {
            "extension_1": attribute_1,
            "extension_2": attribute_2
        }
        material_template = ""
        if material_label == "Cu-M" or material_label == "M+CuOx":
            material_template = "M denotes a metal except Cu. "
        elif material_label == "Cu-MOx" or material_label == "CuMOx" or material_label == "CuOx-MOx":
            material_template = "MOx denotes a metal oxide except CuOx. "
        elif material_label == "CuMSx" or material_label == "Cu-MSx":
            material_template = "MSx denotes a metal sulfide except CuSx. "
        elif material_label == "Cu(Ox)-M(OH)x":
            material_template = "M(OH)x denotes a metal hydroxide. "
        vals = {
            "method_label": method_label,
            "material_label": material_label,
            "product": product,
            "material_statement": material_template,
            "candidate_statement": "",
            "method_statement": fstr(method_statement, vals_1),
            "extension_statement": fstr(extension_text_1, vals_2)
        }
    template_prompt = fstr(fstring_text, vals)
    print(template_prompt)
    #answer = ask(template_prompt)
    #print(answer)
    #print(parse_answer(answer))
    #answer = "a, b, c, d, e"
    answer = ask(template_prompt)
    print(answer)
    return answer


def create_leaf_node(answer, index, material_label, method_label, product, option):
    #print(answer)
    answer_list = parse_answer(answer)
    fl = len(answer_list)
    if fl < 5:
        for ai in range(5-fl):
            answer_list.append('')
    else:
        #随机选择下一个next_attribute，且前文没有
        index_1 = select_1(material_label, method_label, product, attribute_index, 2)
        print(index_1)
        index_first = 0
        while existence_index[index_1][0] == 2:
            index_first += 1
            if index_first > 6:
                index_1 = random.randint(0, len(attribute_index) - 1)
            else:
                index_1 = select_1(material_label, method_label, product, attribute_index, 2)
        #print("extension 1 is successfully chosen! It's " + str(attribute_index[index_1][0]))
        attribute_1 = ""
        if len(attribute_index[index_1]) == 1:
            existence_index[index_1][0] = 2
        else:
            #index_2 = random.randint(0, len(attribute_index[index_1][1])-1)
            index_2 = select_2(material_label, method_label, product, attribute_index, 2, index_1)
            print(index_2)
            attribute_2 = attribute_index[index_1][1][index_2].lstrip()
            index_second = 0
            while existence_index[index_1][1][index_2] == 1:
                index_second += 1
                if index_second > 6:
                    index_2 = random.randint(0, len(attribute_index[index_1][1])-1)
                else:
                    index_2 = select_2(material_label, method_label, product, attribute_index, 2, index_1)
                #index_2 = random.randint(0, len(attribute_index[index_1][1])-1)
            #print("extension 2 is successfully chosen!")
            existence_index[index_1][1][index_2] = 1
            #更新extension_1的exsitence 
            if existence_index[index_1][0] == 0:
                if len(existence_index[index_1][1]) == 1:
                    existence_index[index_1][0] = 2
                else:
                    existence_index[index_1][0] = 1
            else:
                element_flag = 0
                for element in existence_index[index_1][1]:
                    if element == 0:
                        element_flag = 1
                        break
                if element_flag == 0:
                    existence_index[index_1][0] = 2
        #print(existence_index)
        #重新制定template
        extension_template = ""
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
                        if existence_index[i][1][j] == 1:
                            if j_flag == 0:
                                attribute_2 = attribute_2 + attribute_index[i][1][j].lstrip()
                                j_flag = 1
                            else:
                                attribute_2 = attribute_2 + " or " + attribute_index[i][1][j].lstrip()
                    vals_index = {
                        "extension_1": attribute_index[i][0],
                        "extension_2": attribute_2
                    }
                    extension_template = extension_template + " " + fstr(extension_text_1, vals_index)
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
        material_template = ""
        if material_label == "Cu-M" or material_label == "M+CuOx":
            material_template = "M denotes a metal except Cu. "
        elif material_label == "Cu-MOx" or material_label == "CuMOx" or material_label == "CuOx-MOx":
            material_template = "MOx denotes a metal oxide except CuOx. "
        elif material_label == "CuMSx" or material_label == "Cu-MSx":
            material_template = "MSx denotes a metal sulfide except CuSx. "
        elif material_label == "Cu(Ox)-M(OH)x":
            material_template = "M(OH)x denotes a metal hydroxide. "
        if option == "montecarlo":
            vals = {
                "method_label": method_label,
                "material_label": material_label,
                "product": product,
                "material_statement": material_template,
                "candidate_statement": candidate_template,
                "method_statement": fstr(method_statement, vals_1),
                "extension_statement": extension_template
            }
        elif option == "base":
            vals = {
                "method_label": method_label,
                "material_label": material_label,
                "product": product,
                "material_statement": material_template,
                "candidate_statement": "",
                "method_statement": fstr(method_statement, vals_1),
                "extension_statement": extension_template
            }
        template_prompt = fstr(fstring_text, vals)
        print(template_prompt)
        # if index == 5:
        #     #print("yesyes")
        #     new_answer = ask(template_prompt)
        #     print(new_answer)
        #     return new_answer
        #     #new_answer = "a, b, c, d, e"
        # else:
        #     new_answer = "a, b, c, d, e"
        #     return new_answer
        #new_answer = "a, b, c, d, e"
        new_answer = ask(template_prompt)
        print(new_answer)
        return new_answer

initiaize_tree_attribute("data/atomic level dispersion.csv")
# initiaize_tree_existence(attribute_index)
# print(create_leaf_node(test_vals, 'a', 2))
ii = 0
# csv_file = open('output_ToT_data/test.csv','a',newline='',encoding='utf-8') # 调用open()函数打开csv文件，传入参数：文件名“demo.csv”、写入模式“w”、newline=''、encoding='utf-8'。
# writer = csv.writer(csv_file) # 用csv.writer()函数创建一个writer对象。
for material_label in materials:
    for product in products:
        existence_index = initiaize_tree_existence(attribute_index)
        #print(existence_index)
        #print(existence_index[3][0])
        #print(ii)
        ii += 1
        # if ii < 53:
        #     continue
        answer_final = create_initial_node(material_label, "atomic level dispersion", product)
        tree_index = 1
        while tree_index < 5:
            tree_index += 1
            print("Now this is list " + str(ii)+ " and the tree'deepth is " + str(tree_index))
            new_answer = create_leaf_node(answer_final, tree_index, material_label, "atomic level dispersion", product, "montecarlo")
            answer_final = new_answer
        #full_answer.append(answer_final)
        print(answer_final)
        # final_list = parse_answer(answer_final)
        # fl = len(final_list)
        # if fl < 5:
        #     for ai in range(5-fl):
        #         final_list.append('')
        # print(final_list)
#         writer.writerow([material_label, product, "surface/interface modification", final_list[0], final_list[1], final_list[2], final_list[3], final_list[4], answer_final]) # 调用writer对象的writerow()方法
# csv_file.close() # 写入完成后，关闭文件