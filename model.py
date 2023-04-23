import datetime as dt

from typing import Optional
from pydantic import BaseModel, Field

class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")

    price: float = Field(description="The price of the Trade.")

    quantity: int = Field(description="The amount of units traded.")


class TradeData(BaseModel):
    asset_class: Optional[str] = Field(description="The asset class of the instrument traded. E.g. BOND, EQUITY, FX...etc")

    counterparty: Optional[str] = Field(description="The counterparty the trade was executed with. May not always be available")

    instrument_id: str = Field(description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")

    instrument_name: str = Field(description="The name of the instrument traded.")

    trade_date_time: dt.datetime = Field(description="The date-time the Trade was executed. E.g. 2023-04-23T05:33:10.534000")

    trade_details: TradeDetails = Field(description="The details of the trade, i.e. price, quantity")

    trade_id: str = Field(description="The unique ID of the trade")

    trader: str = Field(description="The name of the Trader")
