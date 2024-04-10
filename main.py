import flask as fk
import stock as sk
import ML_Predictions as ml

app = fk.Flask(__name__)

@app.route("/")
def index():
    return fk.render_template("index.html")

@app.route("/stock")
def stock():
    return fk.render_template("stock_details.html")

@app.route('/stock_details', methods=['GET'])
def get_stock_details():
    stock_symbol = fk.request.args.get('symbol')
    days_to_predict = int(fk.request.args.get('days', 2))  # Default to 2 days if days param not provided
    if not stock_symbol:
        return fk.jsonify({'error': 'Stock symbol is required'}), 400
    # No need to validate days_to_predict if it's restricted on the client side
    stock = sk.Stock(stock_symbol)
    historical_data = stock.historyCall()
    predict_model = ml.predict(historical_data)
    predicted_prices = predict_model.predictClosing(days_to_predict)
    # Reshaping the predicted prices into 2D format
    predicted_prices = predicted_prices.tolist()
    stock_count = stock.stockCount()
    current_price = stock.currentPrice()
    market_cap = stock.marketCap()
    return fk.jsonify({
        'symbol': stock_symbol,
        'predicted_prices': predicted_prices,
        'days_predicted': days_to_predict,
        'stock_count': stock_count,
        'current_price' : current_price,
        'market_cap' : market_cap
    })



if __name__ == '__main__':
    app.run(debug=True)
