# Core Pkgs
import streamlit as st 

# NLP Pkgs
import spacy_streamlit
import spacy

import os
from PIL import Image

def load_model(choiced_model):
    nlp = spacy.load(choiced_model)
    return nlp


def main():
    """A Simple NLP app with Spacy-Streamlit"""

    st.title("Spacy-Streamlit NLP App")
    models = ['ja_core_news_md', 'ja_core_news_sm']
    
#     3つのモデルはサイズが異なっている
#     lg —> large
#     md —> medium
#     sm —> small
#     core —> モデルの能力として次のタスクを行えることを示す: general-purpose model with vocabulary, syntax, entities and word vectors
#     news —> ニュース記事のデータで学習されたことを示す

    choiced_model = st.sidebar.selectbox("Model",models)

    nlp = load_model(choiced_model)

    menu = ["MAIN", "Home","NER"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "MAIN":
        st.subheader("visualize")
        raw_text = st.text_area("Your Text","Enter Text Here")
        if st.button("Visualize"):
            docx = nlp(raw_text)
            spacy_streamlit.visualize(models, docx)
    
    if choice == "Home":
        st.subheader("Tokenization")
        raw_text = st.text_area("Your Text","Enter Text Here")
        docx = nlp(raw_text)
        if st.button("Tokenize"):
            spacy_streamlit.visualize_tokens(docx,attrs=['text','pos_','dep_','ent_type_'])

    elif choice == "NER":
        st.subheader("Named Entity Recognition")
        raw_text = st.text_area("Your Text","Enter Text Here")
        docx = nlp(raw_text)
        spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)


if __name__ == '__main__':
	main()