import cohere
import streamlit as st
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("COHERE_API_KEY")

# API 키가 없으면 에러 처리


    # API 클라이언트 초기화
co = cohere.ClientV2(api_key)

    # 제목과 설명
st.title("Dokdox Free AI Service")
st.write("Dokdox is the world's most wonderful web service.")
st.write("Thank you for using the free AI service!")

    # 사용자 입력 받기
user_input = st.text_input("Welcome to Dokdox AI Service! Just type below:")




if user_input:
    
    response = co.chat(
        model="command-r7b-12-2024",
        messages=[{'role': 'user', 'content': user_input}]
    )

    st.write(response.message.content[0].text)
    st.write("This ai response was generated using Cohere's language model./uncommercial use")
   



