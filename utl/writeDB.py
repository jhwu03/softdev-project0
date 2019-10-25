db = sqlite3.connect(constants.DB_FILE)
c = db.cursor()


def insertIntoSQL(tableName:str, columnVals:list) -> str:
    """ This is an easier way to add things into sql table """
    tableHeaders = ''
    for i in columnVals[:-1]:
        if isinstance(i, str):
            cmd += '"{}", '.format(i)
        else:
            cmd += '{}, '.format(i)
    if isinstance(columnVals[-1], str):
         cmd += '"{}"'.format(i)
    else:
        cmd += '{}'.format(i)
    return 'INSERT INTO {} VALUES ({});'.format(tablename, cmd)


def addBlog(userID:int, blogTitle:str):
    """ This will allow the user to add a blog.
    It adds to the blogs db """
