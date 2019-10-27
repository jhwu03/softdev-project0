#Connor Oh
#SoftDev
#search :: Searching
#Oct 2019
import readDB
def search(search):
    allBlogs = readDB.getAllBlogs()
    results = []
    for blog in allBlogs:
        if search in str(blog[0]):
            results.append(blog)
        else if search in str(blog[1]):
            results.append(blog)
        else if
