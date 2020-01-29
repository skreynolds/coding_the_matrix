def create_voting_dict():
    strlist = voting_data
    return {e.split()[0]:[int(e.split()[i]) \
                          for i in range(3,len(e.split()))] for e in strlist}

def policy_compare(sen_a, sen_b, voting_dict):
    return sum(voting_dict[sen_a][i]*voting_dict[sen_b][i] 
               for i in range(len(voting_dict[sen_a])))

def most_similar(sen, voting_dict):
    sen_agree = ""
    agree_val = -46
    for e in voting_dict.keys():
        if e != sen:
            if policy_compare(sen,e,voting_dict) >= agree_val:
                sen_agree = e
                agree_val = policy_compare(sen,e,voting_dict)
    return sen_agree

def least_similar(sen, voting_dict):
    sen_agree = ""
    agree_val = 46
    for e in voting_dict.keys():
        if e != sen:
            if policy_compare(sen,e,voting_dict) <= agree_val:
                sen_agree = e
                agree_val = policy_compare(sen,e,voting_dict)
    return sen_agree

for e in listoflists:
    great_ave_sen = ""
    great_ave_val = -46
    if find_average_similarity(e[0],democrat,voting_dict) >= great_ave_val:
        great_ave_sen = e[0]
        great_ave_val = find_average_similarity(e[0],democrat,voting_dict)
return great_ave_sen
