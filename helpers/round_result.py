def round_result(result):
    return_result = list()
    for a in result:
        return_result.append([round(x) for x in a])

    return return_result
