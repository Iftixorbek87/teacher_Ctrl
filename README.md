# O'qituvchi Portali — v2

## Yangi tuzilma: Patok → Guruh → O'quvchilar

```
Patok (masalan: 2024-yil 1-patok)
  └── Guruh (masalan: A-guruh, B-guruh)
        └── O'quvchilar + Vazifalar jadval
```

## O'rnatish

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# yoki: source .venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Brauzerda: http://127.0.0.1:8000

## Xususiyatlar
- ✅ Patok yaratish va boshqarish
- ✅ Patok ichida guruh qo'shish
- ✅ Guruh ichida o'quvchilar + vazifalar jadval
- ✅ **Patok sahifasida guruh nomi bo'yicha qidiruv**
- ✅ **Guruh sahifasida ism-familya bo'yicha qidiruv**
- ✅ AJAX vazifa belgilash (sahifa yangilanmaydi)
- ✅ 75 ta (yoki belgilangan) vazifa bajarilganda 🏆 nishon
- ✅ Breadcrumb navigatsiya
- ✅ Admin panel: /admin/
