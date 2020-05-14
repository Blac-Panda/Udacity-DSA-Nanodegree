import os


def find_file(suffix=None, path=None):
    if path == None:
        return "Input a path"
    elif suffix == None:
        return "Input suffix"
    result = []
    try:
        files = os.listdir(path)
    except Exception as e:
        return "Path not found"
    files = [os.path.join(path, file) for file in files]
    for file in files:
        if os.path.isfile(file) and file.endswith(suffix):
            result.append(file)
        if os.path.isdir(file):
            sub_result = find_file(suffix, file)
            result.extend(sub_result)
    return result


"""
    verify using test directory
"""
def run_testdir():
    suffix = ".c"
    path = "./testdir"
    
    print(find_file(suffix, path))

run_testdir()


print(find_file('.py', ""))                                                                  # Returns "Path not found"
print(find_file('.py'))                                                                      # Returns "Input a path"
print(find_file(path='/Desktop'))                                                            # Returns "Input suffix"
