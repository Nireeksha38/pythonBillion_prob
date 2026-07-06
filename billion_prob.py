# questions = [
#     ["What is the capital of India?", "Mumbai", "Chennai", "New Delhi", "Kolkata", 3],
#     ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
#     ["Who is known as the Father of the Nation in India?", "Jawaharlal Nehru", "Subhash Chandra Bose", "Mahatma Gandhi", "Bhagat Singh", 3],
#     ["Which language is used to develop Python?", "Java", "C", "Python", "C++", 3],
#     ["What is 5 + 7?", "10", "11", "12", "13", 3],
#     ["Which ocean is the largest?", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", 4],
#     ["Who wrote the Ramayana?", "Vyasa", "Kalidasa", "Valmiki", "Tulsidas", 3],
#     ["Which is the national animal of India?", "Lion", "Elephant", "Tiger", "Leopard", 3],
#     ["What is the boiling point of water?", "90", "100", "80", "120", 2],
#     ["Which company developed Windows?", "Apple", "Google", "Microsoft", "IBM", 3]
# ]

# for question in questions:
#     print(question[0])
#     print("1.", question[1])
#     print("2.", question[2])
#     print("3.", question[3])
#     print("4.", question[4])

#     answer = int(input("Enter the number corresponding to your answer: "))
#     if answer == question[5]:
#         print("Correct!")
#     else:
#         print("Wrong! The correct answer is:", question[question[5]])
questions = [
    ["What is the capital of India?", "Mumbai", "Chennai", "New Delhi", "Kolkata", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Who is known as the Father of the Nation in India?", "Jawaharlal Nehru", "Subhash Chandra Bose", "Mahatma Gandhi", "Bhagat Singh", 3],
    ["Which language is used to develop Python?", "Java", "C", "Python", "C++", 3],
    ["What is 5 + 7?", "10", "11", "12", "13", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["Who wrote the Ramayana?", "Vyasa", "Kalidasa", "Valmiki", "Tulsidas", 3],
    ["Which is the national animal of India?", "Lion", "El  ephant", "Tiger", "Leopard", 3],
    ["What is the boiling point of water?", "90", "100", "80", "120", 2],
    ["Which company developed Windows?", "Apple", "Google", "Microsoft", "IBM", 3]
]
for question in questions:
    print(question[0])
    print("1.", question[1])
    print("2.", question[2])
    print("3.", question[3])
    print("4.", question[4])
   
    answer = int(input("Enter the number corresponding to your answer: "))
    if answer == question[5]:
        print("Correct!")   
    else:
        print("Wrong! The correct answer is:", question[question[5]])