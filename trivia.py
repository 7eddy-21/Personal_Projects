import random

questions = {
    "What is the only planet in our solar system that rotates clockwise?": "venus",
    "In which year did the United States purchase Alaska from Russia?": "1867",
    "What is the name of the deepest point in the Earth's oceans?": "challenger deep",
    "Who was the last pharaoh of ancient Egypt?": "cleopatra vii",
    "Which element has the chemical symbol 'W'?": "tungsten",
    "The word 'robot' comes from a 1920s play. What language is it from?": "czech",
    "What is the name of the famous ship that Charles Darwin sailed on during his voyage of discovery?": "hms beagle",
    "Who composed the 'Moonlight Sonata'?": "ludwig van beethoven",
    "What is the capital of New Zealand?": "wellington",
    "What is the largest living species of lizard?": "komodo dragon",
    "In physics, what is the term for a particle with a positive charge and a negative charge in equal amounts, making it electrically neutral?": "neutron",
    "Which country is known as the 'Land of the Rising Sun'?": "japan",
    "What is the name of the galaxy that is closest to the Milky Way?": "andromeda galaxy",
    "Who wrote the novel 'One Hundred Years of Solitude'?": "gabriel garcia marquez",
    "What is the name of the world's largest hot desert?": "sahara desert",
    "Which Roman emperor made Christianity the state religion of the Roman Empire?": "theodosius i",
    "What is the largest organ in the human body?": "skin",
    "What is the official currency of Switzerland?": "swiss franc",
    "In which city was the first modern Olympic Games held?": "athens",
    "What is the name of the iconic clock tower in London?": "big ben",
    "Which country has the most natural lakes?": "canada",
    "What is the fear of long words called?": "hippopotomonstrosesquippedaliophobia",
    "What is the chemical formula for water?": "h2o",
    "Who was the first woman to win a Nobel Prize?": "marie curie",
    "Which animal has the highest blood pressure?": "giraffe",
    "What is the capital of Australia?": "canberra",
    "Which famous scientist developed the theory of relativity?": "albert einstein",
    "What is the name of the longest river in the world?": "nile river",
    "What is the primary gas found in the sun?": "hydrogen",
    "What is the smallest country in the world?": "vatican city",
    "Which part of the brain is responsible for memory and learning?": "hippocampus",
    "What is the name of the mythological creature that is half-man and half-horse?": "centaur",
    "Who painted the 'Mona Lisa'?": "leonardo da vinci",
    "What is the largest bone in the human body?": "femur",
    "Which ancient wonder of the world is located in modern-day Iraq?": "hanging gardens of babylon",
    "What is the study of mushrooms called?": "mycology",
    "Which country is the world's largest producer of coffee?": "brazil",
    "In what year did the Titanic sink?": "1912",
    "What is the name of the highest mountain in Africa?": "mount kilimanjaro",
    "What is the name of the first satellite launched into space by the Soviet Union?": "sputnik 1",
    "What is the term for a word that is spelled the same forwards and backward?": "palindrome",
    "Which city hosted the 2016 Summer Olympics?": "rio de janeiro",
    "What is the name of the largest moon of Saturn?": "titan",
    "What is the process by which plants make their own food called?": "photosynthesis",
    "Who was the first President of the United States?": "george washington",
    "Which continent is the driest on Earth?": "antarctica",
    "What is the largest country in the world by land area?": "russia",
    "What is the name of the fear of heights?": "acrophobia",
    "What is the main ingredient in hummus?": "chickpeas",
    "What is the name of the first artificial satellite to orbit the Earth?": "sputnik 1"
}

def ultimate_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}.{question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("You got it Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}. \n")

    print(f"Game over! You final score is: {score}/{total_questions}")


ultimate_trivia_game()