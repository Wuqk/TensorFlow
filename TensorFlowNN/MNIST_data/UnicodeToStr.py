def ncr_to_unicode(text):
    """
    用于将&#21271;&#20140;这类NCR（numeric character reference）字符串转换为unicode串
    :param text: NCR strings such as "&#24050;&#36716;&#20986;"
    :return: unicode strings such as "\u5df2\u8f6c\u51fa"
    usage: print print unicode(ncr_to_unicode(code), 'unicode-escape')
    """
    l_word = text[:-1].split(';')
    string = ""
    for word in l_word:
        word = word[2:]
        word_hex = hex(int(word))
        string += ''.join([chr(i) for i in [int(b, 16) for b in word_hex.split(' ')]])
    return string

if __name__ == '__main__':
    ncr_to_unicode("&#30005;&#21147;&#24033;&#26816;")