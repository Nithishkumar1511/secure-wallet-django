🔐 Secure Wallet

A minimalist and secure web application where users can upload JPG/PNG files, which are converted to binary and stored in a MySQL database. Built using Django and MySQL, with role-based access for New Users, Existing Users, and Admin.

🚀 Features

✅ Register as a new user and upload image  
✅ Login as existing user to view/upload images  
✅ Admin panel with access to all uploaded files  
✅ Converts uploaded JPG/PNG to binary and stores in MySQL  
✅ Clean and professional blue/gray UI

🛠️ Tech Stack

Layer         Technologies Used  
Backend       Python, Django  
Frontend      HTML, CSS  
Database      MySQL  
Tools         Git, GitHub  

🧠 How It Works

- User selects one of three options: New User, Existing User, or Admin  
- New Users can register with username & password  
- Existing Users can log in and view their own uploads  
- Admin logs in with fixed credentials to view all uploads  
- Uploaded images are converted to binary and saved in MySQL  
- Clean UI with role-based access and data privacy  

🛠️ Setup Instructions

Clone the project  
git clone https://github.com/Nithishkumar1511/secure-wallet-django.git

Navigate to the project folder
cd secure-wallet-Django

Activate the virtual environment (Windows)
venv\Scripts\activate

Install required packages
pip install -r requirements.txt

Run the development server
python manage.py runserver

🗄️ Database Setup
Create a MySQL database: secure_wallet_db
Update the database settings in settings.py

Run migrations:
python manage.py makemigrations
python manage.py migrate

📌 Author
👨‍💻 Nithishkumar S
📧 finnnithish@gmail.com

🌐 License
This project is open-source and available under the MIT License.

