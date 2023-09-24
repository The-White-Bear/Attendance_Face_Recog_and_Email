# Face Recognition and Automatic Email Sending


## Introduction

This is a project that utilizes face recognition technology to mark attendance and send automatic emails when a recognized face is detected. This project can be applied in various scenarios, from time management in the workplace to door access security.

## Key Features

- Face recognition: The system uses a facial recognition model to identify the user's identity.

- Automatic attendance: When a face is successfully recognized, the system will automatically mark the user as present.

- Auto notification email: After successfully attending, the system will send an email to notify attendees who have been absent for more than 2 attendance sessions.

## Usage Guide

1. **Setup Environment:**
   - Ensure you have Python and the required libraries installed by using `requirements.txt`.
   - Open CMD and run : pip install -r requirements.txt
   -If you have trouble when install dlib, make sure that you installed Cmake and C++. I recommend you to use Visual Studio to install C++ compiler.

2. **Configuration Setup:**
   - Configure the configuration file (`config.yml`) with necessary information such as email settings and facial recognition model configuration.

3. **Run the Application:**
   - Use the following command to run the application:
     ```
     python main.py
     ```

4. **Monitor Results:**
   - The application will display results in real-time and send automatic emails when a face is detected.

## Contribution

We welcome contributions from the community. If you'd like to contribute to this project, please create a pull request and describe the changes you propose in detail.

## License

This project is distributed under the [MIT License](LICENSE).

---
**Note:** Please make sure to adhere to privacy and security rules when using this project. Do not use it for personal privacy infringements or illegal activities.
