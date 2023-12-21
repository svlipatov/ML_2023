from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

# Функция подгрузки данных модели
def load_model():
   model_pipeline = pipeline(task='question-answering', model='deepset/roberta-base-squad2')
   return model_pipeline

# Класс для получения значения запрашиваемых параметров через API
class ApiParams(BaseModel):
   search_topic: str
   question: str

# Подгрузка модели
model = load_model()

# Объект для работы с api
app = FastAPI()

# Отправка результата запроса
@app.post("/answer/")
def answer(params: ApiParams):

   # Ответ на вопрос
   result = model(params.question, params.search_topic)
   return result
   #return result['answer']
