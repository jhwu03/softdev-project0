#Connor Oh
#SoftDev
#search :: Searching
#Oct 2019
from utl import readDB
def searchBlogs(search):
    allBlogs = readDB.getAllBlogs()
    results = []
    for blog in allBlogs:
        if search in str(blog[0]):
            results.append(blog)
        elif search in str(blog[1]):
            results.append(blog)
        elif search in str(blog[2]):
            results.append(blog)
        elif search in str(blog[3]):
            results.append(blog)
    return results

#print(search("Jacob's"))
