import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define the lists for your data
names = [
    "Hussaini Muhammad", "Said Abba Ahmad", "MUDASSIR SUNUSI", "Asiya Hassan Muhammad", "Faiza Abubakar Ahmad", 
    "Aminu Barau", "ABDULHADI SULAIMAN", "Abdullahi Saidu", "Husaini magaji abubakar", "Hafsat Sufiyan", 
    "Hauwa Ibrahim mudi", "UmmuSulaim Yakubu", "Lurwan shuaibu", "Abba Aminu", "Suleiman yahaya", 
    "Mukhtar Abubakar", "Aisha Abubakar Garba", "Khadija Bashir Abdulkadir", "Maryam sulaiman Adam", "Zakiya nura yusuf", 
    "Nafisa yahya", "Maryam Muhammad sani", "Ibrahim muhammad musa", "Aliyu Muhammad", "Sulaiman Abdulnafiu", 
    "Hadiza lawan miko", "Nafiu Rabiu kani", "Abubakar Saleh Inusa", "Umar Umar", "Bello Usman", 
    "Yakubu Khalid", "Hakilu Saidu", "Amina Abba muhamm", "Abdullahi Shuaibu", "Sulaiman Aminu Umar", "Abdulaziz Yusuf", 
    "Amina muhammad rabiu", "Fatima sani", "Samir Isah Alkasim", "Dahiru Aminu", "Abubakar Ismail", 
    "Fatima muhammad rabiu", "Anas inuwa", "Hafsat muhammad rabiu", "Hajjara muhammad rabiu", "altine muhammad", 
    "Asabe muhammad", "Lawan Ibrahim", "Abdulmumini kabiru", "Umma Ahmad Ibrahim", "Yusuf lurwanu", 
    "Abdullahi Muhammad", "Jamilu suleman", "ALYASAU ZULADAINI", "Usman zubairu", "Sulaiman Muhammad kosa", 
    "Sa'adu shu'aibu", "IBRAHIM AHMAD", "Fiddausi Umar", "Usman Idris", "Yusuf abdullahi Mezan", "Shuaibu suleman", 
    "Yahaya Hamza Yahaya Marke", "Sani babandi", "AISHA KAMAL LAWAN", "Umar Sulaiman Umar", "Aminu Abdullahi Inuwa", 
    "Abubakar Nasiru", "Hassan Muhammad Bello", "Musa auwal", "Halima Muhammad", "Abubakar Aminu", 
    "Abubakar isyaku", "Batula dandabi", "Asmau yakubu", "NURA YAU MUHAMMAD", "Usman Ibrahim", 
    "Sulaiman Rilwan Yusif", "Ibrahim mahmud", "Adamu Sulaiman", "MUSA ALIYU", "Abdullahi Ibrahim", 
    "ABDULLAHI TIJJANI", "Abdurrahman nura sule", "Auwalu Faruq", "Muhammad Mukhtar", "Umar kabir", 
    "Abubakar sabo Muhammad", "Adamu sulaiman yaroro", "Ismail isyaku", "AHMAD BASHIR"
]

local_governments = [
    "Auyo", "Babura", "Biriniwa", "Birnin Kudu", "Buji", "Dutse", "Gagarawa", "Garki", "Gumel", "Guri", 
    "Gwaram", "Gwiwa", "Hadejia", "Jahun", "Kafin Hausa", "Kaugama", "Kazaure", "Kiri Kasama", "Kiyawa", 
    "Maigatari", "Malam Madori", "Miga", "Ringim", "Roni", "Sule Tankarkar", "Taura", "Yankwashi"
]

