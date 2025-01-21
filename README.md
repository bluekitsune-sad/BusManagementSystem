# Transport Management System

## Introduction
The Transport Management System is a web-based application designed to streamline university transport operations. It provides separate interfaces for administrators, drivers, and students to manage and access transport-related information efficiently.

## Key Features

### Admin Dashboard
- View comprehensive statistics (total students, drivers, routes, pending fees)
- Manage student and driver records
- Configure and monitor transport routes
- Track fee payment status
- Real-time seat availability monitoring

### Driver Dashboard
- Real-time seat management
- View assigned route details
- Track stop locations and timings
- Monitor student count and seat availability
- Morning and evening schedule management

### Student Dashboard
- View personal timetable
- Check assigned transport route
- Monitor fee payment status
- Access class schedules
- View route and timing information

## Installation

1. Clone the repository:

   ```bash
   git clone [repository-url]
   cd BusManagementSystem
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. In your browser, visit these URLs to set up initial data:
   - [http://localhost:5000/api/mockupload](http://localhost:5000/api/mockupload)
   - [http://localhost:5000/api/db/all](http://localhost:5000/api/db/all)

5. Access the application:
   - Open `login.html` in your browser
   - Use the following credentials:
     - Admin: `admin@iugc.edu` / `admin123`
     - Student: `john@example.com` / `student123`
     - Driver: `david@example.com` / `driver123`

## Project Structure

```
project/
├── app.py           # Backend Flask application
├── login.html       # Login page
├── adminD.html      # Admin dashboard
├── studentD.html    # Student dashboard
├── driverD.html     # Driver dashboard
└── transport.db     # SQLite database
```

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite (using dataset)
- **API**: RESTful architecture
- **UI**: Material Icons, Responsive Design

## Future Integrations

1. **Enhanced Security Features**
   - JWT authentication
   - Role-based access control
   - Password encryption
   - Session management
   - Two-factor authentication

2. **Real-time Features**
   - Live tracking of buses
   - Real-time notifications
   - GPS integration
   - Mobile app integration
   - Push notifications

3. **Advanced Analytics**
   - Route optimization
   - Attendance tracking
   - Fuel consumption monitoring
   - Cost analysis
   - Performance metrics

4. **Additional Features**
   - Payment gateway integration
   - Mobile application
   - QR code-based attendance
   - Parent portal
   - Emergency notification system
   - Weather integration
   - Maintenance scheduling
   - Automated reporting

5. **User Experience Improvements**
   - Dark mode
   - Multiple language support
   - Offline functionality
   - Customizable dashboards
   - Enhanced accessibility features

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

