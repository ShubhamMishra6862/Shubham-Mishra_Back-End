# Backend_Assginment_Steeleye
This repository is of Backend Assignment that was provided by steeleye for One year internship

Name: Shubham Mishra
Registration No.: 12018763
BTech CSE

First run "uvicorn main:app --reload"<br/>
Then open the server in swaggerUI. easy testing use swaggerUI of fast api by "http://127.0.0.1:8000/docs"<br/>

**API PARAMETERS**<br/>
This is about input you can give to different parmeters to every api<br/>

1. **/trades** (List Trades)
   ![image](https://user-images.githubusercontent.com/101014691/233819420-942b1463-d40a-4847-bcfb-18225ebe5ad8.png)
  
   1.2. To get all trades click execute leaving all parameters blank<br/>
   1.1. **search**: It will search for value in "countreparty","instrumentId","instrumentName" and "trader".<br/>
        Input example: Walmart, BSA<br/><br/> 
        Below are the Filtering options<br/>
   1.3. **assetClass**: filtering according to assets.<br/>
        Input example: BOND, FX, EQUITY<br/>
   1.4. **start and end**: date will be accepted in datetime format.<br/>
        Input example: 2023-04-22T16:30:47.27, 2023-04-22T19:35:15.1670<br/>
   1.5. **minPrice and maxPrice**:Filter according to price <= and >= respectively. Will except integer.<br/>
   1.6. **tradeType**: will take "BUY" and "SELL".<br/>
   1.7. **sort**: according to which object member you want to sort the list of Trades.<br/>
        For price: type "trade_details.price"<br/>
        For quantity: type "trade_details.quantity"<br/>
        For tradetype: type "tradeDetails.buySellIndicator"<br/>
        For other members you can simply use its value like assetClass, instrument_id.<br/>
   1.8. **sortIn**: to sort list of trades in ascending or descanding order. Accept value in integer value 1 and -1.<br/>
        Use "1" to sort in ascending order<br/>
        Use "-1" to sort in descending order<br/>

2.**/trades/{trade_id}** (Get Trade By Id)<br/>

3. **/trade/create/** : create new trade data<br/>


**About Project**<br/>
I have used FastAPI, pydantic, MongoDB database and motor as a mongodb driver.<br/>
"main.py" : it contains all API which connects with databases for different operations.<br/>
"database.py" : it has all the function required to interact with database in MongoDB.<br/>
"model.py": defines how our collections will look like.<br/>
1. Following API I have implemented:
   1.1. /trades: which give list of trades. Accepts 9 optional parameters<br/>
   1.2. /trades/{trade_id}: to get a trade by id<br/>
   1.3. /trades/create/: to create a trade<br/>
   these all api interacts with MongoDB functions which has been implemented in database.py and give response with desired output<br/>
2. I used Pydantic model and MongoDB as a database for storing data because what I found that the given trade model was like a **JSON Object** which makes a plus point.<br/>
   The mongodb is a NoSQL database means, it doesn't stores data in tables rather as a collection of complex data (as a JSON object) which makes it quiet friendly for a developer who is not familiar with databases.<br/>
   Below I will explain the different function I used to interact with MongoDB database<br/>
   2.1. For search and match I have used "aggregate" of MongoDB which is a more efficient version of find so that I can apply multiple filtering as well as search opertaion.<br/>
        Aggregation in MongoDB is a step by step filtering ,grouping of collections. It accepts each step whether mulitple match or group in the form of array and perform those steps sequentially.<br/>
        example: db.collections.aggregate([{expression1},{expression2},{expression3}])<br/><br/>
        ![image](https://user-images.githubusercontent.com/101014691/233820635-4621e23c-312d-4879-8e99-adba7258d49b.png)<br/>
        I have declared an array "Matchquery" which will have search and filter parameters that are provided by api "/trades" and parameters with None will not be performed.<br/>
        If you observe in image above image there many if else condition. This is beacause there are multiple parameters in "/trades", now what if some parameters are given and others are "None".<br/>
        so we will not put those parameters with "None" in our aggregation array to prevent from wrong retrieval of collections. <br/>
        The db.collection.aggregate(Matchquery) return a cursor of desired collections, this means we need to traverse these coolections. Thus, I have used an array tradeL in which I append those collection. <br/>
   2.2 The "fetchTrade" uses "find_one" function to retrieve collection which has the desired Trade Id.<br/>
   2.3 the "createTrade" to insert one collection to the database.<br/>

       
