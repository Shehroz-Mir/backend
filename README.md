# Product Management Application

A full-stack web application for managing product inventory. Built with **FastAPI** (backend) and **React** (frontend), this project demonstrates modern web development practices with API integration, state management, and responsive UI.

## 📋 Project Structure

```
.
├── main.py              # FastAPI backend server
├── models.py            # Pydantic models for data validation
├── __pycache__/         # Python cache files
├── frontend/            # React frontend application
│   ├── package.json     # Frontend dependencies
│   ├── public/          # Static files
│   └── src/             # React source code
└── README.md            # This file
```

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Pydantic** - Data validation using Python type hints
- **Python 3.x**

### Frontend
- **React 18** - UI library
- **Axios** - HTTP client for API calls
- **React Scripts** - Build and development tools

## 📦 Features

### Backend (main.py)
- **GET /** - Welcome endpoint
- **GET /products** - Retrieve all products
- **GET /product/{id}** - Retrieve specific product by ID
- **POST /product** - Add a new product
- **PUT /product** - Update existing product
- **DELETE /product** - Delete a product by ID

### Frontend (React)
- **Product List View** - Display all products with details
- **Search & Filter** - Filter products by ID, name, or description
- **Sorting** - Sort products by any field (ascending/descending)
- **Add Product** - Form to create new products
- **Edit Product** - Inline editing capabilities
- **Delete Product** - Remove products from inventory
- **Loading States** - Visual feedback during API calls
- **Error/Success Messages** - Auto-dismissing notifications (5 seconds)

## 📊 Data Model

```python
Product:
  - id: int
  - name: str
  - description: str
  - price: float
  - quantity: int
```

### Sample Data
The application includes 4 pre-loaded products:
1. Laptop (ID: 1) - $1500.00 - Qty: 10
2. Smartphone (ID: 2) - $800.00 - Qty: 5
3. Headphones (ID: 3) - $200.00 - Qty: 15
4. Monitor (ID: 4) - $400.00 - Qty: 7

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+ and npm
- Pip (Python package manager)

### Backend Setup

1. Install FastAPI and Uvicorn:
```bash
pip install fastapi uvicorn
```

2. Run the backend server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The application will open at `http://localhost:3000`

> **Note:** The frontend is configured with a proxy to `http://localhost:8000` for API calls (see `package.json`)

## 📝 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/products` | Get all products |
| GET | `/product/{id}` | Get product by ID |
| POST | `/product` | Create new product |
| PUT | `/product?id={id}` | Update product |
| DELETE | `/product?id={id}` | Delete product |

### Example Requests

**Get all products:**
```bash
curl http://localhost:8000/products
```

**Get specific product:**
```bash
curl http://localhost:8000/product/1
```

**Add new product:**
```bash
curl -X POST http://localhost:8000/product \
  -H "Content-Type: application/json" \
  -d '{"id":5,"name":"Tablet","description":"10-inch tablet","price":600.0,"quantity":3}'
```

## 🎓 Learning Outcomes

This project demonstrates:
- Building RESTful APIs with FastAPI
- Data validation with Pydantic
- React hooks (useState, useEffect, useMemo)
- Component-based architecture
- HTTP requests with Axios
- State management and filtering/sorting logic
- Full-stack integration with CORS support

## 📚 References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Axios Documentation](https://axios-http.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

## 📄 License

This project is for educational purposes as part of the Telusko FastAPI course on YouTube.
