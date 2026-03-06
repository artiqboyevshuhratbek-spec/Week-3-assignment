import requests

url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json'
target = ['uzs','eur', 'gbp', 'jpy', 'rub', 'kzt', 'cny', 'cad', 'aud']

def fetch_exchange_rates(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return False
    except:
        return False

def get_total_value(item):
    return item['total']

def process_data(data, amount, threshold):
    rates = data['usd']
    processed_list = []
    for code in target:
        if code in rates:
            total_value = amount * rates[code]
            if total_value >= threshold:
                processed_list.append({'name': code.upper(),'total': total_value})
    return processed_list

def save_to_file(results, amount):
    with open("currency_report.txt", "w") as f:
        f.write(f"Report for ${amount}\n")
        for item in results:
            f.write(f"{item['name']}: {item['total']:.2f}\n")

print("--- USD Currency Analyst ---\n")
api_data = fetch_exchange_rates(url)

if api_data:
    try:
        user_money = float(input("Enter USD amount: $"))
        user_limit = float(input("Enter minimum threshold: "))
        
        final_results = process_data(api_data, user_money, user_limit)
        
        if not final_results:
            print("No matches found.")
        else:
            print("\nResults:")
            for item in final_results:
                print(f"{item['name']}: {item['total']:.2f}")
            if input("\nSave to file? (yes/no): ").lower() == 'yes':
                save_to_file(final_results, user_money)
                print("Saved!")
    except ValueError:
        print("Please enter numbers only.")
else:
    print("API Error.")