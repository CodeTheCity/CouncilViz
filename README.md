# Council Viz

Council Viz is an open-source project aimed at making Aberdeen City Council data more accessible to the public through intuitive visualisations and structured information. The project was developed during the Democracy Hackathon hosted by CodeTheCity in Aberdeen, with the goal of empowering citizens to engage meaningfully with local governance.

---

## Features

- **Dynamic Data Pipeline:** Collects, processes, and serves council data from Aberdeen City Council's website.
- **User-Friendly Visualisations:** Interactive maps and structured committee data for easy navigation.
- **Category-Based Insights:** Displays information categorised by committees and topics, such as housing, finance, and education.
- **Intuitive User Interface:** Accessible interface for citizens to explore council data.

---

## Technology Stack

### Backend:
- **Node.js** with **Express.js**: Serves dynamic endpoints for council data.

### Frontend:
- **EJS Templates**: Renders dynamic web pages.
- **Leaflet.js**: Creates interactive maps.

### Data Pipeline:
- **Python**: Utilises BeautifulSoup for web scraping and JSON manipulation.
- **JSON Storage**: Structured council data in hierarchical JSON format.

---

## Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/) (v14 or higher)
- [Python](https://www.python.org/) (v3.7 or higher)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/CodeTheCity/CouncilViz.git
   cd CouncilViz
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the server:
   ```bash
   npm start
   ```

5. Access the application at [http://localhost:3000](http://localhost:3000).

---

## File Structure

### Key Files:
- **`app.js`**: Main server file for routing and backend logic.
- **`scraper.py`**: Script for scraping council data and transforming it into JSON.
- **`categories.py`**: Extracts and processes categories from council data.
- **`public/`**: Directory containing static assets and GeoJSON files for visualisations.
- **`views/`**: EJS templates for rendering dynamic pages.
- **`data/`**: Contains processed JSON files such as committees and categories.

---

## API Endpoints

### Root:
- **GET `/`**: Renders the homepage displaying categories.

### Map View:
- **GET `/map`**: Displays an interactive map of council wards using GeoJSON data.

### Committee Data:
- **GET `/:info`**: Retrieves information about specific categories.
- **GET `/:info/:committee`**: Displays detailed information about a specific committee.

---

 

---

## Future Improvements
- Implement real-time data updates from council websites.
- Add more visualisation options, such as bar and pie charts.
- Expand support for additional councils and datasets.

---

## Acknowledgements
- **CodeTheCity**: For organising the Democracy Hackathon and fostering innovation.
- **Aberdeen City Council**: For providing public data.

---

## License
This project is licensed under the [ISC License](https://opensource.org/licenses/ISC).

---

## Contact
For any inquiries, please reach out to the project maintainers via the [GitHub Issues Page](https://github.com/CodeTheCity/CouncilViz/issues).
