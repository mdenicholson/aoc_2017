import pprint

with open("input_day_7") as f:
    entries = f.readlines()
    input_dict = {}
    for item in entries:
        data_parts = [x.replace(",","") for x in item.split()]
        input_dict[data_parts[0]] = {"weight":int(data_parts[1].replace("(","").replace(")","")),"children":data_parts[3:]}

def add_parents(input_dict):
    for program in input_dict:
        if len(input_dict[program]["children"]) > 0:
            for child in input_dict[program]["children"]:
                input_dict[child]["parent"] = program
    return input_dict

full_tree = add_parents(input_dict)

for program in full_tree:
    if "parent" not in full_tree[program].keys():
        tree_root = program
        print "Root is: ", program


def add_depth(input_dict,root,depth):
    input_dict[root]["depth"] = depth
    new_dict = input_dict.copy()
    for child in input_dict[root]["children"]:
        new_dict = add_depth(new_dict,child,depth + 1)
    return new_dict

def add_cumulative_weight(input_dict,depth):
    if depth == 1:
        return input_dict
    for program in input_dict:
        if input_dict[program]["depth"] == depth:
            parent = input_dict[program]["parent"]
            input_dict[parent]["cum_weight"] += input_dict[program]["cum_weight"]
    return add_cumulative_weight(input_dict,depth - 1)

dict_with_depth = add_depth(input_dict,tree_root,1)

max_depth = 0
for program in dict_with_depth:
    dict_with_depth[program]["cum_weight"] = dict_with_depth[program]["weight"]
    if dict_with_depth[program]["depth"] > max_depth:
        max_depth = dict_with_depth[program]["depth"]

dict_with_cum_weight = add_cumulative_weight(dict_with_depth,max_depth)

def check_balance(input_dict):
    for program in input_dict:
        balance = True
        if input_dict[program]["children"] != []:
            first_weight_above = input_dict[input_dict[program]["children"][0]]["cum_weight"]
            for child in input_dict[program]["children"]:
                if input_dict[child]["cum_weight"] != first_weight_above:
                    balance = False
        input_dict[program]["balance"] = balance
    return input_dict

dict_with_balance = check_balance(dict_with_cum_weight)

def extract_unbalanced(input_dict):
    unbalanced_dict = {}
    for program in input_dict:
        if not input_dict[program]["balance"]:
            unbalanced_dict[program] = input_dict[program]
    return unbalanced_dict


unbalanced_dict = extract_unbalanced(dict_with_balance)

max_unbalanced_depth = 0
for program in unbalanced_dict:
    cur_depth = unbalanced_dict[program]["depth"] 
    if cur_depth > max_unbalanced_depth:
        max_unbalanced_depth = cur_depth
        max_depth_prog = program

pprint.pprint(unbalanced_dict[max_depth_prog])
pprint.pprint(dict_with_balance[dict_with_balance[max_depth_prog]["parent"]])
for child in unbalanced_dict[max_depth_prog]["children"]:
    print(child)
    pprint.pprint(dict_with_balance[child])
    for grandchild in dict_with_balance[child]["children"]:
        print grandchild, dict_with_balance[grandchild]["cum_weight"]

