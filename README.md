# MediHelper



## Introduction
In today's fast-paced world, access to reliable health information can be a challenge. MediHelper aims to bridge this gap by offering two primary functionalities:

- **AI-Based Disease Detector**: Users can upload images related to skin conditions, and the AI model will analyze these images to identify potential diseases such as vitiligo, Stevens-Johnson syndrome (SJS), acne, hyperpigmentation, and nail psoriasis. This tool serves as a preliminary diagnostic aid, providing users with insights about their conditions.

- **AI Health Cost Calculator**: This feature allows users to input various parameters affecting their health costs. The calculator uses a linear regression model to predict potential increases or decreases in overall health expenses, helping users make informed financial decisions regarding their healthcare.

Additionally, the homepage provides essential information about common skin diseases and factors influencing health costs, ensuring users are well-informed.

The website is currently under development, with plans to add a medicine reader and other features in the future.

## Technologies Used
- **Programming Languages**: Python, HTML, CSS
- **Frameworks**: Django
- **Machine Learning Libraries**: TensorFlow, Pandas
- **Models**:
  - Image Classifier (for disease detection)
  - Linear Regression (for health cost predictions)

## Dataset Description
The datasets used for training the AI models were sourced from two reputable websites. These datasets include a variety of images depicting different skin conditions and relevant health cost parameters. Access the datasets here:
- [Detect Disease dataset](https://data.mendeley.com/datasets/3hckgznc67/1)
- [Health Cost Calculator Dataset](https://www.synthesized.io/data-template-pages/medical-cost-personal-dataset)

## Future Modifications and Features
- **Medicine Reader**: A feature that allows users to scan medication labels for information.
- **User Authentication**: Implementing user accounts for personalized experiences.
- **Mobile Responsiveness**: Ensuring the website is fully functional on mobile devices.
- **Expanded Disease Database**: Adding more diseases and conditions for detection.
- **User Feedback System**: Allowing users to provide feedback on predictions for continuous improvement.

## How It Works

![Image](https://github.com/user-attachments/assets/86484bae-c316-4486-a491-45361504d791)


![Image](https://github.com/user-attachments/assets/fb758c8e-4d01-4bbb-aee4-7263d873c521)



## Project Setup
To set up MediHelper locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MediHelper.git
   ```

2. Navigate into the project directory:
   ```bash
   cd Health_website
   cd image_process
   cd Cost_calculator
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Django server:
   ```bash
   python manage.py runserver
   ```

5. Open your web browser and visit `http://localhost:8000/` to view the application.

## Conclusion
MediHelper is poised to become a valuable resource for individuals seeking assistance with skin-related health issues and managing healthcare costs. By leveraging AI technologies, it aims to provide accurate predictions and valuable insights, ultimately enhancing user experience and promoting better health management.


