import matplotlib.pyplot as plt
import seaborn as sns

# データの前処理
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 株価の推移
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Date', y='Price')
plt.title('Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# 移動平均線の追加
df['Moving Average'] = df['Price'].rolling(window=20).mean()

plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Date', y='Price', label='Price')
sns.lineplot(data=df, x='Date', y='Moving Average', label='Moving Average')
plt.title('Stock Price with Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
