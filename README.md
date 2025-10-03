# Smart Health Assistant

## Overview
The Smart Health Assistant is a web-based intelligent health advisory system designed to deliver personalized healthcare recommendations to users. Leveraging AI and user-provided information, it offers tailored health plans, symptom analysis, and preventive alerts. Unlike traditional static health apps, this platform dynamically interacts with users through a conversational chatbot, making healthcare advice more responsive, personalized, and accessible.

### Chapter 1: Introduction
#### 1.1 Background
The rapid advancement of information technology has significantly transformed the healthcare sector. Mobile health (mHealth) applications are increasingly utilized for disease prevention, health monitoring, and personalized healthcare delivery (World Health Organization, 2021). In today's digital society, users demand easily accessible, personalized, and preventive healthcare services without the constraints of location or time.

#### 1.2 Aim
The primary aim of this project is to design and develop a Smart Health Assistant: a mobile/web-based personalized health advisory system that leverages AI and user-provided information to generate tailored health recommendations, symptom analyses, and preventive alerts.

#### 1.3 Scope
The Smart Health Assistant application will offer the following functionalities:
- User registration and guest mode access.
- Personalized health screenings, exercise plans, vitamin suggestions, and meal planning based on user demographics (age, gender).
- Symptom checker chatbot using AI (OpenAI GPT model) to suggest diagnostic tests and preliminary evaluations.
- Push notifications and email reminders for regular health monitoring activities.
- Secure storage of user health profiles, chatbot interactions, and recommendation histories.

The app will initially target general preventive healthcare for adults categorized into age groups (20-30, 30-40, 40-50, 50-60, and 60+ years).

#### 1.4 Significance
The Smart Health Assistant will contribute significantly to public health by empowering individuals to take charge of their own health through accessible, personalized guidance.

## System Architecture
### Chapter 2: Proposed System
#### 2.1 Overview of the Proposed System
The Smart Health Assistant is envisioned as a mobile and web-based intelligent health advisory platform that delivers personalized healthcare recommendations to users. Unlike traditional static health apps, the Smart Health Assistant dynamically interacts with users through a conversational chatbot, making healthcare advice more responsive, personalized, and accessible.

#### 2.2 System Architecture
The proposed system architecture consists of the following major components:

| Component            | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| Frontend (Mobile/Web App) | Built using Streamlit for web and Flutter (optional) for mobile, the frontend captures user input and displays personalized recommendations. |
| Backend Server        | Python-based server handling data processing, user authentication, and communication with AI services. |
| AI Chatbot Engine     | Integrated via OpenAI’s GPT API to process natural language symptom descriptions and generate diagnostic suggestions. |
| Database (SQLite)     | Stores user profiles, health history, chatbot interactions, and recommendation logs securely. |
| Notification System   | Push notifications and email alerts about health checkups, preventive tests, and reminders. |
| Cloud Hosting Platform | AWS, Google Cloud, or Heroku to deploy the backend API and manage storage scalability. |



#### 2.3 Key Functional Modules
- **2.3.1 User Registration and Profile Management**
  - Users can register with personal details (age, gender, basic health history).
  - Guest mode allows temporary access without data storage.
- **2.3.2 Personalized Health Plan Generator**
  - Health recommendations are based on user's age group and gender.
  - The system suggests screenings, supplements, exercise, and meal plans.
- **2.3.3 Push Notifications and Email Reminders**
  - Regular alerts about vaccinations, screenings, or checkups.
  - Customizable notification settings based on user preference.

#### 2.4 User Interaction Flow
The general workflow for a user includes:
1. Registration/Login (or guest mode access).
2. Profile Creation (enter age, gender, health info).
3. Receive Initial Health Recommendations.
4. Submit Symptoms through Chatbot for dynamic diagnostic advice.
5. Receive Notifications and Updates.
6. Review/Save/Share Health Reports.



## Technologies and Resources
### Chapter 3: Technologies and Resources
#### 3.1 Technologies
The development of the Smart Health Assistant relies on modern, scalable, and widely accepted technologies. The selected tools and platforms ensure high performance, scalability, and ease of future upgrades.
- Python (Backend Development)
- Streamlit (Web Interface Development)
- OpenAI GPT API (Chatbot AI Engine)
- SQLite (Database Management)
- Firebase Cloud Messaging (Push Notifications)
- Cloud Hosting (AWS/Google Cloud/Heroku)

