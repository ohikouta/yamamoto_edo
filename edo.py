# -*- coding:utf-8 -*-

# 山本くんデータセットで練習！

import pandas as pd
import matplotlib.pyplot as plt

df_edo = pd.read_csv("C:\\Users\\81804\\working_directory\\yamamoto_edo\\edo_keizai.csv", encoding='utf-8')

# columnsの変更
df_edo.columns = df_edo.iloc[0]
print("="*180)
# df_edoはdf_edo.iloc[1:]に変更
df_edo = df_edo.iloc[1:]
print(df_edo.columns)
print(df_edo.iloc[0])
# df_edoの中で使わない列を削除
df_sample = df_edo[["西暦", "米相場"]]
print(df_sample.head())
print(df_sample.columns)
print(df_sample.shape)
print(type(df_sample.iat[0, 0]))

# df_sample["西暦"]をint型にキャスト
for i in range(df_sample.shape[0]):
    df_sample.iat[i, 0] = df_sample.iat[i, 0].replace("年", "")
    df_sample.iat[i, 0] = int(df_sample.iat[i, 0])
    
# 欠損値の処理
print(df_sample.head())
# 欠損値処理①:削除
print(f"全体のデータは{df_sample.shape[0]}個です.")
# df_sample = df_sample.dropna(how='any')
print(f"値を持つデータは{df_sample.shape[0]}個です.")

# 欠損値処理②:置換(穴埋め)
# 前の値で置換,後ろ30個は前の過去の直近の値で置換
# この補完が適切なのか問題
# 強引に補完したけど,全部補完しなくてもいいかも
df_sample = df_sample.fillna(method='bfill')
print(df_sample.head())
df_sample.iloc[-30:].fillna(method='ffill')
print(df_sample.iloc[-10:])

# 最後の欠損値処理:df_sample["米相場"]のデータ型がfloatでなければその行は削除する
df_sample = df_sample[df_sample["米相場"] != "なし"]

# 年数毎に平均を算出し,新しいデータフレームを作成する
import numpy as np
year_list = np.unique(df_sample["西暦"])

print(type(year_list))
print(df_sample["西暦"])

year_period = year_list[-1]-year_list[0]+1
year_with_data = len(year_list)
print(f"記録された期間は{year_period}年間,実際にデータがあるのは{year_with_data}年分,つまり{year_period-year_with_data}年分のデータが欠落している.")

# 各年のデータの平均値をその年の米相場として新たなデータフレームに格納する
new_data = []
for i in year_list:
    df_current_year = df_sample[df_sample["西暦"] == i]
    data_count = df_current_year.shape[0]
    df_current_year = df_current_year.astype({'米相場': float})
    total_price = df_current_year["米相場"].sum()
    average_price = total_price / data_count
    new_data.append(average_price)
    
    
# 各年の平均米相場が格納されたリスト
print(len(new_data))


