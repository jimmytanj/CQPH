# -*- coding: utf-8 -*-

import requests
import json
import cx_Oracle
import isbnlib

def getOracleConnection():
    conn=cx_Oracle.connect("chuban/chuban@localhost/orcl")
    return conn



def getISBN(zibianma):
    isbntry=zibianma[:-4]
    if len(isbntry)==10 and isbnlib.is_isbn10(isbntry):
        return isbntry
    elif len(isbntry)==13 and isbnlib.is_isbn13(isbntry):
        return isbntry
    elif len(isbntry)==11 and isbnlib.is_isbn10(isbntry[:-1]):
        return isbntry[:-1]
    elif len(isbntry)==14 and isbnlib.is_isbn13(isbntry[:-1]):
        return isbntry[:-1]
    else :
        return None
    return None

def getCodeAndNameList(conn):
    resultList=[]
    cursor=conn.cursor()
    cursor.execute('select invcode,invname from bd_invbasdoc')
    allBooks=cursor.fetchall()
    for eachBook in allBooks:
        eachBookIsbn=getISBN(eachBook[0])
        if eachBookIsbn != None:
            resultList.append((eachBook[0],eachBook[1]))
    return resultList

def getBookInfoFromDouban(isbn):
    resultDict=dict()
    req=requests.get("https://api.douban.com/v2/book/isbn/:"+isbn)
    if req.status_code==requests.codes.ok:
        bookInfo=req.content.decode('utf-8')
        bookJson=json.loads(bookInfo)
        resultDict['author']=(',').join(bookJson['author'])
        resultDict['pubdate']=bookJson['pubdate']
        resultDict['tags']=','.join(bookJson['tags'])
        resultDict['origin_title']=bookJson['origin_title']
        resultDict['binding']=bookJson['binding']
        resultDict['translator']=','.join(bookJson['translator'])
        resultDict['catalog']=bookJson['catalog']
        resultDict['pages']=bookJson['pages']
        resultDict['publisher']=bookJson['publisher']
        resultDict['isbn10']=bookJson['isbn10']
        resultDict['isbn13']=bookJson['isbn13']
        resultDict['title']=bookJson['title']
        resultDict['author_intro']=bookJson['author_intro']
        resultDict['summary']=bookJson['summary']
        resultDict['price']=bookJson['price']
        return resultDict
    else :
        return None

if __name__=='__main__':
#    info=getBookInfoFromDouban('9787111128069')
    conn=getOracleConnection()
    codeNameList=getCodeAndNameList()
    for eachCodeName in codeNameList:
        doubanInfo=getBookInfoFromDouban(getISBN(eachCodeName[0]))
        if doubanInfo != None:
            print(doubanInfo)