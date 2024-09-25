import streamlit as st
import matplotlib.pyplot as plt    # 데이터 시각화 준비

st.header("기본 그래프 그리기: plt.plot()")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
plt.plot([10,20,30,40])
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("리스트가 두 개일 때")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt
        
plt.plot([3,4,5,6], [10,20,30,40])
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("변수 설정하여 그래프 그리기")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt
        
x = [1,2,3,4]
y = [10,20,30,40]
plt.plot(x, y)
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.code("""
import streamlit as st
import matplotlib.pyplot as plt
        
plt.plot([3,6,9,12], [60,40,70,100])
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.header("그래프 응용하기")

st.subheader("그래프 제목 추가")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
plt.rc('font', family='Malgun Gothic')
plt.plot([3,6,9,12], [60,40,70,100])
plt.title('새싹이의 수학 점수')
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("선 여러 개 그리기")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
x = ['3월', '6월', '9월', '12월']
y1 = [60, 40, 70, 100]
y2 = [100, 90, 95, 100]
plt.plot(x, y1)
plt.plot(x, y2)
plt.title('새싹이와 나의 수학 점수')
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("범례 추가")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
x = ['3월', '6월', '9월', '12월']
y1 = [60, 40, 70, 100]
y2 = [100, 90, 95, 100]
plt.plot(x, y1, label = '새싹')
plt.plot(x, y2, label = '나')
plt.legend()
plt.title('새싹이와 나의 수학 점수')
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("x축, y축 이름 추가")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
x = ['3월', '6월', '9월', '12월']
y1 = [60, 40, 70, 100]
y2 = [100, 90, 95, 100]
plt.plot(x, y1, label = '새싹')
plt.plot(x, y2, label = '나')
plt.xlabel('월')
plt.ylabel('점수')
plt.legend()
plt.title('새싹이와 나의 수학 점수')
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.header("그래프 속성 설정하기")

st.subheader("색상")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
x = ['3월', '6월', '9월', '12월']
y1 = [60, 40, 70, 100]
y2 = [100, 90, 95, 100]
plt.plot(x, y1, label = '새싹', color ='y')
plt.plot(x, y2, label = '나', color = 'red')
plt.legend()
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("선 모양 설정")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
x = ['3월', '6월', '9월', '12월']
y1 = [60, 40, 70, 100]
y2 = [100, 90, 95, 100]
plt.plot(x, y1, label = '새싹', color ='y', linestyle = ':')
plt.plot(x, y2, label = '나', color = 'red',ls = '-.')
plt.legend()
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("마커 설정")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
x = ['3월', '6월', '9월', '12월']
y1 = [60, 40, 70, 100]
y2 = [100, 90, 95, 100]
plt.plot(x, y1, 'o')
plt.plot(x, y2, '^')
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.header("막대 그래프: plt.bar()")

st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
x = ['youtube', 'instagram', 'game', 'internet']
y = [9, 7, 5, 2]
plt.bar(x,y)
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("x축 데이터가 숫자일 때")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
x = [1, 3, 4, 8]
y = [9, 7, 5, 2]
plt.bar(x,y)
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
x = [1, 3, 2, 8]
y = [9, 7, 5, 2]
plt.bar(x,y)
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
plt.bar(['2013','2023'], [3,13])
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("막대 두께 설정")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
x = ['youtube', 'instagram', 'game', 'internet']
y = [9, 7, 5, 2]
plt.bar(x,y, width=0.3)
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("막대 색상 설정")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
x = ['youtube', 'instagram', 'game', 'internet']
y = [9, 7, 5, 2]
plt.bar(x,y, color='orange')
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("막대 색상 여러 개로 설정")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
x = ['youtube', 'instagram', 'game', 'internet']
y = [9, 7, 5, 2]
color = ['red', 'orange', 'blue', 'green']
plt.bar(x,y, color=color)
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.header("원 그래프: plt.pie()")

st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
app = [9, 7, 5, 2]
plt.pie(app)
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("레이블 추가")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
app = [9, 7, 5, 2]
label = ['youtube', 'instagram', 'game', 'internet']
plt.pie(app, labels = label)
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.subheader("비율 표시")
st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
app = [9, 7, 5, 2]
label = ['youtube', 'instagram', 'game', 'internet']
plt.pie(app, labels = label, autopct='%.3f%%')
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.header("상자 그림: plt.boxplot()")

st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
math = [55,75,75,80,80,80,85,90,95,100]

plt.boxplot(math)
plt.grid()
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

st.divider()

st.header("상자 그림: plt.boxplot()")

st.code("""
import streamlit as st
import matplotlib.pyplot as plt    # 맷플롯립 라이브러리 불러오기
        
몸무게 = [40,  50,  60,  70]
키     = [152, 160, 167, 185]

plt.scatter(몸무게, 키)
st.pyplot(plt.gcf())    # 스트림릿에서는 plt.show() 대신 사용함
        """, language="python")

