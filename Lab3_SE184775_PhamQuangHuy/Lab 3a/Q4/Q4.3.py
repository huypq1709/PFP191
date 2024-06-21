"""3.	Remove empty strings from a list of strings"""
def remove_empty(str_list):
    res_list = []
    for s in str_list:
        if s:
            res_list.append(s)
    return res_list
if __name__ == "__main__":
    str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    print(f"Output: {remove_empty(str_list)}")