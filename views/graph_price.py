import streamlit as st
import matplotlib.pyplot as plt    # 데이터 시각화 준비
import csv

st.header("부모님, 제 용돈을 올려야합니다. 그 이유는요!")

st.divider()

st.code("""
import streamlit as st
import matplotlib.pyplot as plt
import csv

f = open('assets/price.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)

food = input('<품목>'
             '\n빵/사탕/아이스크림/스낵과자/주스/탄산음료/떡볶이/치킨/햄버거/피자' 
             '\n어떤 간식의 가격 변화를 보고 싶은가요?')

price = []
for row in data:
    if food  == row[0]:
        for i in row[1:]:
            price.append(float(i))
            
years = []
for i in range(2003, 2024):
    years.append(i)
    
plt.rc('font', family='Malgun Gothic')
plt.plot(years, price, label = food)
plt.xlabel('연도')
plt.ylabel('물가지수')
plt.title(food + '의 물가 변화')
plt.legend()
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
""", language="python")

st.divider()


f = open('assets/price.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)


st.subheader('''
<품목>
빵/사탕/아이스크림/스낵과자/주스/탄산음료/떡볶이/치킨/햄버거/피자
어떤 간식의 가격 변화를 보고 싶은가요?
''')

food = st.selectbox(
    label='간식 이름 선택',
    options=['빵', '사탕', '아이스크림', '스낵과자', '주스', '탄산음료', '떡볶이', '치킨', '햄버거', '피자'],
    index=None,
    placeholder='간식 이름을 선택하세요'
)

if food :
    price = []
    for row in data:
        if food  == row[0]:
            for i in row[1:]:
                price.append(float(i))
                
    years = []
    for i in range(2003, 2024):
        years.append(i)
        
    plt.rc('font', family='Malgun Gothic')
    plt.plot(years, price, label = food)
    plt.xlabel('연도')
    plt.ylabel('물가지수')
    plt.title(food + '의 물가 변화')
    plt.legend()
    st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함

