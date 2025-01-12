import cohere
import streamlit as st

# Streamlit secrets에서 API 키 가져오기
api_key = st.secrets["cohere"]["COHERE_API_KEY"]

# API 클라이언트 초기화
co = cohere.Client(api_key)

# 제목과 설명
st.title("Dokdox Free AI Service")
st.write("Dokdox is the world's most wonderful web service.")
st.write("Thank you for using the free AI service!")

# 사용자 입력 받기
user_input = st.text_input("Welcome to Dokdox AI Service! Just type below:한국어가능합니다!")

if user_input:
        # Cohere API 호출
        response = co.chat(
            model="command",  # 모델명
            messages=[{'role': 'user', 'content': user_input}]
        )

        # 응답 출력
        st.write(response['messages'][0]['content'])
        st.write("This AI response was generated using Cohere's language model. / Non-commercial use only.")

