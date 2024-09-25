import streamlit as st
import matplotlib.pyplot as plt    # 데이터 시각화 준비
import csv

st.header("피자 vs 치킨, 사람들의 선택은?")

st.divider()

st.code("""
import streamlit as st
import matplotlib.pyplot as plt
import csv

f = open('food.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)

pz = []
ck = []
date = []

for row in data:
    row[1:] = map(int, row[1:])
    date.append(row[0])
    pz.append(row[1])
    ck.append(row[2])

plt.figure(figsize=(10,5))
plt.rc('font', family='Malgun Gothic')
plt.plot(date, pz, 'red', label = '피자')
plt.plot(date, ck, 'blue', label = '치킨')
plt.xticks(rotation=90)
plt.title('피자와 치킨의 검색지수')
plt.legend()
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()


f = open('assets/food.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)

pz = []
ck = []
date = []

for row in data:
    row[1:] = map(int, row[1:])
    date.append(row[0])
    pz.append(row[1])
    ck.append(row[2])

plt.figure(figsize=(10,5))
plt.rc('font', family='Malgun Gothic')
plt.plot(date, pz, 'red', label = '피자')
plt.plot(date, ck, 'blue', label = '치킨')
plt.xticks(rotation=90)
plt.title('피자와 치킨의 검색지수')
plt.legend()
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
