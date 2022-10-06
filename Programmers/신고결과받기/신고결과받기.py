
#Kakao
#Lv1
import copy
report_dict = dict()
declare_dict = dict()
num_dict = dict()
def solution(id_list, report, k):
    for id in id_list:
        id_list_copy = copy.deepcopy(id_list)
        id_list_copy.remove(id)
        num_dict[id] = id_list_copy
        declare_dict[id] = []
        report_dict[id] = 0
    for rep in report: 
        if rep.split()[1] in num_dict[rep.split()[0]] :
            num_dict[rep.split()[0]].remove(rep.split()[1])
            declare_dict[rep.split()[0]].append(rep.split()[1])
            report_dict[rep.split()[1]] +=1
        
    answer = []
    for id in id_list:
        if report_dict[id] < k:
            for id2 in id_list:
                if id in declare_dict[id2]:
                    declare_dict[id2].remove(id)
    for id in id_list:
        answer.append(len(declare_dict[id]))
    
    for id in id_list:
        if report_dict[id] >= k:
            return answer
    return [0]*len(id_list)
