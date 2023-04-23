import datetime as dt
from typing import Optional
from pydantic import BaseModel

class TradeDetails(BaseModel):
    buySellIndicator: str 

    price: float

    quantity: int


class TradeData(BaseModel):
    asset_class: Optional[str]

    counterparty: Optional[str] 

    instrument_id: str

    instrument_name: str 

    trade_date_time: dt.datetime 

    trade_details: TradeDetails

    trade_id: str

    trader: str
