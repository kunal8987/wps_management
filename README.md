# SKU and MSKU Management System

## Overview

This project is a SKU (Stock Keeping Unit) and MSKU (Master SKU) management system built using Django, a high-level Python web framework. The application allows users to create, manage, and associate SKUs with MSKUs, providing a structured way to handle product inventory.

### Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (default) or PostgreSQL
- **Frontend**: Django Admin Interface
- **API Testing**: Postman
- **Version Control**: Git

## Logic

The application consists of two main models:

1. **SKU**: Represents individual products with attributes such as `sku_code`, `name`, and `description`.
2. **MSKU**: Represents a collection of SKUs, allowing for bulk management of related products. It includes attributes like `msku_code` and `name`, and has a many-to-many relationship with the SKU model.

The application provides an admin interface for easy management of SKUs and MSKUs, as well as RESTful API endpoints for programmatic access.

## AI Tools Used

- **Blackbox.AI**: Assisted in generating code snippets, model definitions, and admin configurations.
- **Postman**: Used for testing API endpoints and ensuring the functionality of the application.

## How to Use the Solution

1. **Access the Admin Interface**: 
   - Navigate to `http://127.0.0.1:8000/admin/` after running the server.
   - Log in with the admin credentials you set up.

2. **Create SKUs**: 
   - Use the SKU model in the admin interface to create new SKUs by providing the `sku_code`, `name`, and optional `description`.

3. **Create MSKUs**: 
   - Use the MSKU model to create new MSKUs and associate them with existing SKUs.

4. **API Access**: 
   - Use Postman to send requests to the API endpoints for creating and managing SKUs and MSKUs.

## How to Set It Up

### Prerequisites

- Python 3.x
- Django
- PostgreSQL (optional, if you want to use it instead of SQLite)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/sku-msku-management.git
   cd sku-msku-management