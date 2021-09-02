import spacy_streamlit

models = ["ja_core_news_md", "ja_core_news_sm"]
default_text = "もうすぐ梅雨。日本のオリンピックはどうなる？"
spacy_streamlit.visualize(models, default_text)