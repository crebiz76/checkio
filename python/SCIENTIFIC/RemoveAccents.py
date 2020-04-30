import unicodedata

def checkio(in_string):
    "remove accents"
    result = ''
    for uc in unicodedata.normalize('NFKD', in_string):
        if unicodedata.category(uc) != 'Mn':
            ret = ''.join(uc)
            result += ret
    print(result)
    return result

    # result = ''
    # for in_string in unicodedata.normalize('NFKD', in_string):
    #     if unicodedata.category(in_string) != 'Mn':
    #         ret = ''.join(in_string)
    #         result += ret
    # print(result)
    # return result

    # ret = ''.join(in_string for in_string in 
    #                 unicodedata.normalize('NFKD', in_string) 
    #                 if unicodedata.category(in_string) != 'Mn')
    # print(ret)
    # return ret
    

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
