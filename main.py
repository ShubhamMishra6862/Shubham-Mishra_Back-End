from fastapi import FastAPI
import datetime as dt
from typing import Optional

from model import TradeData
from database import(
    fetch_Lists,
    fetchTrade,
    create_Trade
)

app=FastAPI()


@app.get('/trades')
async def List_Trades(search: Optional[str]=None,assetClass: Optional[str]=None,start:Optional[dt.datetime]=None,end:Optional[dt.datetime]=None,minPrice:Optional[int]=None,maxPrice:Optional[int]=None,tradeType:Optional[str]=None,sort:Optional[str]=None,sortIn:Optional[int]=None):
    response=await fetch_Lists(search,assetClass,start,end,minPrice,maxPrice,tradeType,sort,sortIn)
    return response

# 
@app.get('/trades/{trade_id}',response_model=TradeData)
async def Get_Trade_By_Id(trade_id):
    response=await fetchTrade(trade_id)
    if response:
        return response
    raise HTTPException(404,"Trade Id not available")

@app.post('/trade/create/',response_model=TradeData)
async def Create_Table(tradeData:TradeData):
    response=await create_Trade(tradeData.dict())
    if response:
        return response
    raise HTTPException(400,"Bad Request")
