# AI-Powered Traffic Monitoring System

An intelligent license plate recognition system that leverages YOLOv8 and computer vision technologies to monitor traffic in real-time, automatically detecting and analyzing vehicle license plates while cross-referencing them with a comprehensive database to identify flagged records.

📢 [See the sample video: ](https://www.linkedin.com/feed/update/urn:li:activity:7348594602439815168/)


## Features

- **Real-time License Plate Detection**: Uses YOLOv8 pre-trained model for accurate vehicle detection  
- **OCR Text Extraction**: Integrates EasyOCR for precise license plate text recognition  
- **Database Integration**: PostgreSQL database with SQLAlchemy ORM for efficient data management  
- **Instant Background Verification**: Real-time checks for:
  - Outstanding traffic fines and penalties
  - Active criminal charges or warrants
  - Historical criminal records and violations  
- **Dynamic Visual Alerts**: Color-coded detection boxes for immediate threat assessment  
- **CPU-Optimized**: Runs efficiently on standard hardware without GPU requirements  

## Technology Stack

### Core Technologies

- **Python 3.x** - Primary programming language  
- **YOLOv8** - Object detection model for license plate detection  
- **OpenCV** - Computer vision library for video processing  
- **EasyOCR** - Optical Character Recognition for text extraction  
- **PostgreSQL** - Database management system  
- **SQLAlchemy** - Python SQL toolkit and ORM  


## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/traffic-monitoring-system.git
cd traffic-monitoring-system
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up PostgreSQL database**
```sql
CREATE DATABASE traffic_history;
CREATE USER postgres WITH PASSWORD 'user';
GRANT ALL PRIVILEGES ON DATABASE traffic_history TO postgres;
```

5. **Configure database connection**
Update the database URL in `database.py`:
```python
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:user@localhost/traffic_history'
```

## Project Structure

```
traffic-monitoring-system/
├── main.py              # Main application entry point
├── database.py          # Database configuration and connection
├── models.py            # SQLAlchemy database models
├── extractor.py         # License plate detection and OCR logic
├── verify.py            # Database verification and flagging system
├── requirements.txt     # Project dependencies
├── best.pt              # YOLOv8 trained model (add your model file)
├── images/              # Input video files directory
└── README.md            # Project documentation
```

## System Workflow

### 1. **Video Input Processing**
- System captures real-time video feed or processes video files  
- Each frame is analyzed for vehicle detection using YOLOv8 model  

### 2. **License Plate Detection**
- YOLOv8 model identifies potential license plate regions in the frame  
- Bounding boxes are drawn around detected license plates  
- Detected regions are extracted for text processing  

### 3. **OCR Text Extraction**
- EasyOCR processes the extracted license plate regions  
- Converts visual text into machine-readable strings  
- Applies confidence thresholding to ensure accuracy  
- Cleans and standardizes the extracted text  

### 4. **Database Verification**
- Performs real-time database queries using the extracted plate numbers  
- Searches the `citizen_traffic_history` table for matching records  
- Retrieves comprehensive vehicle and owner information  

### 5. **Risk Assessment**
- Analyzes retrieved data for flagged conditions:
  - **Pending Fines**
  - **Active Charges**
  - **Criminal History**  
- Categorizes vehicles as safe, flagged, or unknown  

### 6. **Visual Alert System**
- **Green Box**: Safe vehicles with clean records  
- **Red Box**: Flagged vehicles with violations/charges  
- **Purple Box**: Fetching the latest result from the database  
- Displays relevant information overlay on video feed  

### 7. **Output Generation**
- Processed video with annotations is saved to output file  
- Real-time display shows live monitoring results  
- System logs detection events for audit purposes  
