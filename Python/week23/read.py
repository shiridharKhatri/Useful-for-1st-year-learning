def listValue(path="file.txt"):
    '''
    This method read the file.txt and returns the 2d list in a tabular
    input : file path:str
    return : 2d list: list[list[str]]
    '''
    file = open(f'week23/{path}')
    fileData = file.readlines()
    file.close()
    personData = []
    for elems in fileData:
        personData.append(elems.strip().split(','))
    return personData

if __name__ == "__main__":
    listValue()