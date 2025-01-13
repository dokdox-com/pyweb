import cohere
import streamlit as st

# Streamlit secrets에서 API 키 가져오기
api_key = st.secrets["COHERE_API_KEY"]

# API 클라이언트 초기화
co = cohere.ClientV2(api_key)

# 제목과 설명
st.title("Dokdox Free AI Service")
st.write("Dokdox is the world's most wonderful web service.")
st.write("Thank you for using the free AI service!")

# 사용자 입력 받기
user_input = st.text_input("대화할려면 밑에서 글자 임력...")
name = st.text_input("이름을 임력해주세요")

# 응답 히스토리 초기화
if "responses" not in st.session_state:
    st.session_state.responses = []

if user_input:
    # Cohere API 호출
    response = co.chat(
        model="command-r7b-12-2024",  # 모델명
        messages=[{'role': 'user', 'content': "응답:" + user_input + " 나의 이름은 " + name}]
    )

    # 응답 저장 및 출력
    st.session_state.responses.append(response.message.content[0].text)
    st.write(response.message.content[0].text)
    st.write("This AI response was generated using Cohere's language model. / Non-commercial use only.")

# 이전 응답 출력
st.write("Previous Responses:")
for resp in st.session_state.responses:
    st.write(resp)
