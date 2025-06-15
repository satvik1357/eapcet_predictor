
````markdown
# 🎓 AP EAPCET College Predictor

A web-based tool to help students predict eligible engineering colleges based on their AP EAPCET rank, gender, category, and preferences using last year's cutoff data.

🌐 **Live Demo**: [https://eapcet-predictor.onrender.com](https://eapcet-predictor.onrender.com)

---

## 📌 Features

- ✅ Predict colleges based on **rank, gender, and category**
- 🎯 Optional filters for **branch**, **district**, and **college type**
- 📊 Results show college name, branch, cutoff, fees, etc.
- ⚡ Built with Flask (backend) and Bootstrap (frontend)
- 📂 Uses Excel dataset (`.xlsx`) with 2023 cutoff ranks

---

## 🖥️ Tech Stack

| Layer       | Technology                     |
|-------------|--------------------------------|
| Frontend    | HTML, CSS, Bootstrap           |
| Backend     | Python, Flask                  |
| Data Source | Excel (`pandas`, `openpyxl`)   |
| Hosting     | [Render](https://render.com)   |

---

## 🚀 How It Works

1. User enters their **EAPCET rank**, **gender**, **category**
2. User optionally selects:
   - Preferred **branch**
   - **District**
   - **College type** (Govt/Private)
3. The backend reads the **Excel file** and filters colleges:
   - Compares the input rank with cutoff for that category/gender
   - Applies filters if selected
4. Results are shown in a clean table with:
   - College name, branch, district, type, cutoff rank, and fee

---

## 🧾 Dataset Info

The dataset used is from **AP EAPCET 2023** counseling data with cutoff ranks across categories and branches.

- File: `APEAPCET2023LASTRANKDETAILS.xlsx`
- Required Python libraries:
  ```txt
  flask
  pandas
  openpyxl
````

---

## 🔧 Local Setup Instructions

1. **Clone the repo:**

   ```bash
   git clone https://github.com/your-username/eapcet-predictor.git
   cd eapcet-predictor
   ```

2. **Create virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**

   ```bash
   python app.py
   ```

5. **Visit in browser:**

   ```
   http://localhost:10000/
   ```

---

## 🌍 Live Deployment

This app is deployed using **Render** and available here:

👉 **[https://eapcet-predictor.onrender.com](https://eapcet-predictor.onrender.com)**

---

## 🙌 Future Enhancements

* Downloadable results as PDF or CSV
* Add AP & TS Polycet / ICET support
* Add college info pages with links
* Support for multiple years of data

---

## 👨‍💻 Author

**Sai Satwik**
📬 Feel free to reach out for collaborations or suggestions!

---

## 📜 License

This project is open-source and free to use under the **MIT License**.

````

---

### 2. **Run Git Commands in Terminal**

Now open terminal in your project folder and run:

```bash
git add README.md
git commit -m "Add detailed README.md with deployment info"
git push origin main
````

---

After that, go to your GitHub repo — you'll see your beautiful `README.md` on the home page. ✅

Let me know if you'd like to include:

* A preview image or screenshot
* Deployment badge or tech badges
* Download button in UI

Happy deploying! 🚀
