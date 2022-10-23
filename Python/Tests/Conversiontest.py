def convert(s):
    '''
    convert(<string>)
    Een string naar een integer converteren

    '''
    x = -1
    try:
        x = int(s)
        print("Conversion succeeded! x =", x)
    except (ValueError,TypeError):
        print("Conversion failed")

    return x
convert('12,1')