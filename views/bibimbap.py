import streamlit as st

st.title("비빔밥 전문점에 오신 것을 환영합니다.")
st.divider()

st.subheader("- 메뉴 -")
st.subheader("불고기 비빔밥: 12,000원")
st.subheader("야채 비빔밥: 8,000원")
st.subheader("전주 비빔밥: 10,000원")
st.write("")
st.subheader("세트 주문시: 3,000원 추가")
st.subheader("(세트는 밥과 반찬이 추가됩니다.)")
st.write("")

# radio
order = st.radio(
    '비빔밥의 종류를 선택하세요.',
    ["불고기", "야채", "전주"],
    captions = ['불고기 비빔밥', '야채 비빔밥', '전주 비빔밥']
)

# checkbox
combo = st.checkbox('세트로 주문하시겠습니까? 3,000원 추가.')

price = 0

if order == '불고기' :
    price = 12_000
elif order == '야채' :
    price = 8_000
else :    # 전주
    price = 10_000

if combo == True :
    price += 3_000    # price = price + 3000

st.header(f"총 금액은 {price:,}원 입니다.")
