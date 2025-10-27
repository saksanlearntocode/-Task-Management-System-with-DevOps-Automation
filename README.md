# To-Do Web Application

A simple and elegant To-Do web application built with Python Flask and SQLite. This application allows users to create, view, edit, complete, and delete tasks with a modern and responsive user interface.

## Features

- ✅ Add new tasks with title and description
- 📝 Edit existing tasks
- ✔️ Mark tasks as completed/not completed
- 🗑️ Delete tasks
- 📱 Responsive design for mobile and desktop
- 💾 SQLite database for data persistence
- 🎨 Modern UI with gradient backgrounds and animations
- 📋 Task status tracking (pending/completed)
- ⏰ Creation timestamp for each task

## Project Structure

```
todo-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── todo.db               # SQLite database (created automatically)
├── templates/            # HTML templates
│   ├── index.html        # Main page template
│   └── edit.html         # Edit task template
└── static/               # Static files
    └── css/
        └── style.css     # Application styles
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation & Setup

1. **Navigate to the project directory:**
   ```bash
   cd d:\DevOpsLab\todo-app
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv todo_env
   ```

3. **Activate the virtual environment:**
   - On Windows (PowerShell):
     ```powershell
     .\todo_env\Scripts\Activate.ps1
     ```
   - On Windows (Command Prompt):
     ```cmd
     todo_env\Scripts\activate.bat
     ```

4. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask development server:**
   ```bash
   python app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://localhost:5000
   ```

3. **The application will automatically create the SQLite database on first run.**

## Usage

### Adding Tasks
1. Enter a task title in the "Task title" field (required)
2. Optionally, add a description in the "Task description" field
3. Click "Add Task" to save the task

### Managing Tasks
- **Complete Task**: Click the green checkmark button to mark a task as completed
- **Uncomplete Task**: Click the orange undo button to mark a completed task as not completed
- **Edit Task**: Click the blue edit button to modify the task title and description
- **Delete Task**: Click the red trash button to permanently delete a task (requires confirmation)

### Task Status
- **Pending**: Orange clock icon indicates the task is not yet completed
- **Completed**: Green check icon indicates the task is finished (with strikethrough text)

## Database Schema

The application uses SQLite with the following table structure:

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Configuration

### Secret Key
For production deployment, change the secret key in `app.py`:
```python
app.secret_key = 'your-secure-secret-key-here'
```

### Database Location
The SQLite database file (`todo.db`) is created in the same directory as `app.py`. To change the location, modify the `DATABASE` variable in `app.py`.

### Server Configuration
By default, the application runs on:
- Host: `0.0.0.0` (accessible from other devices on the network)
- Port: `5000`
- Debug mode: `True` (disable for production)

## Development

### File Structure Explanation

- **`app.py`**: Main Flask application with all routes and database logic
- **`templates/index.html`**: Main page displaying all tasks and add task form
- **`templates/edit.html`**: Edit task page with form for updating task details
- **`static/css/style.css`**: All styling including responsive design and animations
- **`requirements.txt`**: Python package dependencies

### Key Routes

- `GET /`: Display all tasks
- `POST /add`: Add a new task
- `GET /complete/<id>`: Mark task as completed
- `GET /uncomplete/<id>`: Mark task as not completed
- `GET /delete/<id>`: Delete a task
- `GET /edit/<id>`: Show edit form for a task
- `POST /update/<id>`: Update a task

## Customization

### Styling
Modify `static/css/style.css` to change the appearance:
- Colors and gradients
- Fonts and typography
- Layout and spacing
- Responsive breakpoints

### Features
Extend functionality by adding:
- Task categories or tags
- Due dates and reminders
- Task priority levels
- User authentication
- Task sharing

## Troubleshooting

### Common Issues

1. **Port already in use**
   - Change the port in `app.py`: `app.run(port=5001)`

2. **Database permission errors**
   - Ensure the application directory has write permissions

3. **Module not found errors**
   - Ensure virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

4. **Static files not loading**
   - Check that the `static/css/style.css` file exists
   - Verify Flask static file configuration

## Production Deployment

For production deployment:

1. Set `debug=False` in `app.py`
2. Use a secure secret key
3. Configure a production WSGI server (e.g., Gunicorn, uWSGI)
4. Consider using PostgreSQL or MySQL instead of SQLite
5. Implement proper error handling and logging
6. Set up HTTPS and security headers

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for any improvements.