
import pandas as pd                        # Pandas 資料處理套件
import mplfinance as mpf                   # 繪製 K 線套件
          
# 讀取每日股價資料


names = ['Date', 'Adj_Close', 'Close', 'High', 'Low', 'Open', 'Volume']
df = pd.read_csv(r'stock2317.csv',       # 每日股價資料 CSV 檔
                 header=None, 
                 names=names,
                 skiprows=3,             # 跳過開頭三行檔頭標記
                 index_col=None, 
                 delimiter=',')
df['Date'] = pd.to_datetime(df['Date'])  # 字串轉為 datetime 資料型態
df.set_index('Date', inplace=True)       # 指定索引排序欄位為 Date
df_adj = df.iloc[:,1:5]                  # 'Close', 'High', 'Low', 'Open'

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# 設定繪圖顏色
mc = mpf.make_marketcolors(
	up='red',                     # 上漲 K 棒顏色
	down='green',                 # 下跌 K 棒顏色 
	edge='i',                     # K線線柱邊緣顏色(i代表繼承自up和down的顏色)
	wick='i',                     # 上下影線顏色
	volume='in',                  # 成交量長條圖的顏色
	inherit=True)                 # 是否繼承顏色設定

s = mpf.make_mpf_style(
	gridaxis='both',              # 格線位置
	gridstyle='-.',               # 格線線型
	y_on_right=False,             # y軸位置是否在右
    rc={'font.size':12, 
        'font.sans-serif':'SimHei',   # 指定中文字型
        'axes.titlesize':18,
        'axes.labelsize':16,
        'xtick.labelsize':12,
        'ytick.labelsize':12},
	marketcolors=mc)

mpf.plot(df_adj,
         type='candle',            # 指定 K 棒繪圖符號格式
         title='          鴻海2020年股價',
         ylabel='股價',
         figratio=(15, 10),        # 圖形大小
         figscale=1,
         xrotation=20,             # 日期顯示旋轉角度
         style=s,                  # 設定繪圖風格
         show_nontrading=False)    # 是否顯示無交易日
