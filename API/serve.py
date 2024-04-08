
from flask import Flask, request
import flask
import utils 
import json

# Khởi tạo model.
global model 
model = None
# Khởi tạo flask app
app = Flask(__name__)

# Khai báo các route 1 cho API
@app.route("/", methods=["GET"])
# Khai báo hàm xử lý dữ liệu.
def _hello_world():
	return "Welcome to AQS"

@app.route("/", methods=["POST"])
def _answer_question():
	data = {"success": False}
	if request.form.get("question"):
		# Lấy câu hỏi từ người dùng gửi lên
		ques = request.form.get("question")
		prediction_input = utils._check_input(ques)
		output = model.predict(prediction_input)
		output = output.argmax()
		data['answer'] = utils._answer(output)
		data['success'] = True
		utils._record(ques,data['answer'])
	return json.dumps(data,ensure_ascii=False)

if __name__ == "__main__":
	print("App run!")
	# Load model
	model = utils._load_model()
	app.run(debug=False, host="127.0.0.1", threaded=False)