import agent
import funclib.lib
import streamlit as st 

st.title('LPI - Language Programming Interface')
query = st.text_input("Query")

if query:
    messages = []

    messages.append({"role": "system", \
        "content": "Don't make assumptions about what values to plug into functions. \
        Infer certain arguments as appropriate."})

    messages.append({"role": "user", \
        "content": query})

    chat_response = agent.chat_completion_request(
        messages, functions=funclib.lib.funcs()
    )
    print(chat_response.json())
    assistant_message = chat_response.json()["choices"][0]["message"]
    st.write(assistant_message)
