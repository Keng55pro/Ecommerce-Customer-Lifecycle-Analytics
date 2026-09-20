# 🛒 E-Commerce Customer Analytics & Churn Prediction

## 📂 โครงสร้างโปรเจค
- `data/` : เก็บข้อมูลดิบ (OnlineRetail.csv) และฐานข้อมูล SQLite (ecommerce.db)
- `src/` : เก็บไฟล์โมเดล XGBoost (.pkl)
- `notebooks/` : Jupyter Notebook สำหรับประมวลผลข้อมูลและเทรนโมเดล
- `app.py` : Streamlit Interactive Web Application

## 🚀 วิธีเปิดใช้งาน
1. วางไฟล์ `OnlineRetail.csv` ไว้ที่ `data/raw/`
2. ติดตั้ง Library:
   ```bash
   pip install -r requirements.txt