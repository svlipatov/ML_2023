from transformers import pipeline
import streamlit as st
# Функция подгрузки данных модели
@st.cache_resource
def load_model():
   model_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
   return model_pipeline
# Функция запуска модели
def execute(question1 , text1):
   result = model(question=question1, context=text1)
   st.text('Ответ на вопрос: ' + result['answer'])
# Заголовок
st.title(body= 'Приложение отвечающее на пользовательские вопросы по тексту')
# Текст для анализа
text = st.text_area(label='Введите текст',value=' ', height=300)
# Вопрос
question = st.text_input(label='Введите вопрос',value=' ')
# Активность кнопки
if text == ' ' or question == ' ':
   disabled = True
else:
   disabled = False
# Подгрузка модели
model = load_model()
# Кнопка для запуска модели
executed = st.button(label='Выполнить', disabled=disabled)
if executed:
   execute(question, text)
