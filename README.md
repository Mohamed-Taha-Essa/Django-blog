
# Simple Django Blog Application

This is a basic Django blog project that demonstrates the use of both **function-based views (FBVs)** and **class-based views (CBVs)** for managing blog posts. It includes functionality to list, create, update, delete, and view blog posts.

---

## Features

1. **Post Listing**: Displays a list of all blog posts.
2. **Post Details**: Shows the details of a specific post.
3. **Create Post**: Allows creating a new blog post.
4. **Update Post**: Allows editing an existing blog post.
5. **Delete Post**: Enables deleting a blog post.

---

## Requirements

- **Python**: >= 3.8
- **Django**: >= 4.x
- **SQLite** (default database for Django, or another configured database)

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

---

## URL Patterns

### Function-Based Views (FBVs)

| URL Pattern                  | Description                  |
|------------------------------|------------------------------|
| `/post_list/`                | List all posts              |
| `/post_list/<int:pk>`        | Post details                |
| `/creat_post/`               | Create a new post           |
| `/update_post/<int:pk>`      | Update a specific post      |
| `/delet_post/<int:pk>`       | Delete a specific post      |

### Class-Based Views (CBVs)

| URL Pattern                  | View                       | Description                  |
|------------------------------|---------------------------|------------------------------|
| `/`                          | `PostList`                | List all posts              |
| `/post/<int:pk>/`            | `PostDetail`              | Post details                |
| `/post/new/`                 | `PostCreate`              | Create a new post           |
| `/post/<int:pk>/edit/`       | `PostUpdate`              | Update a specific post      |
| `/post/<int:pk>/delete/`     | `PostDelete`              | Delete a specific post      |

---

## Directory Structure

```
myblog/
│
├── posts/
│   ├── views.py         # Contains FBVs and CBVs
│   ├── models.py        # Post model definition
│   ├── urls.py          # URL configurations
│   ├── templates/       # HTML templates for the app
│   └── forms.py         # Optional: Django forms for posts
│
├── manage.py            # Django management script
├── settings.py          # Django project settings
└── urls.py              # Project-level URL configurations
```

---

## Static and Media Files

- **Static Files**: Served from `STATIC_URL` during development.
- **Media Files**: Uploaded files are served from `MEDIA_URL` during development.

---

## Contribution

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

---


## Acknowledgments

- Built using Django's function-based and class-based views.
- Simplified for educational purposes.



