# Groissant-bot

Enhance your GitHub experience with Groissant-bot, an AI-powered assistant. It offers quick Q&A support, efficient code reviews, and streamlined project management, all integrated seamlessly into your GitHub workflow.

## Get Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

* Python <= 3.11

### Installation

Follow these steps to install the project:

```bash
# Clone the repository:
git clone git@github.com:Groissant/Groissant-bot.git

# Navigate to the project directory:
cd Groissant-bot

# Install the required packages:
pip install -r requirements.txt
```

To run the application, execute:

development

``` bash
python run.py
```

product

``` bash
gunicorn -w 4 -b :8000 app:app
```

Testing

``` bash

python test_app.py
```

## Contributing

Feel free to pick up any [issue](https://github.com/Groissant/Groissant-bot/issues?q=is%3Aissue+is%3Aopen) and create a pull request.

## License

This project is licensed under the [Your License Name] License - see the [LICENSE](./LICENSE) file for details.

## Code of Conduct

To ensure a welcoming and inclusive environment for all our contributors and participants, we adhere to a Code of Conduct. Please read [our Code of Conduct](./CODE_OF_CONDUCT.md) before participating in the project.
