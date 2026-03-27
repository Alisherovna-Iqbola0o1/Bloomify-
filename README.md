🌸 Bloomify

---Bloomify 🌸 – bu Django va Django REST Framework yordamida yaratilgan, ishlab chiqarishga tayyor gul bozori backend tizimi. Loyihada mamlakatlarga qarab gul kategoriyalari, rasm va tafsilotlari bilan mahsulot ma’lumotlari, savatcha va buyurtma tizimi, rol asosida autentifikatsiya (mijoz, sotuvchi, admin) va kartaga yoki naqd to‘lov orqali xavfsiz to‘lovlar mavjud. Shuningdek, ElasticSearch yordamida mahsulotlarni tezkor va ilg‘or qidirish imkoniyati mavjud.

Bloomify foydalanuvchilarga kategoriyalar bo‘yicha gullarni ko‘rib chiqish, mahsulotlarni filtrlash va buyurtmalarni tezda joylashtirish imkonini beradi. Adminlar va sotuvchilar inventarizatsiyani boshqarish, buyurtmalarni kuzatish va savdoni monitoring qilishni oson amalga oshirishlari mumkin. Tizim media fayllarni yuklash, CORS orqali frontend bilan integratsiya, va JWT autentifikatsiya orqali xavfsiz API kirishini qo‘llab-quvvatlaydi.

---🚀 Asosiy funksiyalar
Foydalanuvchilarni boshqarish: ro‘yxatdan o‘tish, login, profilni yangilash
Kategoriyalar va mahsulotlar: CRUD operatsiyalari bilan to‘liq boshqaruv
Savatcha tizimi: mahsulotlarni qo‘shish, o‘zgartirish va olib tashlash
Buyurtmalar: buyurtma berish va tarixini kuzatish
Rol asosida autentifikatsiya: mijoz, sotuvchi, admin
To‘lovlar: kartaga yoki naqd to‘lovni qo‘llab-quvvatlash
Media fayllar: mahsulot rasmlari uchun upload imkoniyati
Qidiruv: ElasticSearch yordamida ilg‘or qidiruv
CORS qo‘llab-quvvatlash: frontend bilan muammosiz integratsiya

---🛠️ Texnologiyalar
Backend: Django, Django REST Framework
Autentifikatsiya: JWT
Database: SQLite (default) / PostgreSQL orqali sozlanadi
Search: ElasticSearch
CORS: django-cors-headers
Muhit sozlamalari: python-dotenv
Email backend: konsol (development uchun)
---⚙️ O‘rnatish va ishga tushirish

✅Repository-ni klon qilish:
    1.git clone <repository-url>
    2.cd Bloomify
    3.Virtual environment yaratish va faollashtirish
    4.python -m venv venv
    5.source venv/bin/activate      # Windows: venv\Scripts\activate

✅Talab qilinadigan paketlarni o‘rnatish:
    1.pip install -r requirements.txt
    2. .env faylini yaratib, quyidagilarni qo‘shing

    SECRET_KEY=your_secret_key
    DEBUG=True
    DB_ENGINE=django.db.backends.sqlite3
    DB_NAME=db.sqlite3
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=
    ELASTICSEARCH_HOST=localhost:9200

✅Migratsiyalarni bajarish:
    1.python manage.py migrate
    2.Admin user yaratish (optional)
    3.python manage.py createsuperuser

✅Serverni ishga tushirish:
    1.python manage.py runserver

📌 Foydalanish:
    API manzili: http://localhost:8000/api/
    Admin panel: http://localhost:8000/admin/
    Postman yoki boshqa API client yordamida endpointlarni sinab ko‘rish mumkin

🤝 Hissa qo‘shish:

✅Hissalar qabul qilinadi!

Repository-ni fork qiling
Yangi branch yarating (git checkout -b feature-name)
O‘zgarishlarni commit qiling (git commit -m 'Add feature')
Branch-ni push qiling (git push origin feature-name)
Pull Request oching