ages = ["Under 18", "18-24", "25-30", "31-35", "36 and above"]
genders = ["Male", "Female"]
education_levels = ["Primary", "Secondary", "Tertiary", "Vocational Training", "No formal education"]
employment_statuses = ["Employed (Full-time)", "Employed (Part-time)", "Self-employed/Entrepreneur", "Unemployed", "Student"]
financial_support_levels = ["Very difficult", "Difficult", "Neutral", "Easy", "Very easy"]
training_usefulness = ["Very useful", "Useful", "Neutral", "Not useful", "Not applicable"]
electricity_reliability = ["Very reliable", "Reliable", "Unreliable", "Very unreliable"]
internet_access = ["Excellent", "Good", "Fair", "Poor", "No access at all"]
market_access = ["Very easy", "Easy", "Neutral", "Difficult", "Very difficult"]
programs_fairness = ["Yes", "No", "Not sure"]
favoritism_experienced = ["Yes", "No", "Prefer not to say"]

# Pre-defined meaningful responses for the last two questions
government_roles = [
    "Provide access to affordable finance and reduce bureaucratic hurdles.",
    "Invest in infrastructure such as electricity, roads, and internet to support businesses.",
    "Offer more training programs focused on business management and entrepreneurship.",
    "Facilitate better market access and networking opportunities for young entrepreneurs.",
    "Implement transparent and corruption-free policies in empowerment programs."
]

suggestions_comments = [
    "The government should establish more youth-friendly financial institutions.",
    "There should be regular mentorship programs for young entrepreneurs.",
    "It's crucial to improve electricity supply to enhance business operations.",
    "The internet accessibility in rural areas needs to be addressed to help businesses grow.",
    "Youth empowerment programs should be monitored to ensure fairness and transparency."
]

# Create a list to store data
data = []

for _ in range(1000):
    name = random.choice(names)
    email_name_part = name .lower().replace(" ", "")
    email = f"{email_name_part}{random.randint(1, 100)}@gmail.com"
    
    response = {
        "Email": email,
        "Full Name": name,
        "Age": random.choice(ages),
        "Gender": random.choice(genders),
        "Local Government Area (LGA)": random.choice(local_governments),
        "Level of Education": random.choice(education_levels),
        "What is your current employment status?": random.choice(employment_statuses),
        "If self-employed, what type of business do you own or operate?": fake.word() if random.choice(employment_statuses) == "Self-employed/Entrepreneur" else "",
        "What are the main challenges you face in starting or growing your business?": ', '.join(random.sample([
            "Lack of access to finance", "Inadequate business skills", "Poor infrastructure (e.g., electricity, roads, internet)", 
            "Limited market access", "Bureaucratic challenges (e.g., registration, permits)", 
            "Corruption and favoritism", "Lack of mentorship and support", "Other…"], 2)),
        "How difficult is it for you to access financial support (loans, grants, etc.)?": random.choice(financial_support_levels),
        "Have you participated in any government or NGO-led entrepreneurship training programs?": random.choice(["Yes", "No"]),
        "If yes, how useful was the training in improving your business skills?": random.choice(training_usefulness) if random.choice(["Yes", "No"]) == "Yes" else "",
        "How reliable is the electricity supply in your area?": random.choice(electricity_reliability),
        "How would you rate your access to the internet for business purposes?": random.choice(internet_access),
        "How easy is it for you to reach larger markets outside your LGA?": random.choice(market_access),
        "Do you believe that existing youth empowerment programs in Jigawa State are fair and transparent?": random.choice(programs_fairness),
        "Have you or someone you know experienced favoritism or corruption in any empowerment programs?": random.choice(favoritism_experienced),
        "What specific support would help you most in growing your business?": ', '.join(random.sample([
            "Access to affordable finance", "Business management training", "Improved infrastructure (electricity, internet, roads)", 
            "Better access to markets", "Simplified business registration and permits", 
            "Mentorship and networking opportunities", "Other…"], 2)),
        "What role do you think the government should play in supporting youth entrepreneurs?": random.choice(government_roles),
        "Please provide any additional suggestions or comments on how to improve youth empowerment and entrepreneurship in Jigawa State.": random.choice(suggestions_comments),
        "Do you consent to participate in this survey and allow your responses to be used for the purpose of this project?": "Yes"
    }
    data.append(response)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel('survey_responses.xlsx', index=False)
