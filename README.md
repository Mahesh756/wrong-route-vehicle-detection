**Project Title:** **Wrong-Way Detection System for Traffic Monitoring**

**Overview:**

This Python-based system is designed to monitor and detect vehicles traveling in the wrong direction on roads. 
The system employs computer vision techniques for real-time analysis of traffic flow. When a vehicle is identified moving against the designated direction,
an alarm is triggered to alert authorities. Additionally, the system captures the vehicle's license plate number for further action.

**Key Features:**

Real-time Video Analysis: Utilizes computer vision libraries to analyze live video feeds from traffic cameras.
Wrong-Way Detection: Implements algorithms to identify vehicles moving in the wrong direction based on their trajectories.
Alarm Generation: Triggers an alarm or notification when a wrong-way movement is detected, alerting authorities in real-time.
License Plate Recognition: Captures license plate numbers of vehicles in violation for subsequent actions.
Fine Notification: Integrates with a messaging system to send fine notifications to the owners of the identified vehicles.

**How to Use:**

1. **Clone the Repository:**
   
git clone [https://github.com/your-username/traffic-wrong-way-detection.git](https://github.com/Mahesh756/wrong-route-vehicle-detection.git)

2. **Install Dependencies:**
   
pip install -r requirements.txt

3. **Configure Settings:**

Set up camera sources, alarm preferences, and messaging API credentials in the configuration file.

4. **Run the Application:**
   
python mypro.py
