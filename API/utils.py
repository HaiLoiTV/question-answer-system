from keras.models import load_model
from underthesea import word_tokenize
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
import string
import hyper as hp
import csv
# Load model
def _load_model():
	# Khởi tạo model
    model = load_model("model_QA.keras")
    print("Load model complete!")
    return model
def _check_input(prediction_input):
    texts_p = []
    prediction_input = [letters.lower() for letters in prediction_input if letters not in string.punctuation]
    prediction_input = ''.join(prediction_input)
    word_tokenize(prediction_input, format='text')
    texts_p.append(prediction_input)
    prediction_input = hp.tokenizer.texts_to_sequences(texts_p)
    prediction_input = np.array(prediction_input).reshape(-1)
    prediction_input = pad_sequences([prediction_input],hp.input_shape)
    return prediction_input
def _answer(output):
    # Lấy ra câu trả lời dự đoán nhất
    response_tag = hp.le.inverse_transform([output])[0]
    return hp.responses[response_tag]

def _record(ques,ans):
    with open("data.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([ques,ans])
    return ""