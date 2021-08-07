import yfinance as yf
import openpyxl 

ticker = input('請輸入股票代號： ')
time_start = input('請輸入「開始」時間(yyyy-mm-dd): ')
time_end = input('請輸入「結束」時間(yyyy-mm-dd)(!!注意!!：不包含結束時間喔): ')
filename = ticker + '.csv'

data = []
# 讀取舊檔
with open('pf.csv', 'r') as f:
	for line in f:
		if 'Date, Clsed' in line:
			continue
		data.append(line.strip().split(','))
	print('existed data: ', data)

# Download stock data then export as CSV
data_df = yf.download(ticker, start=time_start, end=time_end)
data_df.to_csv(ticker + '.csv')

data_update = []
with open(filename, 'r') as f:
	for line in f:
		if 'Date,Open,High,Low,Close,Adj Close,Volume' in line:
			continue
		data_update.append(line.strip().split(','))
	print('updated data：', data_update)

# 寫入
with open('SPY_1.csv', 'w') as f:
		f.write('Date,Closed\n')
		for line in data_update:
			f.write(line[0] + ',' + line[4] + '\n')