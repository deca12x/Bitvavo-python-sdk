from python_bitvavo_api.bitvavo import Bitvavo
import json
import time
import os

# Use this class to connect to Bitvavo and make your first calls.
# Add trading strategies to implement your business logic.
class BitvavoImplementation:
    api_key = os.getenv("BITVAVO_API_KEY")
    api_secret = os.getenv("BITVAVO_API_SECRET")
    bitvavo_engine = None
    bitvavo_socket = None

    # Connect securely to Bitvavo, create the WebSocket and error callbacks.
    def __init__(self):
        self.bitvavo_engine = Bitvavo({
            'APIKEY': self.api_key,
            'APISECRET': self.api_secret
        })
        self.bitvavo_socket = self.bitvavo_engine.newWebsocket()
        self.bitvavo_socket.setErrorCallback(self.error_callback)

    # Handle errors.
    def error_callback(self, error):
        print("Add your error message.")
        #print("Errors:", json.dumps(error, indent=2))

    # Retrieve the data you need from Bitvavo in order to implement your
    # trading logic. Use multiple workflows to return data to your
    # callbacks.
    def a_trading_strategy(self):
        self.bitvavo_socket.ticker24h({}, self.a_trading_strategy_callback)

    # In your app you analyse data returned by the trading strategy, then make
    # calls to Bitvavo to respond to market conditions.
    def a_trading_strategy_callback(self, response):
        # Iterate through the markets
        for market in response:

            match market["market"]:
               case "ZRX-EUR":
                    print("Eureka, the latest bid for ZRX-EUR is: ", market["bid"] )
                    # Implement calculations for your trading logic.
                    # If they are positive, place an order: For example:
                    # self.bitvavo_socket.placeOrder("ZRX-EUR",
                    #                               'buy',
                    #                               'limit',
                    #                               { 'amount': '1', 'price': '00001' },
                    #                               self.order_placed_callback)
               case "a different market":
                    print("do something else")
               case _:
                    print("Not this one: ", market["market"])



    def order_placed_callback(self, response):
        # The order return parameters explain the quote and the fees for this trade.
        print("Order placed:", json.dumps(response, indent=2))
        # Add your business logic.


    # Sockets are fast, but asynchronous. Keep the socket open while you are
    # trading.
    def wait_and_close(self):
        # Bitvavo uses a weight based rate limiting system. Your app is limited to 1000 weight points per IP or
        # API key per minute. The rate weighting for each endpoint is supplied in Bitvavo API documentation.
        # This call returns the amount of points left. If you make more requests than permitted by the weight limit,
        # your IP or API key is banned.
        limit = self.bitvavo_engine.getRemainingLimit()
        try:
            while (limit > 0):
                time.sleep(0.5)
                limit = self.bitvavo_engine.getRemainingLimit()
        except KeyboardInterrupt:
            self.bitvavo_socket.closeSocket()


# Shall I re-explain main? Naaaaaaaaaa.
if __name__ == '__main__':
    bvavo = BitvavoImplementation()
    bvavo.a_trading_strategy()
    bvavo.wait_and_close()
