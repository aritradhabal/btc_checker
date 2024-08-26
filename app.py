# # from flask import Flask, render_template, request, jsonify
# # import requests

# # app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/get_addresses', methods=['POST'])
# # def get_addresses():
# #     address = request.form['address']
# #     url = f'https://blockchain.info/rawaddr/{address}'
# #     response = requests.get(url)

# #     if response.status_code == 200:
# #         data = response.json()
# #         txs = data['txs']

# #         # Sort transactions by time in descending order (most recent first)
# #         txs.sort(key=lambda tx: tx['time'], reverse=True) 

# #         interacting_addresses = set()

# #         for tx in txs:
# #             for input in tx['inputs']:
# #                 if 'prev_out' in input and 'addr' in input['prev_out']:
# #                     interacting_addresses.add(input['prev_out']['addr'])
# #             for output in tx['out']:
# #                 if 'addr' in output:
# #                     interacting_addresses.add(output['addr'])

# #             # Stop if we have 10 unique addresses
# #             if len(interacting_addresses) >= 10:
# #                 break

# #         return jsonify(list(interacting_addresses)[:10]) 
# #     else:
# #         return jsonify({'error': 'Invalid Bitcoin address or API error'})

# # if __name__ == '__main__':
# #     app.run(debug=True)



# from flask import Flask, render_template, request, jsonify
# import requests

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/get_addresses', methods=['POST'])
# def get_addresses():
#     address = request.form['address']
#     url = f'https://blockchain.info/rawaddr/{address}'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         txs = data['txs']

#         # Sort transactions by time in descending order (most recent first)
#         txs.sort(key=lambda tx: tx['time'], reverse=True) 

#         interacting_addresses = set()
#         address_data = [] # To store address and balance data

#         for tx in txs:
#             for input in tx['inputs']:
#                 if 'prev_out' in input and 'addr' in input['prev_out']:
#                     interacting_addresses.add(input['prev_out']['addr'])
#             for output in tx['out']:
#                 if 'addr' in output:
#                     interacting_addresses.add(output['addr'])

#             if len(interacting_addresses) >= 10:
#                 break

#         # Fetch balance for each interacting address
#         for addr in interacting_addresses:
#             balance_url = f'https://blockchain.info/q/addressbalance/{addr}'
#             balance_response = requests.get(balance_url)
#             if balance_response.status_code == 200:
#                 balance = int(balance_response.text) / 100000000  # Convert satoshis to BTC
#                 address_data.append({'address': addr, 'balance': balance})

#         return jsonify(address_data[:10]) 
#     else:
#         return jsonify({'error': 'Invalid Bitcoin address or API error'})

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Hardcoded list of Bitcoin addresses for testing
hardcoded_addresses = [
    "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2",
    "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy",
    "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq",
    "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    "3EktnHQD7RiAE6uzMj2ZifT9YgRrkSgzQX",
    "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo",
    "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
    "1KTiXcHLNfrYPcquTocK7r2B81rAvXjW4u",
    "1dice8EMZmqKvrGE4Qc9bUFf9PX3xaYDp",
    "37XuVSEpWW4trkfmvWzegTHQt7BdktSKUs"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_addresses', methods=['POST'])
def get_addresses():
    # Ignore the actual address from the request and use hardcoded ones
    address_data = [{'address': addr, 'balance': random.uniform(0, 10)} for addr in hardcoded_addresses] 
    return jsonify(address_data)

if __name__ == '__main__':
    app.run(debug=True)