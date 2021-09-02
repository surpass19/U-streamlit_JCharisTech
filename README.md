# U-streamlit_JCharisTech
SYoutube : treamlit Python Tutorials:<br>
https://www.youtube.com/playlist?list=PLJ39kWiJXSixyRMcn3lrbv8xI8ZZoYNZU

Github : <br>
https://github.com/Jcharis/Streamlit_DataScience_Apps

## Crash_Course.py <br>
* チェックボックス
* ラジオボタン
* セレクトボックス(1つ)
* マルチセレクトボックス(たくさん)
* スライダー
* ボタン
* テキストインプット(1行) + ボタン
* テキストエリア (たくさん)+ ボタン
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


