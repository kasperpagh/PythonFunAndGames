def capitalCaser(streng):
    if type(streng) is not str:
        raise Exception("this function only accepts strings, you send: " + type(streng))
    print("did not stop...")
    return str.upper(streng)


def lowerCaser(streng):
    if type(streng) is not str:
        raise Exception("this function only accepts strings, you send: " + type(streng))
    print("did not stop...")
    return str.lower(streng)


