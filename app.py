import cohere
import streamlit as st

#open ai 와 함께 작업함.
st.title("Dokdox free ai service")


st.write("Thank you for using free ai service!")


co = cohere.ClientV2("Jd7EmJVUo3X1GDVsyW3TOjZxmKAwdquS9R3bQRI1")


user_input = st.text_input("welcom to dokdox ai service!just type under this message!")


if user_input:
    
    response = co.chat(
        model="command-r-plus-08-2024",
        messages=[{'role': 'user', 'content': user_input}]
    )

    st.write(response.message.content[0].text)















