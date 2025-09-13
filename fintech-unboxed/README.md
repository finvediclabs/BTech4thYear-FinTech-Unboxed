# FinTech Unboxed: Create a Personal Finance Manager

## Overview
FinTech Unboxed is a personal finance manager application that helps users track their income, expenses, and financial goals. The application provides visual analytics to help users understand their financial situation better. It is built using a full-stack approach with a Flask backend and a MongoDB database, along with a user-friendly frontend.

## Project Structure
```
fintech-unboxed
├── backend
│   ├── app.py
│   ├── models
│   │   └── finance.py
│   ├── routes
│   │   └── api.py
│   └── requirements.txt
├── frontend
│   ├── static
│   │   └── style.css
│   ├── templates
│   │   └── index.html
│   └── app.py
├── config
│   └── settings.py
├── README.md
```

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fintech-unboxed
   ```

2. **Set up the backend:**
   - Navigate to the `backend` directory.
   - Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Ensure you have MongoDB installed and running.
   - Update the database connection settings in `config/settings.py`.
   - Run the backend application:
     ```
     python app.py
     ```

3. **Set up the frontend:**
   - Navigate to the `frontend` directory.
   - Run the frontend application:
     ```
     python app.py
     ```

4. **Access the application:**
   Open your web browser and go to `http://localhost:5000` to access the personal finance manager.

## Resolving Common Bugs

### Troubleshooting Database Connections
- Ensure that MongoDB is running and accessible.
- Check the connection string in `config/settings.py` for accuracy.
- Verify that the MongoDB service is not blocked by a firewall.

### Fixing Routing Issues
- Ensure that the routes defined in `backend/routes/api.py` are correctly set up.
- Check for typos in the route paths in both the frontend and backend applications.
- Use debugging tools to trace the requests and responses.

### Handling Dependency Conflicts
- Ensure that all required packages are listed in `backend/requirements.txt`.
- If you encounter version conflicts, consider creating a virtual environment and installing dependencies there:
  ```
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  pip install -r requirements.txt
  ```

## Conclusion
FinTech Unboxed aims to empower users to take control of their finances through effective tracking and visualization. If you encounter any issues not covered in this README, please refer to the documentation of the respective libraries or seek help from the community.