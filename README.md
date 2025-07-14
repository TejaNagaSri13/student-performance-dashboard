# 📘 Student Performance Dashboard

A simple and interactive **Streamlit** web app to analyze student academic performance from a CSV file.  
Upload student marks, and instantly view insightful visualizations and statistics like subject-wise averages, top performers, pass/fail ratios, and a correlation heatmap.

---

## 📊 Features

- 📤 Upload CSV file of student scores
- 📈 Subject-wise average scores (bar chart)
- 🏆 Top 5 performers (with emojis 🥇🥈🥉)
- ✅ Pass/Fail analysis (adjustable pass mark, pie chart)
- 📉 Correlation heatmap of subjects
- 📥 Download analyzed data as CSV

---

## 🧠 Technologies Used

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)

---

## 📁 Sample CSV Format
Name,Math,Science,English,History
Aditi Singh,88,92,85,80
Rahul Verma,76,65,70,72
Simran Kaur,95,90,92,93
...


> ✅ Ensure the first column is the student name, followed by numeric scores for each subject.

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/TejaNagaSri13/student-performance-dashboard.git
cd student-performance-dashboard

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt


3️⃣ Run the Streamlit app
```bash
streamlit run app.py

🌐 Live Demo
👉 Click here to open the live app

📤 Exported Output
The dashboard adds Total, Average, and Passed_All columns.

You can download the processed CSV with a single click.

🙋‍♀️ Author : 
👤 TejaNagasri Kola

🎓 Final Year Student, Sasi Institute of Technology and Engineering

💼 LinkedIn Profile : www.linkedin.com/in/teja-nagasri-kola-27a752280

🏁 Future Enhancements (Ideas)
Login system (admin/teacher access)
Subject-wise toppers
Export PDF reports
Attendance data integration

📜 License
This project is open source and free to use under the MIT License.
