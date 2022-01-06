import streamlit as st
from transformers import *
# source & destination languages
src = "en"
dst = "vi"

task_name = f"translation_{src}_to_{dst}"
model_name = f"Helsinki-NLP/opus-mt-{src}-{dst}"

translator= pipeline(task_name, model=model_name, tokenizer=model_name)


# Title for the page and nice icon
st.set_page_config(page_title="NMT", page_icon="🤖")
# Header
st.title("Translate")
with st.form("my_form"):

    user_input = st.text_area("Source Text", max_chars=200)

    translation = translator(user_input)[0]["translation_text"]


    # Create a button
    submitted = st.form_submit_button("Translate")
    # If the button pressed, print the translation
    # Here, we use "st.info", but you can try "st.write", "st.code", or "st.success".
    if submitted:
        st.write("Translation")
        st.info(translation)