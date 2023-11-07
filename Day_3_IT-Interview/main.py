# ASCII Art: IT Interview

# Define the ASCII art
ascii_it_interview = """
            _________
           |  _____  |    ______
           | |     | |   |  __  |
           | |_____| |   | |__| |
           |_________|   |______|
           |  _____  |   /      \\
           | |     | |  /  --o  |
           | |_____| | /_________\\
           |_________|
           //         \\
          //           \\
         //    o        \\
        //_______________\\
"""

# Print the ASCII art
print("Welcome to my IT interview. This will be a set of questions that test your tech knowledge and see if you can pass an IT interview. \n")
print(ascii_it_interview)

# ASCII Art: IT Interview Outcomes

# Define the ASCII art for passing the interview
pass_interview = """
      _________
     |         |
     |  ^   ^  |
     |    -    |  < Yay! You passed, congradulation. Welcome to the company!
     |  \___/  |
     |_________|
"""

# Define the ASCII art for failing the interview
fail_interview = """
      _________
     |         |
     |  >   <  |
     |    -    |  < Sorry i don't think you are a good fit!
     |   ___   |
     |_________|

     Thanks for takin the time to interview with us.
"""


print("Let's start this interview with some coding questions.\n")

question_1 = input("Have you ever implemented a search algorithm in a production environment? Yes or No\n")

if question_1.lower() == "yes":
    question_2 = input("Are you familiar with writing unit tests for your code? Yes or No\n")
   
    if question_2.lower() == "yes": 
        print("Let's move on to the next part of the interview. System Design.\n\n")
        # You should ask the next question here or take appropriate action for the next part of the interview
    else:
        print(fail_interview)
else:
    print(fail_interview)














# # Function to print ASCII art based on interview outcome
# def print_interview_outcome(passed):
#     if passed:
#         print(ascii_pass_interview)
#     else:
#         print(ascii_fail_interview)

# # Example Usage:
# # Print outcome for passing the interview
# print_interview_outcome(True)

# # Print outcome for failing the interview
# print_interview_outcome(False)







