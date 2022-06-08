import asyncio
from binance import Client
import time 
from binance.enums import *
from binance.helpers import round_step_size


symbol = 'BTCUSDT'

api_key = 'zyN3R5T1FOPwKLBvxnf09X6EkKzcIEBCes1RpNqD6moXU7YoqOBX3M2vFcUgCAQy'
api_secret = 'dQMgSnNJs3MrBvU5qx65WYmn7PIAK9o0LLjLLVmPicjjCsWTA3iFA6H9UwDKn55h'


FreeUSDT = 100.0

TargetPrice_BTCUSDT = 28000.0000000000

quantity = (FreeUSDT/TargetPrice_BTCUSDT)/10

def main():
    client = Client(api_key, api_secret) # Connect to server.
    while(1):
        userinputs = input("請輸入指令")
        print("-------------------------------------------------------------------")
                
        
            
        
    getbal(client)

    info = client.get_symbol_info(symbol)
    print(info['filters'][2]['maxQty'])
    print("-------------------------------------------------------------------")
    orders = client.get_all_orders(symbol=symbol)
    print("-------------------------------------------------------------------")
    fees = client.get_trade_fee(symbol=symbol)
    print("-------------------------------------------------------------------")
    print("交易手續費")
    print(fees[0]['makerCommission']+" %")
    
    

    # tick_size = 0.000001
    # rounded_amount = round_step_size(quanity, tick_size) #訂單大小 
    # print(rounded_amount)
    #limit_buy(client) #限價單 
    print("-------------------------------------------------------------------")
    openorders = client.get_open_orders(symbol=symbol) # 查詢所有未成交訂單
    print(openorders)
    result = client.cancel_order(
    symbol=symbol,
    orderId='10754189012')
    print(result)
    print("-------------------------------------------------------------------")
    openorders = client.get_open_orders(symbol=symbol) # 查詢所有未成交訂單
    print(openorders)
    



    
    


    
def getbal(client): #得到所有剩餘的Crypto
    info = client.get_account()
    bal = info['balances'] ## Res_ALL_crypto.
    for i in bal:

        if float(i['free']) > 0:
            print(i)
    print("-------------------------------------------------------------------")
    


def buy(client):

    return 0
    
def limit_buy(client):
    order = client.create_order(
    symbol=symbol,
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=0.001,
    price='28400.1')
def limit_sell(client, price, quantity):
    order = client.order_limit_sell(
    symbol = symbol,
    quantity = quantity,
    price= price)
def OCO_sell(client, price, stopPrice, quantity, stopLimitPrice):
    order= client.order_oco_sell(
    symbol= symbol,                                            
    quantity = quantity,                                            
    price = price,                                            
    stopPrice= stopPrice,                                            
    stopLimitPrice= stopLimitPrice,                                            
    stopLimitTimeInForce= 'FOK')
def margin_buy(client):
    order = client.create_margin_order(
    symbol= symbol,
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='0.00001')

    
    



if __name__ == "__main__":
    main()