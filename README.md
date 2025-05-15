# **City Navigator**

# A Django application called **City Navigator** that allows users to:

- **Create and manage 2D maps** (grids) stored in the database.
- **Determine if a path exists** between two points in a map using **4-directional movement**.

---

## **Detailed Requirements**

### 1. Users

- Use Django’s built-in authentication (or a custom setup if you prefer).
- Each **user** can create multiple maps.
- (Optional but recommended) Make maps **public** or **private** (private maps visible only to their owner).

### 2. Map Model

In `maps/models.py`, `Map` should have:

- **Name**: A unique identifier for the map that is human-readable.
- **Owner**: A relationship to the user who created the map.
- **Layout**: A 2D grid representation of the city with roads and blocked areas.
- **Public** (optional): A flag indicating whether other users can view this map.

Example structure for the layout:

```json
[
  ["R", "R", "#"],
  ["R", "#", "R"],
  ["R", "R", "R"]
]
```

where:
`"R"` = road (traversable)
`"#"` = blocked (impassable)

### 3. MapView

Implement **CRUD operations** for the Map model using Django views (class-based views). Specifically:

- **Create**: Let a user provide a name, and a 2D layout (JSON) for the map.
- **Read**:

  - **ListView**: Show all maps belonging to the current user.
  - **DetailView**: Show a specific map's name and layout.
- **Update**: Allow the user to edit the map's layout.
- **Delete**: Allow the user to delete a map.

Make sure you **respect ownership**:

> Only the owner can update or delete a map (unless you add more complex permissions).

### 4. MapNavigationView

- Takes a **map ID** (or slug) to identify which map's layout to use.
- Receives **start and end coordinates** (`(row_s, col_s)` and `(row_e, col_e)`) from the user (via GET request).
- Runs a **pathfinding function** to determine if there is a path from start to end. Movement is restricted to up, down, left, right on `"R"` cells only.
- Return **success or failure** based on whether a path exists. Output in **JSON format**.

### 5. Testing

- **Model**: Creating a map, ownership, etc.
- **MapView**: Ensuring only owners can edit or delete a map, etc.
- **MapNavigationView**: Checking correctness. Test both reachable and unreachable paths, plus any edge cases you seem fit.

---

## **Setup Instructions**

**0. Prerequisites**

- Python (recommended 3.8 or higher)
- pip (Python package manager)

**1. Clone the repository**

```bash
   git clone <repository-url>
   cd <project-directory>
```

**2. Create and activate a virtual environment**

```bash
   # Install virtualenv if not already installed
   pip install virtualenv

   # On Windows
   python -m virtualenv env
   env\Scripts\activate

   # On macOS/Linux
   python3 -m virtualenv env
   source env/bin/activate
```

**3. Install dependencies**

```bash
   pip install -r requirements.txt
   # Or if no requirements.txt exists:
   pip install django
```

**4. Apply migrations**

```bash
   python manage.py makemigrations
   python manage.py migrate
```

**5. Create a superuser** (optional)

```bash
   python manage.py createsuperuser
```

**6. Run the development server**

```bash
   python manage.py runserver
```

   The application will be available at http://127.0.0.1:8000/

**7. Running tests**

```bash
   python manage.py test maps
```

## **Structure of the Django App**

city-navigator/               # Project root
│
├── env/                      # Virtual environment (should be in .gitignore)
│
├── maps/                     # Django app
│   ├── migrations/           # Database migrations
│   │   └── __init__.py
│   ├── __pycache__ /
│   ├── __init__.py
│   ├── admin.py             # Model admin registrations
│   ├── apps.py              # App config
│   ├── models.py            # Map model definition
│   ├── serializers.py       # DRF serializers
│   ├── tests.py             # Test cases
│   ├── urls.py              # App URL routes
│   └── views.py             # App Views
│
├── quickstart/              # project config folder
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL routes
│   └── wsgi.py
│
├── .gitignore
├── db.sqlite3               # SQLite database
├── manage.py                # Django CLI tool
└── README.md                # Project documentation
