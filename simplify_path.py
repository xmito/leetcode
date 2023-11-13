

# Simplify path (Medium)
# Given a string path, which is an absolute path (starting with a slash '/') to a file
# or directory in a Unix-style file system, convert it to the simplified canonical path.
# In a Unix-style file system, a period '.' refers to the current directory, a double
# period '..' refers to the directory up a level, and any multiple consecutive slashes
# (i.e. '//') are treated as a single slash '/'. For this problem, any other format of
# periods such as '...' are treated as file/directory names.
# The canonical path should have the following format:
# - The path starts with a single slash '/'.
# - Any two directories are separated by a single slash '/'.
# - The path does not end with a trailing '/'.
# - The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path.
# Constraints:
# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.

# Time complexity: O(n) - linear in number of path segments
# Space complexity: O(n) - linear in number of path segments
def simplifyPath(path: str) -> str:
    stack = []   
    for seg in path.split('/'):
        if seg == '.' or seg == '':
            continue
        elif seg == '..':
            try:
                # It's more efficient to catch exception than to explicitely
                # check that are any elements on top of the stack
                stack.pop()
            except IndexError:
                pass
            continue
        stack.append(seg)

    return '/' + '/'.join(stack)


if __name__ == "__main__":
    res = simplifyPath("/home/")
    print(res)
    assert res == "/home"

    res = simplifyPath("/../")
    print(res)
    assert res == "/"

    res = simplifyPath("/home//foo")
    print(res)
    assert res == "/home/foo"