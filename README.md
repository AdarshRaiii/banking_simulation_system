# Banking Simulation System

A comprehensive banking simulation system built with Python, featuring a web interface, command-line interface, and robust transaction processing with ledger integrity verification.

## Features

- **Account Management**: Support for Savings and Current accounts
- **Transaction Processing**: Deposits, withdrawals, and transfers between accounts
- **Ledger System**: Immutable transaction ledger with integrity verification
- **Web Interface**: Flask-based web application with customer and admin views
- **CLI Interface**: Command-line interface for basic operations
- **In-Memory Storage**: Fast, persistent in-memory repository for development
- **Comprehensive Testing**: Pytest-based test suite

## Project Structure

```
banking_simulation/
├── banking/
│   ├── web_app.py          # Flask web application
│   ├── cli/
│   │   └── main.py         # Command-line interface
│   ├── models/
│   │   ├── __init__.py
│   │   ├── account.py      # Account and AccountType models
│   │   ├── ledger.py       # Transaction ledger
│   │   └── transaction.py  # Transaction model
│   ├── repository/
│   │   └── in_memory_repo.py # In-memory data storage
│   ├── services/
│   │   ├── __init__.py
│   │   └── transaction_service.py # Business logic layer
│   └── templates/
│       ├── index.html      # Landing page
│       ├── customer.html   # Customer interface
│       └── admin.html      # Admin interface
├── tests/
│   └── test_happy_path.py  # Test suite
├── requirements.txt        # Python dependencies
├── pytest.ini             # Pytest configuration
└── README.md              # This file
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd banking_simulation
```

2. Create a virtual environment:
```bash
python -m venv myenv
myenv\Scripts\activate  # On Windows
# or
source myenv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Application

Run the Flask web application:

```bash
python banking/web_app.py
```

Open your browser and navigate to `http://localhost:5000`

The web app provides:
- Landing page with navigation
- Customer interface for account operations
- Admin interface for system overview

### Command-Line Interface

Run the CLI application:

```bash
python banking/cli/main.py
```

The CLI allows basic deposit operations on a test account.

### Running Tests

Execute the test suite:

```bash
pytest
```

## Architecture

### Models
- **Account**: Represents bank accounts with ID, type, and balance
- **Transaction**: Records individual financial transactions
- **Ledger**: Immutable record of all transactions for integrity verification

### Repository Layer
- **InMemoryRepository**: Provides data persistence using in-memory storage

### Service Layer
- **TransactionService**: Handles business logic for deposits, withdrawals, and transfers

### Presentation Layer
- **Web App**: Flask application with HTML templates
- **CLI**: Simple command-line interface for basic operations

## Key Concepts

- **Minor Units**: All monetary values are stored in cents (minor units) to avoid floating-point precision issues
- **Ledger Integrity**: The system maintains a transaction ledger that can verify the integrity of all operations
- **Account Types**: Supports both Savings and Current account types

## Development

### Adding New Features

1. Define new models in the `models/` directory
2. Implement business logic in the `services/` directory
3. Add data access methods to the repository layer
4. Create web routes in `web_app.py` or CLI commands in `cli/main.py`
5. Add corresponding HTML templates if needed
6. Write comprehensive tests in the `tests/` directory

### Code Style

- Follow PEP 8 Python style guidelines
- Use type hints where appropriate
- Write docstrings for all public methods
- Maintain separation of concerns across layers

## Dependencies

- **Flask 3.0.0**: Web framework for the web interface
- **Click 8.1.7**: Command-line interface framework
- **Pytest 8.3.3**: Testing framework

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
