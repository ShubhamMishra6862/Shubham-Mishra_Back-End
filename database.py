from model import (TradeData,TradeDetails)
import motor.motor_asyncio
import datetime as dt
client=motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://shubhammishra6862:root@cluster0.w880tnj.mongodb.net/?retryWrites=true&w=majority')

database=client.steeleye #to create database
collection=database.tradesList  #create collection


async def fetchLists(search,assetClass,start,end,minPrice,maxPrice,tradeType,sort,sortIn):
    Matchquery=[]
    if(search!=None):
       Matchquery.append({"$match":{"$or":[
        {"counterparty":search},
        {"instrument_id":search},
        {"instrument_name":search},
        {"trader":search}]}})

    if(assetClass!=None):
        Matchquery.append({"$match":{"asset_class": assetClass}})

    if(start!=None):
        Matchquery.append({"$match":{"trade_date_time":{"$gte": start}}})
    if(end!=None):
        Matchquery.append({"$match":{"trade_date_time":{"$lte":end}}})
    if(minPrice!=None):
         Matchquery.append({"$match":{"trade_details.price":{"$gte": minPrice}}})
    if(maxPrice!=None):
         Matchquery.append({"$match":{"trade_details.price":{"$lte": maxPrice}}})
    if(tradeType!=None):
         Matchquery.append({"$match":{"trade_details.buySellIndicator":tradeType}})
    if(sort!=None):
         if(sortIn!=None):
            if(sortIn==1 or sortIn==-1):
                Matchquery.append({"$sort":{sort:sortIn}})
            else:
                return ("invalid sortIn value")
         else:
            Matchquery.append({"$sort":{sort:1}})

    tradeL=[];
    cursor=collection.aggregate(Matchquery)
    async for document in cursor:
        tradeL.append(TradeData(**document))

    print (Matchquery) 
    return tradeL


async def fetchTrade(id):
    document=await collection.find_one({"trade_id":id})
    return document


async def createTrade(TradeObject):
    document=TradeObject
    response=await collection.insert_one(document)
    return document
