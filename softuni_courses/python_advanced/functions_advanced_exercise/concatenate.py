def concatenate(*args, **kwargs):
    word = ''.join(args)

    for k, v in kwargs.items():
        if k in word:
            word = word.replace(k, v)

    return word


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))