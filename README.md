# Web Scraper

A simple web application to extract data from websites. Enter a URL and get the main text content using a clean interface.

## Features
- Enter a URL to scrape
- Extracts and displays main text content
- Responsive and minimal UI

## Getting Started

### Prerequisites
- Docker (recommended) or Python 3 with Flask and requests

### Using Docker
1. Build and run the container:
   ```bash
   docker-compose up --build
   ```
2. Open your browser and go to `http://localhost:8080` (or the port specified in your `docker-compose.yml`).

### Manual Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   python app.py
   ```
3. Open `http://localhost:5000` in your browser.

## File Structure
- `index.html` - Main HTML file
- `app.py` - Flask backend for scraping
- `style.css` - Stylesheet
- `Dockerfile` & `docker-compose.yml` - For containerized deployment
- `requirements.txt` - Python dependencies

## License
MIT
