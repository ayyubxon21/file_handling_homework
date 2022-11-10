def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    for i in data:
        if i.isalpha():
            list.append(i)
            list.extend('\n')
    return list
print(main(open('txt_file/data04.txt').read()))
    
# Read data from file