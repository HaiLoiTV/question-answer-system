Để chạy bài dự án CNTT - Hệ thống Chatbot trả lời câu hỏi về trường học (TDTU)
-Mở thư mục API bằng các công cụ như Visual Studio Code,...
-Cài đặt các gói thư viện cần thiết: Mở cmd tại thư mục chứa file code và gõ lệnh: pip install -r requirements.txt
-Đồng thời cài đặt ngrok (https://ngrok.com/download) để tạo 1 kết nối mà từ bên ngoài có thể gọi API đến (yêu cầu đăng nhập trang ngrok.com để lấy authtoken).
-Sau khi cài đặt xong, chạy file ngrok.exe và gõ lệnh: 
1. ngrok authtoken <mã>
2. ngrok http 5000
-Copy đường link ở dòng Forward 
-Chạy python serve.py tại thư mục chứa file.
-Tiếp tục mở file demo.ipynb bằng Google Colab (cài đặt thư viện gradio - !pip install gradio)
-Dán đường link đã lưu ở trên vào biến url và chạy code
-Giao diện chat sẽ hiển thị ra kèm đường link. 