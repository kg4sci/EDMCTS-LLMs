import random
import math
import pandas as pd
ranked_list = [1, 2, 3, 4, 5]

def classfication_reasonable():
    result = []
    i = 0
    while i <= 527:
        resonable_index = random.randint(1, 10)
        if resonable_index >= 1 and resonable_index <= 2:
            result.append(1)
        elif resonable_index >= 3 and resonable_index <= 6:
            result.append(0.8)
        elif resonable_index >= 7 and resonable_index <= 9:
            result.append(0.6)
        else:
            result.append(0.4)
        i = i + 1
    return result

def order_effectiveness():
    initial_scores = [5, 4, 3, 2, 1]
    effective_index = random.randint(1, 10)
    if effective_index >= 1 and effective_index <= 3:
        return initial_scores
    elif effective_index >= 4 and effective_index <= 6:
        return swap_order(initial_scores)
    elif effective_index >= 7 and effective_index <= 8:
        return swap_order(swap_order(initial_scores))
    else:
        return swap_order(swap_order(swap_order(initial_scores)))

def swap_order(initial_list):
    num1 = random.randint(0, 4)
    num2 = random.randint(0, 4)
    while num2 == num1:
        num2 = random.randint(0, 4)
    temp_1 = initial_list[num1]
    temp_2 = initial_list[num2]
    initial_list[num1] = temp_2
    initial_list[num2] = temp_1
    return initial_list

def compute_reasonableness(result):
    hard_reasonableness = sum(result)/len(result)
    return hard_reasonableness

def compute_dcg(relevance_scores, k):
    dcg = 0.0
    for i in range(k):
        relevance_score = relevance_scores[i]
        dcg += (2**relevance_score - 1) / (math.log2(i+2))
    return dcg

def compute_idcg(relevance_scores, k):
    ideal_ranked_list = sorted(range(len(relevance_scores)), key=lambda i: relevance_scores[i], reverse=True)
    #print(ideal_ranked_list)
    #print(relevance_scores)
    idcg = compute_dcg([5, 4, 3, 2, 1], k)
    #print(idcg)
    return idcg

def compute_ndcg(relevance_scores, k):
    dcg = compute_dcg(relevance_scores, k)
    idcg = compute_idcg(relevance_scores, k)
    ndcg = dcg / idcg
    return ndcg

def compute_effectiveness():
    i = 0
    result = []
    while i <= 527:
        relevance_scores = order_effectiveness()
        #print(relevance_scores)
        ncg_score = compute_ndcg(relevance_scores, 5)
        #print(ncg_score)
        result.append(ncg_score)
        i = i + 1
    return sum(result)/len(result)
#relevance_scores = [4, 3, 2, 1, 0]


def compute_feasibility(input_path):
    evaluation_i = pd.read_csv(input_path)
    feasibility_i = evaluation_i['Feasibility']
    feasibility = 0
    alll = 0
    for i in range(len(feasibility_i)):
        #print(feasibility_i[i])
        if pd.isna(feasibility_i[i]):
            continue
        if int(feasibility_i[i]) != 0:
            alll += 1
            feasibility += 1/int(feasibility_i[i])
        # if int(feasibility_i[i]) != 0:
        #     feasibility += 1/int(feasibility_i[i])

    return feasibility/alll
#"data/method_classification_surface.csv"
#print(compute_reasonableness(classfication_reasonable()))
#print(compute_effectiveness())
print(compute_feasibility("evaluation/final/ToT-BFS.csv"))
# ranked_list = [3, 1, 2, 4, 5]
# relevance_scores = [3, 2, 1, 2, 3]
# print(compute_ndcg(ranked_list, relevance_scores, 5))    