#### 3.2 Hardware Requirements
| Component   | Specification                          |
|-------------|----------------------------------------|
| Server      | AWS EC2 t2.medium (4 vCPU, 8GB RAM) or equivalent |
| Client Device | Any smartphone (Android/iOS), Tablet, or PC with internet connectivity |

#### 3.3 Software Requirements
| Software         | Version/Requirement |
|-------------------|---------------------|
| Python            | 3.10+              |
| Flask/FastAPI     | Latest             |
| Streamlit         | Latest             |
| SQLite            | Latest stable      |
| OpenAI Python SDK | Latest             |
| Firebase Cloud Messaging SDK | Latest |
| Git               | Version control system |

## System Architecture Details
### Chapter 4: System Architecture
#### 4.1 Overview of System Architecture & Components
The architecture of the Smart Health Assistant follows a modular and layered approach to ensure scalability, maintainability, and security.

| Component          | Role                                                                 |
|--------------------|----------------------------------------------------------------------|
| User Interface (UI)| Captures user inputs and displays personalized health recommendations. Built using Streamlit for web apps. |
| Backend API Server | Processes client requests, interacts with the database, communicates with the AI engine, and handles authentication (Python Flask/FastAPI). |
| AI Chatbot Service | Uses OpenAI GPT API to understand user symptoms and suggest diagnostic tests. |
| Notification System | Firebase Cloud Messaging sends push alerts and reminders to users. |
| Database (SQLite)  | Stores user profiles, health records, chatbot conversations, and health plans securely. |
| Cloud Infrastructure | Hosts application components on AWS/Google Cloud for scalability and reliability. |


## Project Timeline
### Chapter 5: Project Timeline
#### 5.1 Overview
Effective time management is crucial for the successful implementation of the Smart Health Assistant project. This chapter outlines the key phases of the project lifecycle, associated activities, and estimated timelines. The project is divided into six main phases, each focusing on specific deliverables, ensuring smooth progression and timely completion.

#### 5.2 Gantt Chart
The following Gantt chart represents the proposed project schedule visually:
- **Literature Review**: May 2025
- **System Design**: June 2025
- **Backend Development**: July 2025
- **Frontend Development**: July-August 2025
- **Integration and Testing**: August 2025
- **Finalization and Documentation**: September 2025


## References
- Bass, L., Clements, P., & Kazman, R. (2012). *Software architecture in practice* (3rd ed.). Addison-Wesley Professional.
- Project Management Institute. (2017). *A guide to the project management body of knowledge (PMBOK® Guide)* (6th ed.). Project Management Institute.
- World Health Organization. (2021). *Global strategy on digital health 2020–2025*. https://www.who.int/publications/i/item/9789240020924
- Lee, J., & Yoon, W. (2021). Emerging trends in telemedicine and digital health solutions: A review. *Journal of Medical Internet Research, 23*(5), e24908. https://doi.org/10.2196/24908

## Setup Instructions
1. **Prerequisites**:
   - Install Python 3.10+ (e.g., via Homebrew: `brew install python`).
   - Install Git: `brew install git`.
   - Install dependencies: `pip install -r requirements.txt`.

2. **Clone the Repository**:
git clone https://github.com/yourusername/SmartHealthAssistant.git
cd SmartHealthAssistant


3. **Set Up Environment**:
- Create a virtual environment: `python3 -m venv env`.
- Activate it: `source env/bin/activate`.
- Install dependencies: `pip install -r requirements.txt`.

4. **Configure Environment Variables**:
- Create a `.env` file based on `.env.example` with your OpenAI API key and email settings:
OPENAI_API_KEY=your_api_key_here
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
FROM_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_app_password


5. **Run the Application**:
- Start the Streamlit app: `streamlit run app.py`.
- Access it at `http://localhost:8501`.

## Usage
- **Register/Login**: Create an account or log in to save health data.
- **Guest Mode**: Access features temporarily without registration by providing age, gender, and medical condition.
- **Health Plan**: View personalized health recommendations.
- **Symptom Checker**: Use the chatbot to analyze symptoms.
- **Notifications**: Receive email reminders (for registered users).

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Ensure you follow the project structure and update the documentation accordingly.

## License