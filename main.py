import streamlit as st
st.title('쌈@뽕')
name = st.text_input('이름 입력해! : ')
menu = st.selectbox('좋아하는 음식 선택해!', ['망고빙수', '김치볶음밥', '회오리감자'])
if st.button == ('인사말 생성') :
  st.write(f'안녕 {name}! 너는 {menu}를 좋아하는구나!!멋찌다')
