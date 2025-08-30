# ALX Backend Caching Property Listings

A Django-based property listing application with multi-level caching using Redis. The project demonstrates view-level caching, low-level queryset caching, cache invalidation using signals, and cache metrics analysis. PostgreSQL is used for persistent storage, and Docker is used to containerize both PostgreSQL and Redis.

---

## Features

- **Property Listings**: Create, update, and view properties.
- **Caching**:
  - View-level caching (15 minutes).
  - Low-level queryset caching (1 hour) using Redis.
  - Automatic cache invalidation on property create/update/delete.
  - Cache hit/miss metrics tracking.
- **Database**: PostgreSQL for persistent storage.
- **Containerization**: Dockerized PostgreSQL and Redis for realistic development environment.

---

## Project Structure

```

alx\_backend\_caching\_property\_listings/
├── alx\_backend\_caching\_property\_listings/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── properties/
│   ├── models.py
│   ├── views.py
│   ├── utils.py
│   ├── signals.py
│   └── ...
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── README.md
└── venv/  (ignored by git)

````

---

## Setup & Installation

1. **Clone the repository:**
```bash
git clone <repo-url>
cd alx_backend_caching_property_listings
````

2. **Create and activate a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run Docker containers for PostgreSQL and Redis:**

```bash
docker-compose up -d
```

5. **Apply migrations:**

```bash
python manage.py migrate
```

6. **Create a superuser:**

```bash
python manage.py createsuperuser
```

7. **Run the development server:**

```bash
python manage.py runserver
```

---

## Usage

* **List properties:**
  `GET /properties/` (cached for 15 minutes)

* **Low-level cached queryset:**
  The `get_all_properties()` utility caches all properties for 1 hour.

* **Cache metrics:**
  Use `get_redis_cache_metrics()` in `properties/utils.py` to retrieve cache hits, misses, and hit ratio.

---

## Cache Invalidation

* Signals (`post_save`, `post_delete`) automatically invalidate the `all_properties` cache when properties are created, updated, or deleted.

---

## Technologies Used

* Django 5.2.4
* PostgreSQL
* Redis
* Docker
* django-redis
* Python 3.12

---


