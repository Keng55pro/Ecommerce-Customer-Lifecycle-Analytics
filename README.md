# 🛒 E-Commerce Customer Analytics & Churn Prediction

## โครงสร้างโฟลเดอร์
```
Ecommerce-analytics/
├── data/
│   ├── raw/
│   │   └── OnlineRetail.csv          
│   └── ecommerce.db                  
├── src/
│   ├── churn_xgboost_model.pkl      
│   └── model_features.pkl            
├── notebooks/
│   └── 01_data_cleaning.ipynb       
├── app.py                           
├── requirements.txt                 
└── README.md
```

- `data/` : เก็บข้อมูลดิบ (OnlineRetail.csv) และฐานข้อมูล SQLite (ecommerce.db)
- `src/` : เก็บไฟล์โมเดล XGBoost (.pkl)
- `notebooks/` : Jupyter Notebook สำหรับประมวลผลข้อมูลและเทรนโมเดล
- `app.py` : Streamlit Interactive Web Application

## 🚀 วิธีเปิดใช้งาน
1. วางไฟล์ `OnlineRetail.csv` ไว้ที่ `data/raw/`
2. ติดตั้ง Library:
   ```bash
   pip install -r requirements.txt
Link https://ecommerce-customer-lifecycle-analytics-hpye6ra6ezzpmasyapr4om.streamlit.app/
