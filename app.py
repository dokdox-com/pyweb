import cohere
import streamlit as st

# Streamlit secrets에서 API 키 가져오기
api_key = st.secrets["COHERE_API_KEY"]


#경고
st.warning("dokdox 에서 만든 이 페이지는 개발중인 기능으로 아직 완성되지 않았습니다.오류가 발생할수도 있습니다.")
# API 클라이언트 초기화
co = cohere.ClientV2(api_key)

#예시
st.metric(label="Temperature", value="20°C", delta="약 20 도 증가됨")
#링크
st.markdown("[더 나은 dokdox 의 정보를 확인할려면 dokdox.com 에 방문해보세요.](https://dokdox.com)")
st.link_button("dokdox 의 날씨서비스로 이동할려면 이곳을 클릭!", "https://dokdox.com")

st.title("DOKDOX/AI")
st.write("Dokdox is the world's most wonderful web service.")
st.write("Thank you for using the free AI service!")

# 사이드바에 슬라이더 추가

# 응답 히스토리 초기화
num_sentences = st.sidebar.slider("토큰범위설정-0으로 할 경우 오류가 발생할수도 있습니다.", min_value=0, max_value=1000, value=5)