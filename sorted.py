def sort_dictionary(inputDict):
    if not isinstance(inputDict, dict):
        return "Input should be a dictionary."

    # sort the dictionary by keys in reverse order
    sortedDict = dict(sorted(inputDict.items(), key=lambda x: x[0], reverse=True))

    # create a list of tuples with the sorted keys and phone numbers
    result = [(name, data[0]) for name, data in sortedDict.items()]

    return result
