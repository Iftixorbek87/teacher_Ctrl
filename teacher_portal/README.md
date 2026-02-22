# O'qituvchi Portali — Django Dasturi

## 📋 Tavsif
Ushbu dastur o'qituvchilarga o'quvchilar guruhlarini boshqarish va ularning vazifa bajarishini kuzatish imkonini beradi.

### Asosiy xususiyatlar:
- ✅ Guruh yaratish va boshqarish
- ✅ O'quvchilar ro'yxati tuzish
- ✅ Har bir o'quvchi uchun 75 ta (yoki belgilangan sonli) vazifani belgilash
- ✅ Vazifalarni belgilash — bir klik bilan (AJAX, sahifa yangilanmaydi)
- ✅ O'quvchi 75 ta vazifani bajarganda avtomatik "Bitirdi" nishoni
- ✅ Admin panel orqali to'liq boshqaruv
- ✅ Classic va professional dizayn

---

## 🚀 O'rnatish va ishga tushirish

### 1. Python virtual muhit yaratish (tavsiya etiladi)
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 2. Kerakli kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 3. Ma'lumotlar bazasini tayyorlash
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Superuser (admin) yaratish
```bash
python manage.py createsuperuser
# Username, email, parol kiriting
```

### 5. Serverni ishga tushirish
```bash
python manage.py runserver
```

### 6. Brauzerda ochish
- **Asosiy sahifa:** http://127.0.0.1:8000/
- **Admin panel:** http://127.0.0.1:8000/admin/

---

## 📁 Loyiha tuzilmasi
```
teacher_portal/
├── manage.py
├── requirements.txt
├── teacher_portal/          # Asosiy sozlamalar
│   ├── settings.py
│   └── urls.py
├── apps/
│   ├── groups/              # Guruhlar moduli
│   │   ├── models.py        # Group modeli
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── admin.py
│   └── students/            # O'quvchilar moduli
│       ├── models.py        # Student, TaskCompletion modellari
│       ├── views.py
│       ├── urls.py
│       ├── forms.py
│       └── admin.py
└── templates/
    ├── base/                # Asosiy shablonlar (login, dashboard)
    ├── groups/              # Guruh sahifalari
    └── students/            # O'quvchi sahifalari
```

---

## 🎯 Ishlatish qo'llanmasi

1. **Kirish:** `/login/` sahifasida tizimga kiring
2. **Guruh yaratish:** "Yangi guruh" tugmasi → nom va vazifalar sonini kiriting
3. **O'quvchi qo'shish:** Guruh sahifasidan "O'quvchi qo'shish" tugmasi
4. **Vazifani belgilash:** Jadvalda ✓ checkboxni bosing — avtomatik saqlanadi
5. **Admin panel:** `/admin/` — barcha ma'lumotlarni to'liq boshqarish

---

## ⚙️ Sozlamalar
`teacher_portal/settings.py` faylida:
- `DEBUG = False` — ishlab chiqarish uchun
- `SECRET_KEY` — o'zgartiring!
- `TOTAL_TASKS = 75` — standart vazifalar soni
