# MediHelper



## Introduction
In today's fast-paced world, access to reliable health information can be a challenge. MediHelper aims to bridge this gap by offering two primary functionalities:

- **AI-Based Disease Detector**: Users can upload images related to skin conditions, and the AI model will analyze these images to identify potential diseases such as vitiligo, Stevens-Johnson syndrome (SJS), acne, hyperpigmentation, and nail psoriasis. This tool serves as a preliminary diagnostic aid, providing users with insights about their conditions.

- **AI Health Cost Calculator**: This feature allows users to input various parameters affecting their health costs. The calculator uses a linear regression model to predict potential increases or decreases in overall health expenses, helping users make informed financial decisions regarding their healthcare.

Additionally, the homepage provides essential information about common skin diseases and factors influencing health costs, ensuring users are well-informed.

The website is currently under development, with plans to add a medicine reader and other features in the future.

## Technologies Used
### Programming Languages

- **Python**: A versatile, high-level programming language known for its readability and wide-ranging applications in web development, data science, and automation.

- **HTML**: The standard markup language for creating web pages, structuring content with elements like headings, paragraphs, and links.

- **CSS**: A stylesheet language that controls the visual presentation of HTML documents, allowing for layout, colors, and responsive designs.

### Frameworks

- **Django**: A high-level Python web framework that simplifies web development with built-in features like an ORM and authentication, promoting rapid application creation.

### Machine Learning Libraries

- **TensorFlow**: An open-source library for machine learning developed by Google, enabling the creation of deep learning models for tasks like image recognition and NLP.

- **Pandas**: A data manipulation library in Python that provides DataFrames for efficient data analysis and cleaning, essential for data science tasks.

### Models

- **Image Classifier (for disease detection)**: A machine learning model that analyzes medical images to identify diseases by learning from labeled datasets.

- **Linear Regression (for health cost predictions)**: A statistical model that predicts healthcare costs based on independent variables, helping forecast future expenditures.

## Dataset Description
The datasets used for training the AI models were sourced from two reputable websites. These datasets include a variety of images depicting different skin conditions and relevant health cost parameters. Access the datasets here:
- [Detect Disease dataset](https://data.mendeley.com/datasets/3hckgznc67/1) 
- [Health Cost Calculator Dataset](https://www.synthesized.io/data-template-pages/medical-cost-personal-dataset)


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

## Future Modifications
- **Medicine Scanner**: A feature that allows users to scan medication labels for information.
- **User Authentication**: Implementing user accounts for personalized experiences.
- **Mobile Responsiveness**: Ensuring the website is fully functional on mobile devices.
- **Expanded Disease Database**: Adding more diseases and conditions for detection.
- **Chat bot**: Allowing users to interact as well as provide feedback on predictions for continuous improvement.

## Conclusion
MediHelper is poised to become a valuable resource for individuals seeking assistance with skin-related health issues and managing healthcare costs. By leveraging AI technologies, it aims to provide accurate predictions and valuable insights, ultimately enhancing user experience and promoting better health management.


