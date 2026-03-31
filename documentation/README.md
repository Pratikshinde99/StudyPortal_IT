# 📚 SPPU Study Material Portal

<div align="center">

![Study Portal Banner](https://img.shields.io/badge/SPPU-Study%20Portal-6366f1?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHBhdGggZD0iTTQgMTloNXYtOEg0eiIvPjxwYXRoIGQ9Ik0xNCAxOWg1di04aC01eiIvPjxwYXRoIGQ9Ik05IDEwaDZ2OUg5eiIvPjxwYXRoIGQ9Ik05IDd2M00xNSA3djMiLz48L3N2Zz4=)

**A modern, beautiful web portal for SPPU Information Technology students to access organized study materials, notes, and resources.**

[![Python](https://img.shields.io/badge/Python-3.11.5-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=flat&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat)](LICENSE)

[🌐 Live Demo](#) • [📖 Documentation](#features) • [🐛 Report Bug](https://github.com/Pratikshinde99/StudyPortal/issues) • [✨ Request Feature](https://github.com/Pratikshinde99/StudyPortal/issues)

</div>

---

## 🎯 **Overview**

The **SPPU Study Material Portal** is a comprehensive web application designed specifically for Information Technology students at Savitribai Phule Pune University (SPPU). It provides a centralized platform to access semester-wise study materials, previous year papers, notes, and other educational resources.

### ✨ **Key Highlights**

- 🎨 **Modern Dark Theme UI** - Beautiful, eye-friendly interface with smooth animations
- 📱 **Fully Responsive** - Works seamlessly on desktop, tablet, and mobile devices
- 🔐 **Secure Admin Panel** - Protected admin area for content management
- 📚 **Organized Content** - Materials organized by semester and subject
- ⚡ **Fast Performance** - Quick loading and efficient PDF delivery
- 🗄️ **MongoDB GridFS** - Efficient storage and retrieval of large PDF files
- 🔍 **Easy Navigation** - Intuitive semester and subject-based browsing

---

## 🚀 **Features**

### For Students
- ✅ Browse study materials by semester (SEM 1 to SEM 8)
- ✅ Access subject-wise organized content
- ✅ Download or view PDFs directly in browser
- ✅ Clean, distraction-free reading experience
- ✅ No login required for viewing materials

### For Admins
- ✅ Secure login system with bcrypt password hashing
- ✅ Upload PDFs with semester and subject categorization
- ✅ Manage all uploaded materials
- ✅ View all PDFs in the system
- ✅ Session-based authentication

### Technical Features
- ✅ MongoDB GridFS for efficient file storage
- ✅ Environment-based configuration
- ✅ Flash messages for user feedback
- ✅ Error handling and validation
- ✅ Production-ready deployment configuration

---

## 🛠️ **Tech Stack**

| Category | Technology |
|----------|-----------|
| **Backend** | Python 3.11.5, Flask 2.3.3 |
| **Database** | MongoDB Atlas (Cloud) / Local MongoDB |
| **File Storage** | GridFS (MongoDB) |
| **Authentication** | Flask Sessions, Bcrypt |
| **Frontend** | HTML5, CSS3 (Modern Dark Theme), Vanilla JavaScript |
| **Deployment** | Heroku / Render / Railway (Ready) |
| **Security** | python-dotenv, bcrypt, flask-talisman |

---

## 📋 **Prerequisites**

Before you begin, ensure you have the following installed:

- **Python 3.11+** - [Download Python](https://www.python.org/downloads/)
- **MongoDB** (Local) OR **MongoDB Atlas Account** (Cloud) - [Get MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **pip** - Python package installer (comes with Python)

---

## 🔧 **Installation & Setup**

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/Pratikshinde99/StudyPortal.git
cd StudyPortal
```

### **Step 2: Create Virtual Environment**

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 4: Set Up MongoDB Atlas (Recommended)**

1. **Create a MongoDB Atlas Account**
   - Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
   - Sign up for a free account

2. **Create a New Cluster**
   - Click "Build a Database"
   - Choose the **FREE** tier (M0)
   - Select your preferred cloud provider and region
   - Click "Create Cluster"

3. **Create Database User**
   - Go to "Database Access" in the left sidebar
   - Click "Add New Database User"
   - Choose "Password" authentication
   - Set username and password (save these!)
   - Set user privileges to "Read and write to any database"
   - Click "Add User"

4. **Configure Network Access**
   - Go to "Network Access" in the left sidebar
   - Click "Add IP Address"
   - Click "Allow Access from Anywhere" (for development)
   - Click "Confirm"

5. **Get Connection String**
   - Go to "Database" in the left sidebar
   - Click "Connect" on your cluster
   - Choose "Connect your application"
   - Copy the connection string
   - It looks like: `mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority`

### **Step 5: Configure Environment Variables**

1. **Copy the example environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file with your actual credentials:**

   ```bash
   # MongoDB Atlas Connection (replace with your actual connection string)
   MONGODB_URI=mongodb+srv://your-username:your-password@cluster0.xxxxx.mongodb.net/study_portal?retryWrites=true&w=majority
   
   # Generate a secure secret key
   SECRET_KEY=your-generated-secret-key-here
   
   # Admin Credentials
   ADMIN_USERNAME=Pratik
   ADMIN_PASSWORD=@Pratik9890
   
   # Development Mode
   FLASK_DEBUG=true
   FLASK_ENV=development
   ```

3. **Generate a secure SECRET_KEY:**
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```
   Copy the output and paste it as your `SECRET_KEY` in `.env`

4. **(Optional) Generate a hashed password for production:**
   ```bash
   python -c "import bcrypt; print(bcrypt.hashpw(b'@Pratik9890', bcrypt.gensalt()).decode())"
   ```
   Add the output to `.env` as `ADMIN_PASSWORD_HASH` and remove `ADMIN_PASSWORD`

### **Step 6: Run the Application**

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`

🎉 **Success!** Open your browser and navigate to `http://localhost:5000`

---

## 📁 **Project Structure**

```
StudyPortal/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── runtime.txt            # Python version for deployment
├── Procfile               # Heroku deployment configuration
├── .env                   # Environment variables (DO NOT COMMIT)
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
│
├── static/                # Static assets
│   └── style.css          # Modern dark theme CSS
│
├── templates/             # HTML templates
│   ├── welcome.html       # Landing page
│   ├── login.html         # Admin login page
│   ├── upload.html        # PDF upload page (admin)
│   ├── view_pdfs.html     # All PDFs listing (admin)
│   ├── sem3.html          # Semesters overview page
│   ├── semester_subjects.html  # Subject listing for a semester
│   ├── subject_pdfs.html  # PDFs for a specific subject
│   ├── contact.html       # Contact page
│   └── search.html        # Search functionality (future)
│
└── venv/                  # Virtual environment (not in git)
```

---

## 🎓 **Supported Semesters & Subjects**

<details>
<summary><b>Click to expand semester details</b></summary>

### **Semester 1**
- M1 (Mathematics I)
- Physics
- BEE (Basic Electrical Engineering)
- FPL (Fundamentals of Programming Languages)
- EG (Engineering Graphics)

### **Semester 2**
- Chemistry
- EM (Engineering Mathematics)
- M2 (Mathematics II)
- PPS (Programming Problem Solving)
- BXE (Basic Electronics Engineering)

### **Semester 3**
- DM (Discrete Mathematics)
- LDCO (Logic Design & Computer Organization)
- DSA (Data Structures & Algorithms)
- OOPS (Object-Oriented Programming)
- BCN (Basic Computer Networks)

### **Semester 4**
- M3 (Mathematics III)
- PA (Probability & Applications)
- DBMS (Database Management Systems)
- CG (Computer Graphics)
- SE (Software Engineering)

### **Semester 5**
- OS (Operating Systems)
- TOC (Theory of Computation)
- ML (Machine Learning)
- HCI (Human-Computer Interaction)
- ADMBS (Advanced Database Management Systems)

### **Semester 6**
- CNS (Computer Network Security)
- DSBDA (Data Science & Big Data Analytics)
- WAD (Web Application Development)

### **Semester 7**
- ISR (Information Security & Risk)
- SPM (Software Project Management)
- DL (Deep Learning)
- Mobile Computing
- Wireless Communication

### **Semester 8**
- DS (Distributed Systems)
- STARTUP (Startup & Entrepreneurship)
- Blockchain Technology
- NLP (Natural Language Processing)

</details>

---

## 🔐 **Admin Access**

### **Default Credentials** (Change in production!)
- **Username:** Set in `.env` as `ADMIN_USERNAME`
- **Password:** Set in `.env` as `ADMIN_PASSWORD`

### **Admin Features:**
1. Navigate to `/login`
2. Enter admin credentials
3. Access the upload page to add new materials
4. View all uploaded PDFs
5. Logout when done

### **Security Best Practices:**
- ✅ Always use environment variables for credentials
- ✅ Use bcrypt hashed passwords in production
- ✅ Change default credentials immediately
- ✅ Keep `.env` file out of version control
- ✅ Use HTTPS in production

---

## 🚀 **Deployment**

### **Deploy to Heroku**

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set MONGODB_URI="your-mongodb-atlas-uri"
   heroku config:set SECRET_KEY="your-secret-key"
   heroku config:set ADMIN_USERNAME="your-admin-username"
   heroku config:set ADMIN_PASSWORD="your-admin-password"
   heroku config:set FLASK_DEBUG="false"
   heroku config:set FLASK_ENV="production"
   ```

5. **Deploy**
   ```bash
   git push heroku master
   ```

6. **Open Your App**
   ```bash
   heroku open
   ```

### **Deploy to Render**

1. Create a new Web Service on [Render](https://render.com/)
2. Connect your GitHub repository
3. Set environment variables in Render dashboard
4. Deploy automatically on every push

### **Deploy to Railway**

1. Create a new project on [Railway](https://railway.app/)
2. Connect your GitHub repository
3. Add environment variables
4. Deploy with one click

---

## 🧪 **Usage Guide**

### **For Students:**

1. **Browse Materials**
   - Visit the homepage
   - Click "Browse Materials"
   - Select your semester
   - Choose your subject
   - Download or view PDFs

2. **Contact**
   - Click "Contact" in the navigation
   - Find contact information and support

### **For Admins:**

1. **Login**
   - Navigate to `/login`
   - Enter your credentials

2. **Upload Materials**
   - Select semester from dropdown
   - Choose subject (auto-populated based on semester)
   - Select PDF file
   - Click "Upload Material"

3. **Manage PDFs**
   - View all uploaded PDFs
   - Download or delete as needed

---

## 🛡️ **Security Features**

- ✅ **Bcrypt Password Hashing** - Secure password storage
- ✅ **Environment Variables** - Sensitive data protection
- ✅ **Session Management** - Secure admin sessions
- ✅ **CSRF Protection** - Form security
- ✅ **Input Validation** - File type and size validation
- ✅ **Error Handling** - Graceful error management
- ✅ **Gitignore Protection** - Prevents committing sensitive files

---

## 🤝 **Contributing**

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### **Contribution Ideas:**
- 🔍 Add search functionality
- 📊 Implement analytics dashboard
- 🎨 Improve UI/UX
- 📱 Create mobile app
- 🔔 Add notification system
- 💬 Implement comments/reviews
- 🌐 Add multi-language support

---

## 🐛 **Troubleshooting**

### **Common Issues:**

**1. MongoDB Connection Error**
```
Solution: Check your MONGODB_URI in .env file
- Ensure password doesn't contain special characters (URL encode if needed)
- Verify network access is configured in MongoDB Atlas
- Check if your IP is whitelisted
```

**2. Module Not Found Error**
```
Solution: Install dependencies
pip install -r requirements.txt
```

**3. Port Already in Use**
```
Solution: Change the port or kill the process
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9
```

**4. Admin Login Not Working**
```
Solution: Check your .env file
- Verify ADMIN_USERNAME and ADMIN_PASSWORD are set correctly
- Ensure .env file is in the root directory
- Check for typos in credentials
```

---

## 📝 **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 **Author**

**Pratik Shinde**

- GitHub: [@Pratikshinde99](https://github.com/Pratikshinde99)
- Email: pratikshinde99@example.com

---

## 🙏 **Acknowledgments**

- SPPU IT Department for the curriculum structure
- Flask community for excellent documentation
- MongoDB for reliable database services
- All contributors and users of this portal

---

## 📊 **Project Stats**

![GitHub stars](https://img.shields.io/github/stars/Pratikshinde99/StudyPortal?style=social)
![GitHub forks](https://img.shields.io/github/forks/Pratikshinde99/StudyPortal?style=social)
![GitHub issues](https://img.shields.io/github/issues/Pratikshinde99/StudyPortal)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Pratikshinde99/StudyPortal)

---

## 🗺️ **Roadmap**

- [x] Basic portal functionality
- [x] Admin authentication
- [x] PDF upload and management
- [x] Semester-wise organization
- [ ] Search functionality
- [ ] User registration
- [ ] Bookmarks/Favorites
- [ ] Download statistics
- [ ] Mobile application
- [ ] API for third-party integrations

---

## 💬 **Support**

If you like this project, please give it a ⭐ on GitHub!

For support, email pratikshinde99@example.com or open an issue on GitHub.

---

<div align="center">

**Made with ❤️ for SPPU IT Students**

[⬆ Back to Top](#-sppu-study-material-portal)

</div>
