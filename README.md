# U-streamlit_JCharisTech
Youtube : Streamlit Python Tutorials:<br>
https://www.youtube.com/playlist?list=PLJ39kWiJXSixyRMcn3lrbv8xI8ZZoYNZU

Github : <br>
https://github.com/Jcharis/Streamlit_DataScience_Apps

## Crash_Course.py <br>
* warning, error, exception
```
st.warning("This is a warning ")

st.error("This shows an error ")

st.exception("NameError('name not defined')")
```
* 画像
```
from PIL import Image 
img = Image.open("example.jpeg")
st.image(img,width=300,caption='Streamlit Images')
```
* チェックボックス
```
if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")
```
* ラジオボタン
```
# Radio Button
status = st.radio("What is your status",('Active','Inactive'))
if status == 'Active':
	st.text("Status is Active")
else:
	st.warning("Not Active Yet")
```
* セレクトボックス(1つ)
* マルチセレクトボックス(たくさん)
```
# SelectBox
occupation = st.selectbox("Your Occupation",['Data Scientist','Programmer','Doctor','Businessman'])
st.write("You selected this option",occupation)

# MultiSelect
location = st.multiselect("Where do you stay",("London","New York","Accra","Kiev","Berlin","New Delhi"))
st.write("You selected",len(location),"location")
```
* スライダー
```
# Slider
salary = st.slider("What is your salary",1000,10000)
```
* ボタン
```
if st.button("******"):
	# 処理
```
* テキストインプット(1行) + ボタン
* テキストエリア (たくさん)+ ボタン
```
# Text Input
name = st.text_input("Enter Name","Type Here...")

# Text Area
c_text = st.text_area("Enter Text","Type Here...")
if st.button('Analyze'):
    c_result = c_text.title()
    st.success(c_result)
else:
    st.write("Press the above button..")
```
* date_input
* time_input
* スライドバー [st.sidebar.*****]
* Display JSON [st.json]
* Display Code [st.code]
* import 文形もcode文として出力 [st.echo]
```
with st.echo():
	# This will also be shown
	import pandas as pd 

	df = pd.DataFrame()
```
* ページ名・ページアイコンの変更
```
st.set_page_config(page_title = '******', page_icon=':Smiley:')
# 画像のpathも指定することが可能
```
* 拡張 (隠せるので, 一画面に多くの機能を配置できる)
```
st.expander('Movies DF',expanded=False):
	#False → 最初は非表示
	st.dataframe(df.head(10))
```
* バッククォート [SHIFT + @]

## face_detection_app <br>
* ファイルのアップロード
```
image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])

if image_file is not None:
	our_image = Image.open(image_file)
	st.text("Original Image")
	st.image(our_image)
```

## CSS_generator_app.py
* カラーの選択 [st.color_picker("Pick a Font Color","#fff")]

## japanese_spacy_streamlit_sample.py
* spacyを使った色々[spacy_streamlit.*(visualize)]

Github/Document : https://github.com/explosion/spacy-streamlit<br>

Youtube : A Simple NLP App with Spacy Streamlit Python<br>
https://www.youtube.com/watch?v=zBSze1elKRQ&list=PLJ39kWiJXSixyRMcn3lrbv8xI8ZZoYNZU&index=28

Blog : Simple NLP app with Spacy-Streamlit<br>
https://blog.jcharistech.com/2020/07/09/simple-nlp-app-with-spacy-streamlit/ <br>

Blog : spaCy からたどる最近の日本語自然言語処理ライブラリの調査 <br>
https://hakasenote.hnishi.com/2020/20200810-spacy-japanese-nlp/

## HTML_EDA_app.py
Youtube : How to use Pandas Profiling & Sweetviz in Streamlit with Streamlit Components Python(EDA App) <br>
https://www.w3schools.com/howto/howto_js_slideshow.asp

* CSS, JavaScriptがStreamlit内で使える
```
import streamlit.components.v1 as components
footer_temp = """ CSS, JavaScript """
components.html(footer_temp,height=500)
```
* W3Schools : CSS, JavaScriptの例がコピペでとってこれる <br>
https://www.w3schools.com/howto/howto_js_slideshow.asp <br>
Style以下をコピペ 

## read_documents_app.py
* Documentsを読み込みまとめ

## fake_data_generate_app.py
