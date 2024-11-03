# Quantitative Trading Assistant 📈

A Streamlit-based AI assistant that helps users understand quantitative trading concepts, strategies, and market analysis. The assistant leverages advanced language models and real-time market data to provide expert guidance on trading principles and methodologies.

## Features

- 🤖 AI-powered trading expertise and mentorship
- 🔍 Real-time market research capabilities
- 📚 Clear explanations of complex trading concepts
- 💡 Practical examples and case studies
- ⚠️ Risk management guidance
- 🗄️ Persistent chat history using PostgreSQL
- 🔄 Integration with latest market trends

## Prerequisites

- Python 3.8+
- PostgreSQL database
- API keys for:
  - Groq
  - Tavily

## Installation

1. Clone the repository:
```bash
git clone https://github.com/haqqibrahim/quantitative-trading-assistant.git
cd quantitative-trading-assistant
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
```
Then edit `.env` with your API keys and database credentials:
```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

## Configuration

The application can be configured through the following environment variables:

- `GROQ_API_KEY`: Your Groq API key for AI capabilities
- `TAVILY_API_KEY`: Your Tavily API key for market research
- `DATABASE_URL`: PostgreSQL connection string
- `MODEL_NAME`: LLM model to use (default: "mixtral-8x7b-32768")
- `DEBUG`: Enable debug mode (true/false)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Groq for providing the LLM capabilities
- Thanks to Tavily for market research API
- All contributors and users of this project

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.