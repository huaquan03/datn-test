from vnstock import Vnstock

stock = Vnstock().stock(symbol='ACB', source='VCI')
stock.listing.all_symbols()