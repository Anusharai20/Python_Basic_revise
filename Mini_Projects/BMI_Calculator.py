"""
==================================================
                BMI CALCULATOR
==================================================

Project      : Mini Python Project
Author       : Anusha Rai
Concepts     :
                ✔ Variables
                ✔ User Input
                ✔ Type Conversion
                ✔ Arithmetic Operators
                ✔ Functions
                ✔ Conditional Statements

==================================================
"""
# Convert Feet & Inches to Meters
def convert_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    meters = total_inches * 0.0254
    return meters

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to determine BMI category
def bmi_category(bmi):  
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
    
    
    
# Main function
def main(): 
    print("Welcome to the BMI Calculator!")
    
    print("=" * 50)
    print("          🏥 BODY MASS INDEX CALCULATOR")
    print("=" * 50)
    # Get user input for their credentials and measurements
    name = input("👤 Enter your name: ")
    age = int(input("🎂 Enter your age: "))
    weight = float(input("Enter your weight in kilograms: "))
    feet = int(input("📏 Enter your height in feet: ")) #for height
    inches = int(input("📏 Enter your height in inches: ")) #for height
    
    # Convert height to meters
    height = convert_to_meters(feet, inches)
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Determine BMI category
    category = bmi_category(bmi)
    
    # Display the result
    print("=" * 50)
    print("          🏥 YOUR BODY MASS INDEX RESULT IS HERE             ")
    print("=" * 50)
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Weight: {weight} kg")
    print(f"Height: {feet} feet {inches} inches ({height:.2f} meters)")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")
    print("=" * 50)
    if category == "Underweight":
        print("💡 Advice : Eat a balanced diet and consult a nutritionist if needed.")

    elif category == "Normal Weight":
            print("🎉 Great! You are maintaining a healthy weight.")

    elif category == "Overweight":
            print("🏃 Try regular exercise and maintain a healthy diet.")

    else:
            print("⚠️ Consider consulting a healthcare professional for guidance.")

    print("-" * 50)

    print("😊 Thank you for using the BMI Calculator!")

    print("=" * 50)


# Run the main function
if __name__ == "__main__":
    main()  
    