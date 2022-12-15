"""
You are given a list of files. You need to sort this list by the file extension.
The files with the same extension (or without one) should be sorted by name.

Some possible cases:

Filename cannot be an empty string;
Sorting order: files without name, files without extension, files with name and extension;
Filename ".config" or "config." is all name with an empty extension;
Filename like "str1.str2.str3" has an extension "str3" and a name "str1.str2";
Filename like ".str1.str2" has an extension "str2" and a name ".str1".
Input: List of strings.

Output: List of strings.
"""
def sort_by_ext(files: list[str]) -> list[str]:
    # define a custom key function to extract the file extension and name
    def key_func(file):
        # split the file name into the name and extension
        name, ext = file.rsplit('.', maxsplit=1)
        
        if name == "":
            return(0, ext)
        elif ext == file:
            return(1,file)
        elif ext == "":
            return(2,name)
        else:
            return(3, ext, name)
    return sorted(files, key=key_func)

print("Example:")
print(sort_by_ext([".cad", ".bat", ".aa", ".bat"]))
print(sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]))
print(sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]))
