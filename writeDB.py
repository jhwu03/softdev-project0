db = sqlite3.connect(constants.DB_FILE)
c = db.cursor()


def insertIntoSQL(tableName:str, columnVals:list) -> str:
    """ This is an easier way to add things into sql table """
    cmd = 'INSERT INTO ' + table_name + ' VALUES ('
    for i in columnVals[:-1]:
        if isinstance(i, str):
            cmd += "" #TODO: Fix this
        cmd += i + ', '
     command += columnVals[-1]
     return command + ');'


def addBlog(userID:int, blogTitle:str):
    """ This will allow the user to add a blog.
    It adds to the blogs db """
    cmd = 'INSERT INTO blogs VALUES
