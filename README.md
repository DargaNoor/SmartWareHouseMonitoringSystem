# SmartWareHouseMonitoringSystem

The **Smart Warehouse Management System** is a final year project undertaken by a team of four members, guided by an assigned mentor. The project aims to address and mitigate common challenges faced in the warehousing industry while leveraging modern technology trends to optimize warehouse operations. This project is subject to weekly reviews with continuous feedback from the guide and bi-monthly comprehensive assessments involving both the guide and the project head.


**Project Objectives:**
1. Improve warehouse management efficiency.
2. Address problems such as empty rack detection, object motion sensing, and pest control.
3. Assist local warehouses in streamlining their operations.
4. Implement an alert system for critical conditions.

**Functional Requirements:**\
**Alert Notification System:** Notify users/system when values exceed predefined limits through email using microcontrollers or embedded systems.\
Gas and Temperature Detection: Utilize gas sensors for detecting LPG, iso-butane, propane, and other gases, while also incorporating temperature sensors for monitoring environmental conditions.\
**Radio Frequency Identification (RFID):** Employ RFID technology for tracking inventory by using tags and readers.\
**QR Code:** Unique QR code is generated for Small Scale industrial products to maintain and keep track of them.


**Hardware Requirements:**\
**Arduino IDE:** Employ Arduino Uno microcontroller boards for data processing and control.\
**Gas Sensor (MQ-6):** Use MQ-6 sensors to detect LPG and other gases within the warehouse environment.\
**Temperature Sensor (DHT11):** Implement DHT11 temperature and humidity sensors for monitoring temperature conditions.\
**Load Cell (5kg):** Integrate 5kg load cells for weighing purposes.\
**HX711:** Use the HX711 precision analog-to-digital converter for accurate weight measurements.\
**LCD Display (16x2):** Employ LCD displays for visualizing data.\
**EM-18 Reader Module:** Utilize EM-18 RFID reader modules for RFID tag scanning.



**Software Requirements:**\
**Embedded C:** Develop code in Embedded C to control and manage the hardware components effectively.\
**OS-Windows:** Utilize an operating system (OS) like Windows to provide a user-friendly interface and support for software development.\
**Arduino 1.8.12:** Utilize the Arduino Uno version 1.8.12 Integrated Development Environment (IDE) for coding and programming the microcontrollers.\
**Python Flask:** Implement Flask, a Python web application framework, for web-based interactions and data visualization.
**Inventory Tracking Technology:**
1. Implement Radio Frequency Identification (RFID) for real-time inventory tracking.
2. Use QR codes for small-scale industries to uniquely identify products.


**Benefits of this System developed:**
1. Optimize warehousing operations, ensuring safe storage and reducing economic losses.
2. Improve inventory management, order processing, layout, labor management, shipping, logistics, reporting, analytics, and returns management.
3. By presenting the project in a more concise manner, it becomes easier to understand the main objectives, requirements, hardware, software, and benefits of the Smart Warehouse Management System.

**Results:**\
\
**Home Page Of Web application:**\
![image](https://github.com/DargaNoor/SmartWareHouseMonitoringSystem/assets/90261006/2db00d5d-fd43-4395-ab28-d1dbfc23f2fe)\
This page is the basic index page for the application and to user(trained) who is viewing.\
\
\
**Adding Product Form Page:**\
![image](https://github.com/DargaNoor/SmartWareHouseMonitoringSystem/assets/90261006/6c309b09-f431-4dfa-8239-c2483e46670a)\
For adding a product either through RFID or generating QR Code, which will depend on the Quantity and relationship of product with the organization.\
\
\
**Initial Reading:**\
![image](https://github.com/DargaNoor/SmartWareHouseMonitoringSystem/assets/90261006/9335fb84-0df4-44f0-9266-c1db0509ed2a)\
The basic details of products entered till now will be displayed here.\
\
\
**QR Code:**\
![image](https://github.com/DargaNoor/SmartWareHouseMonitoringSystem/assets/90261006/3bf03edf-492f-4404-bcbf-694c173df33b)\
An Image of QR code will be displayed here where onclick can see the details of that specifc product.\
\
\
**Values from Sensors:**\
![image](https://github.com/DargaNoor/SmartWareHouseMonitoringSystem/assets/90261006/312ad8f2-c3f7-42a6-ab0b-2f5e6d7f7728)\
The values which are displayed on screen via server(Python Flask) reading and getting required values from sensors.\
\
\
**Contact Form:**\
![image](https://github.com/DargaNoor/SmartWareHouseMonitoringSystem/assets/90261006/a55aed53-5c93-4a65-bff1-a2905ced94f2)\
This is form where any issues regarding the management or any technical issues will be sent to the admin via mail.\
\
\
**Hardware Implementation:**\
![image](https://github.com/DargaNoor/SmartWareHouseMonitoringSystem/assets/90261006/db8bf20b-b9bd-4f13-a77a-22dbeb521b99)\
The above image represents the hardware part implementatin where all sensors,Arduino Uno and a lot of IoT is being used.\
\
\
**Rat Detected Through Camera:**\
![image](https://github.com/DargaNoor/SmartWareHouseMonitoringSystem/assets/90261006/1e834dbb-4f23-442a-920f-05e3604fe8a3)\
The part of rat being detected is being highlighted through red border which can be seen in above image.\
\
\
**Detection of Rat notification via Telegram:**\
![image](https://github.com/DargaNoor/SmartWareHouseMonitoringSystem/assets/90261006/2974e43d-86bd-4643-af0d-096c7f3fcfb4)\
\
\
**Rat detected Time and Size Measurements:**\
![image](https://github.com/DargaNoor/SmartWareHouseMonitoringSystem/assets/90261006/aa91296a-1465-43ed-a555-e5cb53333471)\
The Rat detected size measurements and how much time it got detected is being shown in screen.

