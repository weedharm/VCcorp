import streamlit as st
import sentencepiece as spm
import ctranslate2
from nltk import sent_tokenize


def translate(source, translator, sp_source_model, sp_target_model):
    """Use CTranslate model to translate a sentence

    Args:
        source (str): Source sentences to translate
        translator (object): Object of Translator, with the CTranslate2 model
        sp_source_model (object): Object of SentencePieceProcessor, with the SentencePiece source model
        sp_target_model (object): Object of SentencePieceProcessor, with the SentencePiece target model
    Returns:
        Translation of the source text
    """

    source_sentences = sent_tokenize(source)
    source_tokenized = sp_source_model.encode(source_sentences, out_type=str)
    translations = translator.translate_batch(source_tokenized)
    translations = [translation[0]["tokens"] for translation in translations]
    translations_detokenized = sp_target_model.decode(translations)
    translation = " ".join(translations_detokenized)

    return translation


# [Modify] File paths here to the CTranslate2 SentencePiece models.
ct_model_path = "model/"
sp_source_model_path = "source.spm"
sp_target_model_path = "target.spm"

# Create objects of CTranslate2 Translator and SentencePieceProcessor to load the models
translator = ctranslate2.Translator(ct_model_path, "cpu")    # or "cuda" for GPU
sp_source_model = spm.SentencePieceProcessor(sp_source_model_path)
sp_target_model = spm.SentencePieceProcessor(sp_target_model_path)


# Title for the page and nice icon
st.set_page_config(page_title="NMT", page_icon="🤖")
# Header
st.title("Translate")

# Form to add your items
with st.form("my_form"):
    # Textarea to type the source text.
    user_input = st.text_area("Source Text", max_chars=200)
    # Translate with CTranslate2 model
    translation = translate(user_input, translator, sp_source_model, sp_target_model)

    # Create a button
    submitted = st.form_submit_button("Translate")
    # If the button pressed, print the translation
    # Here, we use "st.info", but you can try "st.write", "st.code", or "st.success".
    if submitted:
        st.write("Translation")
        st.info(translation)