import spacy

nlp = spacy.load("./models2/model-best")

text = """
GOPU SAI SANDEEP
Mobile: 9866558070 
 sandeep.gopu2908@gmail.com
______________________________________________________________________________________________________________________________
Objective:
To share the vision of an organization where the career will be challenging and my knowledge and 
experience in Testing are utilized.
Professional Summary:
 Sound understanding of software development life cycle (SDLC) and involvement in Software 
Testing Life cycle (STLC).
 Having 3+ years of experience as a manual tester of IT professional experience in software 
testing
 Attended the walk-through meetings to discuss business requirements and participated in 
client meetings.
 Extensive experience in creating and managing Test Scenarios and Test Cases.
 Having knowledge on python
 Having Experience on automation testing using selenium
 Generating and managing Defect Tracking Reports using ADO Board.
 Skilled in Managing Test documents, and Defect Report.
 Experience in agile model and traditional models
 Capable in performing Smoke and Sanity testing.
 Having Experience in API Testing using Postman Tool
 Good knowledge on GITHUB
 Having knowledge on cross browser testing and mobile responsiveness using 
browserstack.com
 Highly Interactive and ability to work with cross- functional teams
 Good Team player and also have ability to work independently in a time sensitive environment
 Ability to work as a team with Business Analysts, Developers for analyzing business 
specifications
Technical Skills:
Operating Systems : Windows 
Coding : Python , Selenium,,
Other tools : Postman, ADO Board, Jira
Key-Skills : Manual Testing, API Testing 
Experience:
Company Role From To
Wancura Software Solutions
Alpha Numero Global Systems 
Pvt.Ltd
Software Test Engineer
QA Engineer
Jul 04th 2019
 Feb 20th
 2023
Feb10th2023
Mar31st2023
Education:
 Completed Graduation (B.Tech) from college of Bharat Institute of Engineering and Technology
Project#1 : Tutella
 
 Testing Approach : Manual Testing , API Testing 
 Tool : ADO Board
Description: 
Tutella is another great app that simplifies the way you can find the trainer for your requirement from 
home only. Tutella means guardianship, the relation of a tutor to his student. It is an Interactive online 
Educating Platform where an aspired student can choose his personal trainer. TUTELLA Where Trainers
(Teachers, GYM, business...) can register themselves as a trainer to train students in their required field in any 
mode (online/offline) based on their preferences , whereas students can select their trainer by seeing their 
profile and demo of explanation and give a request to the trainer. Tutella is available in both web and mobile 
platforms and also its having admin panel manage the data.
Responsibilities:
 Understanding the Requirements and Functional Specifications of the Application
 Performed API testing
 Performed browser compatibility testing
 Prepared the Test cases based on BVA, ECP and experienced based testing
 Executed Test Cases and verified actual results against expected results.
 Involved in GUI Testing, Functional, Re-Testing and Regression testing.
 Login the defects in bug tracking tool and verify the defects logged by other teammates
 Interacting with Client daily and explain the progress of the project on Daily basis
 Regression testing is implemented at various phases of the development and test cycles.
 Providing screen shots to identify & reproduce the bugs in any environments.
 Executing the test cases, Regression and preparing the Defects and Test development and execution 
reports and retesting scrupulously
 Identifying the impacted areas for the bug fixes and development and review of test cases
Project#2 : SkillShoppy 
 
 
 Testing Approach : Manual Testing and Automation Testing
 Tool : ADO Board
Description: 
This project is a digital platform for selling and buying projects online. Anyone can register, login 
and then they can sell and buy any projects like web apps, mobile apps etc. This project shows different 
options for customer to earn the money and reviews option also available.
Responsibilities:
 Understanding the Requirements and Functional Specifications of the Application
 Performed browser compatibility testing
 Performed automation testing using selenium 
 Analyzing user requirements, developing Test Scenarios, Test Cases Preparation and Review the 
Documents
 Executed Test Cases and verified actual results against expected results.
 Involved in GUI Testing, Functional, Re-Testing and Regression testing.
 Login the defects in bug tracking tool and verify the defects logged by other teammates
 Interacting with Client daily and explain the progress of the project on Daily basis
 Regression testing is implemented at various phases of the development and test cycles.
 Providing screen shots to identify & reproduce the bugs in any environments.
Project#3 : Sanrai Pulmo Rehab
 Testing Approach : Manual Testing, Automation Testing
 Tools : jira
Description :
 This project is a Medical platform to consult a doctors through online. Anyone can register, 
login and then they can contact the specialist doctors through online This project shows different options 
for customer to solve their respective problems.
Responsibilities:
 Understanding the Requirements and Functional Specifications of the Application
 Performed automation testing using selenium 
 Analyzing user requirements, developing Test Scenarios, Test Cases Preparation and Review the 
Documents
 Executed Test Cases and verified actual results against expected results.
 Involved in GUI Testing, Functional, Re-Testing and Regression testing.
 Login the defects in bug tracking tool and verify the defects logged by other teammates
 Interacting with Client daily and explain the progress of the project on Daily basis
 Regression testing is implemented at various phases of the development and test cycles.
 Providing screen shots to identify & reproduce the bugs in any environments.
Personal Details:
Father Name G.V.RAJA GOPALA RAO
Marital Status Single
Languages Know Telugu, English
PAN Number CLFPG3941J
Date of Birth 29/08/1996
 As a Tester Self-Motivated, Quick Learner
Acknowledgement:
I hereby declare that the above furnished information is true to the best of my knowledge. 
Gopu Sai Sandeep
"""

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)
