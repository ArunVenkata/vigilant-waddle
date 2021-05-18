def get_int(param, default=0):
    try:
        return int(param)
    except:
        return default