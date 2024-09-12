# QR Image with OLED Display: Enhancing Efficiency

## Team
**Prudence Radebe (Project Lead & Developer):** Responsible for designing, developing, and implementing the QR image reader with OLED display integration. Also in charge of coordinating tasks and ensuring project completion.

## Technologies

### Libraries, Languages, and Platforms
- **Python:** Main programming language for developing the scanner application.
- **RPi.GPIO:** Library for Raspberry Pi GPIO control.
- **picamera2:** Library for accessing the Raspberry Pi camera module.
- **requests:** Library for making HTTP requests.
- **Luma:** OLED Display Library for controlling OLED displays, such as Adafruit SSD1306.

### Frameworks and Hardware
- **Raspberry Pi:** Hardware platform for running the scanner application.
- **Raspberry Pi Camera Module:** Hardware component for capturing images.
- **OLED Display:** Hardware component for showcasing printed images.

## Challenge Statement

### Problem Statement
The project aims to develop a QR image capable of efficiently capturing and analyzing QR images. Additionally, it will integrate an OLED display to showcase the printed images for easy verification.

### Risks

#### Technical Risks
- **Integration Complexity:** Integrating the OLED display with the Raspberry Pi and ensuring seamless functionality.
- **Image Recognition Accuracy:** Ensuring accurate QR image recognition under varying lighting and environmental conditions.

#### Non-Technical Risks
- **User Adoption:** Ensuring user acceptance and ease of use for users unfamiliar with the new scanning process.
- **Hardware Compatibility:** Compatibility issues between Raspberry Pi, camera module, and OLED display components.

## Infrastructure

### Branching and Merging
Utilizing GitHub Flow for collaborative development and version control.

### Deployment Strategy
Continuous integration and deployment pipeline for automated testing and deployment to Raspberry Pi devices.

### Data Population
Manual entry or CSV import for initial data population and testing purposes.

### Testing Tools and Automation
- Unit testing for code functionality and integration testing for API endpoints.
- Continuous integration with GitHub Actions for automated testing.

## Existing Solutions

### Similar Products or Solutions
- **Commercial QR Scanners:** Offer similar functionality but may lack the flexibility of integration with custom hardware components like OLED displays.
- **Desktop QR Reading Software:** Provides QR analyzing capabilities but lacks portability compared to a Raspberry Pi-based solution.

### Comparison
- **Commercial QR Scans:** Provide out-of-the-box solutions but may not meet specific requirements or integrate with custom hardware.
- **Desktop QR Scans Software:** Limited by the hardware it's installed on and lacks the versatility of a Raspberry Pi-based solution.

## Conclusion
The proposed QR image reader with OLED display integration aims to provide a versatile and customizable solution for QR image reading and verification. By leveraging Python and Raspberry Pi technology, the project offers a flexible platform adaptable to various environments and requirements.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
