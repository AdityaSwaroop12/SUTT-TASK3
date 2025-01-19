📚 E-LibDeck: Your Ultimate Library Management System
Welcome to E-LibDeck – a seamless e-library management system designed for students and librarians! 🎓📖 Built with Django, it provides robust features for managing books, user authentication, borrowing, returning, and more. 🖥️✨

🌟 Features at a Glance
🔐 Authentication & Profiles
Students: Google Sign-In restricted to BITS email 📧
Librarians: Classic username-password login 🔑
Personalized dashboards:
📄 Students: Name, email, hostel & room details
🏢 Librarians: PSRN, name, and more!
📚 Book Management
📋 Book List: Available to both students and librarians
📤 Excel Upload: Librarians can add books via an Excel template
🖼️ Manual Entry: Option to upload book cover images
🔎 Search Functionality: Easily find books by name
📖 Book Details:
Students: View details like author, publisher, ISBN, availability
Librarians: Edit details and update book information
🤝 Borrowing of books
📅 Students:
Borrow books via the portal
Borrowing count
🧾 Librarians:
View who has borrowed books 📌
Configure late fee rules 📊
🌟 Additional Features
🗨️ Feedback System:
Students: Submit feedback with optional images
Librarians: Review feedback in a dedicated section
🚀 Deployment
The application is hosted on PythonAnywhere. 🌐

🛠️ Tech Stack
Backend: Django 🐍
Frontend: Django Templates, Bootstrap 🎨
Database: SQLite 📂
📋 Installation & Setup
Prerequisites
Python 3.x 🐍
Django 4.x 🌟
SQLite 📂
Google Cloud Console (for OAuth setup) 🌐
Steps to Run Locally
Clone the repository:
git clone https://github.com/YourUsername/E-LibDeck.git
Navigate to the project directory:
cd E-LibDeck
Install dependencies:
pip install -r requirements.txt
Configure your Google OAuth settings.
Run migrations:
python manage.py migrate
Start the development server:
python manage.py runserver
💻 Contributing
We welcome contributions! 🤝 Feel free to submit issues or pull requests to enhance the project.

📜 License
This project is licensed under the MIT License.

🎯 Future Enhancements
📱 Add mobile responsiveness
🌍 Multilingual support
📦 Integrate book reservation system

🛡️ Crafted with ❤️ by Aditya Swaroop
