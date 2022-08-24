"""3 in one game
1.rock paper scissors
2.Hangman
3.Quiz"""

import mysql.connector
import random
import time


m1 = mysql.connector.connect(host="localhost", user="root", password="admin")

mycursor = m1.cursor()

try:
    mycursor.execute("CREATE DATABASE cs_project")
    mycursor.execute("USE cs_project")
    mycursor.execute(
        "Create TABLE Score_Hangman(name varchar(15), score int(20),Wins int(3))"
    )
    mycursor.execute(
        "Create TABLE Score_RPS(name varchar(15), score int(20),Wins int(3))"
    )
    mycursor.execute(
        "Create TABLE Score_Quiz(name varchar(15), score int(20),Wins int(3))"
    )
except:
    mycursor.execute("USE cs_project")

print(
    """
Which game would you like to play?

                                                1)Hangman
                                                2)Rock Paper Scissors
                                                3)Quiz
"""
)

print()
score_RPS = 0
win_RPS = 0
game = input("Which game would you like to play?: ")
username = input("What is your name?: ")

mycursor.execute("SELECT name from Score_RPS")
myresult_1 = mycursor.fetchall()
# print(myresult_1)
var_name = 0
# print(len(myresult_1))
# for var_name in range(len(myresult_1)):
if len(myresult_1) > 0 and username in myresult_1[var_name]:
    print("WELCOME BACK")
else:
    sql1234 = "INSERT INTO Score_RPS values(%s,%s,%s)"
    var123 = (username, 0, 0)
    mycursor.execute(sql1234, var123)
    m1.commit()


Lhangman = ["hangman", "1", "1)", "1)hangman", "1 hangman"]
Lrps = [
    "rock paper scissor",
    "rock paper scissors",
    "2",
    "2)",
    "2)rock paper scissor",
    "2)rock paper scissor",
    "rps",
    "2)rps",
    "2 rps",
]
Lquiz = ["quiz", "3", "3)", "3 quiz", "3)quiz"]

Lgames = Lhangman + Lrps + Lquiz

yes = ["YES", "yes", "Yes", "Y", "y"]
no = ["NO", "no", "No", "N", "n"]
quit = ["QUIT", "quit", "Quit"]

L_stats = ["statistics", "statistic", "stats", "stat", "s"]

while game in Lgames:

    # rock paper scissors started

    while game in Lrps:

        rps = ["Rock", "Paper", "Scissors"]
        playagain = "yes"

        L_rock = ["Rock", "rock", "r", "stone"]
        L_paper = ["Paper", "paper", "p"]
        L_scissors = ["Scissors", "scissors", "scissor", "s"]

        L_rps = [L_rock, L_paper, L_scissors]

        user_choice_rock = 0
        user_choice_paper = 0
        user_choice_scissors = 0

        computer_choice_rock = 0
        computer_choice_paper = 0
        computer_choice_scissors = 0

        user_win_rock = 0
        user_win_paper = 0
        user_win_scissors = 0

        user_lose_rock = 0
        user_lose_paper = 0
        user_lose_scissors = 0

        computer_win_rock = 0
        computer_win_paper = 0
        computer_win_scissors = 0

        computer_lose_rock = 0
        computer_lose_paper = 0
        computer_lose_scissors = 0

        tie_rock = 0
        tie_paper = 0
        tie_scissors = 0

        rock_figure_user = """
        		            _______
        		        ---'   ____)
        Y  	              		(_____)
        O      		        	(_____)
        U		                (____)
        		        ---.__(___)

                """
        paper_figure_user = """
        		            _______
        		        ---'   ____)____
        Y		                  ______)
        O		                  _______)
        U		                 _______)
        		        ---.__________)
        		        """

        scissors_figure_user = """
        		            _______
        		        ---'   ____)____
        Y		                  ______)
        O		               __________)
        U		              (____)
        		        ---.__(___)
        				"""
        rock_figure_computer = """
        C
        O		            _______
        M		        ---'   ____)
        P  	              	   (_____)
        U      		            (_____)
        T		               (____)
        E		        ---.__(___)
        R
                """
        paper_figure_computer = """

        C
        O		            _______
        M		        ---'   ____)____
        P		                  ______)
        U		                  _______)
        T		                 _______)
        E		        ---.__________)
        R

        		        """

        scissors_figure_computer = """

        C
        O		            _______
        M		        ---'   ____)____
        P		                  ______)
        U		               __________)
        T		              (____)
        E		        ---.__(___)
        R

                """

        clash_figure = """
                __   __
                 \ \ / /
                  \ V /
                   > <
                  / .   \ 
                 /_/ \_\ 
                """

        tie_figure = """

  _____ _   _               _______ _____ ______
 |_   _| | ( )             |__   __|_   _|  ____|
   | | | |_|/ ___    __ _     | |    | | | |__
   | | | __| / __|  / _` |    | |    | | |  __|
  _| |_| |_  \__ \ | (_| |    | |   _| |_| |____
 |_____|\__| |___/  \__,_|    |_|  |_____|______|


"""
        win_figure = """



YYYYYYY       YYYYYYY                                     WWWWWWWW                           WWWWWWWW
Y:::::Y       Y:::::Y                                     W::::::W                           W::::::W
Y:::::Y       Y:::::Y                                     W::::::W                           W::::::W
Y::::::Y     Y::::::Y                                     W::::::W                           W::::::W
YYY:::::Y   Y:::::YYYooooooooooo   uuuuuu    uuuuuu        W:::::W           WWWWW           W:::::W ooooooooooo   nnnn  nnnnnnnn
   Y:::::Y Y:::::Y oo:::::::::::oo u::::u    u::::u         W:::::W         W:::::W         W:::::Woo:::::::::::oo n:::nn::::::::nn
    Y:::::Y:::::Y o:::::::::::::::ou::::u    u::::u          W:::::W       W:::::::W       W:::::Wo:::::::::::::::on::::::::::::::nn
     Y:::::::::Y  o:::::ooooo:::::ou::::u    u::::u           W:::::W     W:::::::::W     W:::::W o:::::ooooo:::::onn:::::::::::::::n
      Y:::::::Y   o::::o     o::::ou::::u    u::::u            W:::::W   W:::::W:::::W   W:::::W  o::::o     o::::o  n:::::nnnn:::::n
       Y:::::Y    o::::o     o::::ou::::u    u::::u             W:::::W W:::::W W:::::W W:::::W   o::::o     o::::o  n::::n    n::::n
       Y:::::Y    o::::o     o::::ou::::u    u::::u              W:::::W:::::W   W:::::W:::::W    o::::o     o::::o  n::::n    n::::n
       Y:::::Y    o::::o     o::::ou:::::uuuu:::::u               W:::::::::W     W:::::::::W     o::::o     o::::o  n::::n    n::::n
       Y:::::Y    o:::::ooooo:::::ou:::::::::::::::uu              W:::::::W       W:::::::W      o:::::ooooo:::::o  n::::n    n::::n
    YYYY:::::YYYY o:::::::::::::::o u:::::::::::::::u               W:::::W         W:::::W       o:::::::::::::::o  n::::n    n::::n
    Y:::::::::::Y  oo:::::::::::oo   uu::::::::uu:::u                W:::W           W:::W         oo:::::::::::oo   n::::n    n::::n
    YYYYYYYYYYYYY    ooooooooooo       uuuuuuuu  uuuu                 WWW             WWW            ooooooooooo     nnnnnn    nnnnnn







"""
        lose_figure = """



YYYYYYY       YYYYYYY                                     LLLLLLLLLLL
Y:::::Y       Y:::::Y                                     L:::::::::L
Y:::::Y       Y:::::Y                                     L:::::::::L
Y::::::Y     Y::::::Y                                     LL:::::::LL
YYY:::::Y   Y:::::YYYooooooooooo   uuuuuu    uuuuuu         L:::::L                  ooooooooooo       ssssssssss       eeeeeeeeeeee
   Y:::::Y Y:::::Y oo:::::::::::oo u::::u    u::::u         L:::::L                oo:::::::::::oo   ss::::::::::s    ee::::::::::::ee
    Y:::::Y:::::Y o:::::::::::::::ou::::u    u::::u         L:::::L               o:::::::::::::::oss:::::::::::::s  e::::::eeeee:::::ee
     Y:::::::::Y  o:::::ooooo:::::ou::::u    u::::u         L:::::L               o:::::ooooo:::::os::::::ssss:::::se::::::e     e:::::e
      Y:::::::Y   o::::o     o::::ou::::u    u::::u         L:::::L               o::::o     o::::o s:::::s  ssssss e:::::::eeeee::::::e
       Y:::::Y    o::::o     o::::ou::::u    u::::u         L:::::L               o::::o     o::::o   s::::::s      e:::::::::::::::::e
       Y:::::Y    o::::o     o::::ou::::u    u::::u         L:::::L               o::::o     o::::o      s::::::s   e::::::eeeeeeeeeee
       Y:::::Y    o::::o     o::::ou:::::uuuu:::::u         L:::::L         LLLLLLo::::o     o::::ossssss   s:::::s e:::::::e
       Y:::::Y    o:::::ooooo:::::ou:::::::::::::::uu     LL:::::::LLLLLLLLL:::::Lo:::::ooooo:::::os:::::ssss::::::se::::::::e
    YYYY:::::YYYY o:::::::::::::::o u:::::::::::::::u     L::::::::::::::::::::::Lo:::::::::::::::os::::::::::::::s  e::::::::eeeeeeee
    Y:::::::::::Y  oo:::::::::::oo   uu::::::::uu:::u     L::::::::::::::::::::::L oo:::::::::::oo  s:::::::::::ss    ee:::::::::::::e
    YYYYYYYYYYYYY    ooooooooooo       uuuuuuuu  uuuu     LLLLLLLLLLLLLLLLLLLLLLLL   ooooooooooo     sssssssssss        eeeeeeeeeeeeee







"""
        rules_rps = """
        INSTRUCTIONS :


        1)Instead of typing the full word, you can also type just the first initial of the word you want to choose.
                For eg: Instead of typing full 'Scissors' you can just type 'S'

        2)To end the Game Type Quit and Hit Enter

        3)Your input is not case sensitive

        4)You will get the Detailed Statistics at the End of the Game

        5)To read the Instructions Again, type Rules or Instructions and Hit Enter


        """

        L_rules_rps = ["rules", "rule", "instructions", "instructions"]
        print(rules_rps)

        print()

        print("**********Type Quit to end the Game**********")

        print()

        user_selection_rps = input("Select Rock Paper or Scissors: ").lower()

        while user_selection_rps not in quit:

            for i in range(3):
                if user_selection_rps in L_rps[i]:
                    rps_topic_index = i
                    break

            computer_selection_rps = random.choice(rps)

            if (
                user_selection_rps in L_rock
                or user_selection_rps in L_paper
                or user_selection_rps in L_scissors
            ):

                user_win_RPS = ""

                print()
                print(f"You Chose:{L_rps[i][0]}")
                print(f"Computer Chose : {computer_selection_rps}")

                if user_selection_rps in L_rock and computer_selection_rps in L_rock:
                    print(rock_figure_user, clash_figure, rock_figure_computer)
                    print(tie_figure)

                    user_choice_rock += 1
                    computer_choice_rock += 1
                    tie_rock += 1

                elif (
                    user_selection_rps in L_scissors
                    and computer_selection_rps in L_scissors
                ):
                    print(scissors_figure_user, clash_figure, scissors_figure_computer)
                    print(tie_figure)

                    user_choice_scissors += 1
                    computer_choice_scissors += 1
                    tie_scissors += 1

                elif (
                    user_selection_rps in L_paper and computer_selection_rps in L_paper
                ):
                    print(paper_figure_user, clash_figure, paper_figure_computer)
                    print(tie_figure)

                    user_choice_paper += 1
                    computer_choice_paper += 1
                    tie_paper += 1

                elif user_selection_rps in L_rock and computer_selection_rps in L_paper:
                    print(rock_figure_user, clash_figure, paper_figure_computer)
                    print(lose_figure)

                    user_choice_rock += 1
                    computer_choice_paper += 1

                    user_lose_rock += 1
                    computer_win_paper += 1

                elif (
                    user_selection_rps in L_rock
                    and computer_selection_rps in L_scissors
                ):
                    print(rock_figure_user, clash_figure, scissors_figure_computer)
                    print(win_figure)

                    user_choice_rock += 1
                    computer_choice_scissors += 1
                    user_win_rock += 1
                    computer_lose_scissors += 1
                    user_win_RPS = "yes"

                elif (
                    user_selection_rps in L_paper
                    and computer_selection_rps in L_scissors
                ):
                    print(paper_figure_user, clash_figure, scissors_figure_computer)
                    print(lose_figure)

                    user_choice_paper += 1
                    computer_choice_scissors += 1

                    user_lose_paper += 1
                    computer_win_scissors += 1

                elif user_selection_rps in L_paper and computer_selection_rps in L_rock:
                    print(paper_figure_user, clash_figure, rock_figure_computer)
                    print(win_figure)

                    user_choice_paper += 1
                    computer_choice_rock += 1

                    user_win_paper += 1
                    user_win_RPS = "yes"
                    computer_lose_rock += 1

                elif (
                    user_selection_rps in L_scissors
                    and computer_selection_rps in L_rock
                ):
                    print(scissors_figure_user, clash_figure, rock_figure_computer)
                    print(lose_figure)

                    user_choice_scissors += 1
                    computer_choice_rock += 1

                    user_lose_scissors += 1
                    computer_win_rock += 1

                elif (
                    user_selection_rps in L_scissors
                    and computer_selection_rps in L_paper
                ):
                    print(scissors_figure_user, clash_figure, paper_figure_computer)
                    print(win_figure)

                    user_choice_scissors += 1
                    computer_choice_paper += 1

                    user_win_scissors += 1
                    user_win_RPS = "yes"
                    computer_lose_paper += 1

                if user_win_RPS == "yes":
                    win_RPS += 1
                    score_RPS += 50

                score_update_rps = "UPDATE Score_RPS set score=%s where name=%s"
                score_data_var_rps = (score_RPS, username)
                mycursor.execute(score_update_rps, score_data_var_rps)
                m1.commit()

                win_update_rps = "UPDATE Score_RPS set Wins=%s where name=%s"
                win_data_var = (win_RPS, username)
                mycursor.execute(win_update_rps, win_data_var)
                m1.commit()

            elif user_selection_rps in L_rules_rps:
                print(rules_rps)

            else:
                print()
                print("Please give a correct input")

            print()
            print("**********Type Quit to end the Game**********")
            print()
            user_selection_rps = input("Select rock paper or scissors: ").lower()

        print()
        print("THE GAME HAS ENDED")
        print()

        score_selection_rps = "SELECT * FROM Score_RPS WHERE name = %s"
        user_var_rps = (username,)
        mycursor.execute(score_selection_rps, user_var_rps)
        myresult_rps = mycursor.fetchall()
        for resultloop in myresult_rps:
            print(
                resultloop[0],
                "won",
                resultloop[2],
                "games and scored",
                resultloop[1],
                "points",
            )
            print()

        playagain = input("Do you want to play again?: ").lower()

        if playagain not in yes:
            another_game = input("Do you want to play any other game? ").lower()

            if another_game in yes:
                game = (
                    input(
                        "What game do you want to play?(Hangman, rock paper scissors, Quiz): "
                    )
                ).lower()
            else:
                game = ""
                print("Bye")
                break

    # rock paper scissors ended

    # Hangman Started
    while game in Lhangman:
        score_Hangman = 0
        win_Hangman = 0
        word_list_h = [
            "abruptly",
            "jazz",
            "absurd",
            "abyss",
            "affix",
            "askew",
            "avenue",
            "awkward",
            "axiom",
            "azure",
            "bagpipes",
            "bandwagon",
            "banjo",
            "bayou",
            "beekeeper",
            "blitz",
            "blizzard",
            "bookworm",
            "boxcar",
            "boxful",
            "buzzing",
            "crypt",
            "dizzying",
            "duplex",
            "embezzle",
            "frizzled",
            "glowworm",
            "gnarly",
            "haphazard",
            "jackpot",
            "jigsaw",
            "larynx",
            "lymph",
            "mystify",
            "oxidize",
            "queue",
            "matrix",
            "whiskey",
            "psyche",
        ]

        playagain_hangman = "yes"

        while playagain_hangman in yes:
            random_word_h = random.choice(word_list_h)
            unique_random_word_h = ""  # this will find the unique chars in the word

            for i in random_word_h:
                if i not in unique_random_word_h:
                    unique_random_word_h += i
            # for eg: earlier assassinate would get 8 hints(game would be finished in 6 correct tries only), but now only 3 hints given
            hints = len(unique_random_word_h) - 3
            wrong = 6
            list_hangman_figure = [
                """
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========""",
                """
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========""",
                """
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========""",
                """
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========""",
                """
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
            =========""",
                """
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========""",
                """
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |""",
            ]

            print(
                """
            ------------------------------------------------------HERE YOU GO!------------------------------------------------------
            """
            )

            print(list_hangman_figure[6])
            print()
            print()
            print()

            L1 = []

            for i in range(len(random_word_h)):
                L1.insert(i, "_")

            list_tr = list(random_word_h)
            wrong_counter = 0
            hints_counter = 0
            hangman_figure_counter = 0

            print(
                "RULES--> 1.DON'T ENTER THE SAME LETTER TWICE OR YOU WILL LOSE A LIFE!"
            )
            print("         2.Type hint if you want to use a hint")
            print()
            print(
                "GUESS THIS WORD :  ",
                "_ " * len(random_word_h),
                "(",
                len(random_word_h),
                " CHARACTERS )",
            )
            print("You have BEEN GRANTED ", hints, "  HINTS and  ", wrong, "  LIVES.")

            while wrong_counter < wrong:
                user_selection_hangman = input("Enter a letter :  ").lower()
                print()

                if user_selection_hangman.lower() in list_tr:
                    while user_selection_hangman.lower() in list_tr:
                        L1[
                            list_tr.index(user_selection_hangman.lower())
                        ] = user_selection_hangman.lower()
                        list_tr[list_tr.index(user_selection_hangman.lower())] = ""

                    print("YAY!! You guessed the letter correct")
                    print("The word is  ", (" ".join(L1)).upper())

                    print()

                    print("HINTS left  :  ", hints - hints_counter)
                    print("You have ", wrong - wrong_counter, "LIVES remaining")

                    print()

                    print("*" * 100)

                    print()

                elif user_selection_hangman in ["Hint", "hint", "HINT"]:

                    if hints_counter < hints:
                        random_letter_h = random.choice("".join(list_tr))

                        while random_letter_h in list_tr:
                            L1[list_tr.index(random_letter_h)] = random_letter_h
                            list_tr[list_tr.index(random_letter_h)] = ""

                        print("The word is  ", (" ".join(L1)).upper())
                        print()

                        hints_counter += 1

                        print("HINTS left  :  ", hints - hints_counter)
                        print("You have ", wrong - wrong_counter, "LIVES remaining")
                        print()
                        print("*" * 100)
                        print()

                    else:

                        print("You are OUT OF HINTS")

                        print()

                        print("You have ", wrong - wrong_counter, "LIVES remaining")

                        print()

                        print("The word is  ", (" ".join(L1)).upper())

                        print()

                        print("*" * 100)

                        print()

                else:
                    print("OOPS! This is the wrong letter. You lost a LIFE.")
                    wrong_counter += 1

                    if hangman_figure_counter >= 0:
                        print(list_hangman_figure[5 - hangman_figure_counter])
                        hangman_figure_counter += 1

                    print("You have ", wrong - wrong_counter, "LIVES remaining")

                    print()

                    print("HINTS left  :  ", hints - hints_counter)

                    print()

                    print("The word is  ", (" ".join(L1)).upper())

                    print()

                    print("*" * 100)

                    print()

                if "".join(L1) == "".join(random_word_h): #if game won

                    win_Hangman += 1
                    score_Hangman += 100
                    score_update_Hangman = (
                        "UPDATE Score_Hangman set score=%s where name=%s"
                    )

                    score_data_var_Hangman = (score_Hangman, username)
                    mycursor.execute(score_update_Hangman, score_data_var_Hangman)
                    m1.commit()

                    win_update_Hangman = (
                        "UPDATE Score_Hangman set Wins=%s where name=%s"
                    )
                    win_data_var_Hangman = (win_Hangman, username)
                    mycursor.execute(win_update_Hangman, win_data_var_Hangman)
                    m1.commit()

                    print(
                        "HOORAY!!! You won the game...   with",
                        wrong - wrong_counter,
                        "Lives remaining and ",
                        hints - hints_counter,
                        " Hints left",
                    )

                    print()
                    print("*" * 100)

                    break

                if wrong - wrong_counter == 0:
                    print("OH NO! THE WORD WAS ", (" ".join(random_word_h)).upper())
                    print("<>" * 26, "<YOU LOSE!>", "<>" * 26)
                    print(
                        "-*" * 19,
                        "-->>>>>>>>BETTER LUCK NEXT TIME!!<<<<<<<<--",
                        "*-" * 19,
                    )

                    break

            ()
            score_selection_Hangman = "SELECT * FROM Score_Hangman WHERE name = %s"
            user_var_Hangman = (username,)
            mycursor.execute(score_selection_Hangman, user_var_Hangman)
            myresult_Hangman = mycursor.fetchall()
            for resultloop_Hangman in myresult_Hangman:
                print(
                    resultloop[0],
                    "won",
                    resultloop[2],
                    "games and scored",
                    resultloop[1],
                    "points",
                )
            print()


            playagain_hangman = (input("Do you want to play again?: ")).lower()

        if playagain_hangman not in yes:
            another_game = (input("Do you want to play any other game? ")).lower()
            if another_game in yes:
                game = (
                    input(
                        "What game do you want to play?(Hangman, rock paper scissors, Quiz): "
                    )
                ).lower()
            else:
                game = ""
                print("Bye")
                break

    ##############################################################################################################################   QUIZ STARTS ###############################################################

    while game in Lquiz:

        L_tech = [
            "1",
            "1.",
            "Tech",
            "tech",
            "TECH",
            "Technology",
            "technology",
            "TECHNOLOGY",
        ]
        L_video_games = [
            "2",
            "2.",
            "Video Games",
            "Video games",
            "VIDEO GAMES",
            "video games",
            "Video Game",
            "Video game",
            "VIDEO GAME",
            "video game",
        ]
        L_sports = ["3", "3.", "Sports", "SPORTS", "sports", "Sport", "sport", "SPORT"]
        L_current_affairs = [
            "4",
            "4.",
            "Current Affairs",
            "Current affairs",
            "current affairs",
            "CURRENT AFFAIRS",
            "Current Affair",
            "Current affair",
            "current affair",
            "CURRENT AFFAIR",
        ]
        L_entertainment = ["5", "5.", "entertainment", "Entertainment", "ENTERTAINMENT"]
        L_topics = [L_tech, L_video_games, L_sports, L_current_affairs, L_entertainment]
        question_number = 0
        wrong_quiz = 0
        correct_quiz = 0

        print()
        print()
        print()

        questions_L_tech = [
            "Which social media app only lets you view pictures and messages for a limited time?",
            "What year did the first Apple iPhone launch?",
            "Created in 1990, what was the name of the first internet search engine?",
            "What is the name of Elon Musk's aerospace company?",
            "What is the name of the British computer scientist who invented the World Wide Web in 1989?",
            "What does LG stand for in LG Electronics?",
            "What technology is used to record cryptocurrency transactions?",
            "What kind of malware is designed to take advantage of a security hole before it is known?",
            "What does acronym FOSS stand for?",
            "What technology is used to make telephone calls over the Internet possible?",
            "Which computer language is the most widely used?",
        ]

        options_L_tech = [
            ["A)Whatsapp", "B)Snapchat", "C)Messenger", "D)Instagram"],
            ["A)2005", "B)1999", "C)2008", "D)2007"],
            ["A)Archie", "B)Google", "C)Yahoo", "D)Firefox"],
            ["A)Boeing", "B)SpaceX", "C)Nasa", "D)Space"],
            ["A)Tim Berners Lee", "B)Tim Cook", "C)Larry Page", "D)Elon Musk"],
            ["A)Lost and Gone", "B)Loop Goop", "C)Lock Glock", "D)Lucky-Goldstar"],
            ["A)Digital wallet", "B)Token", "C)Mining", "D)Blockchain"],
            ["A)Zero-day exploit", "B)Virus", "C)Ransomware", "D)Trojan horse"],
            [
                "A)Full Option Sensor System",
                "B)Follow-On Support Service",
                "C)Free and Open-Source Software",
                "D)Fiber Optics Science System",
            ],
            ["A)Bluetooth", "B)Ethernet", "C)NFC", "D)VoIP"],
            ["A)C#", "B)Python", "C)JavaScript", "D)HTML"],
        ]

        answers_L_tech = [
            ["B)Snapchat", "Snapchat", "B", "b", "2"],
            ["D)2007", "2007", "D", "d", "4"],
            ["A)Archie", "Archie", "A", "a", "1"],
            ["B)SpaceX", "SpaceX", "B", "b", "2"],
            ["A)Tim Berners Lee", "Tim Berners Lee", "A", "a", "1"],
            ["D)Lucky-Goldstar", "Lucky-Goldstar", "D", "d", "4"],
            ["D)Blockchain", "Blockchain", "d", "D", "4"],
            ["A)Zero-day exploit", "Zero-day exploit", "A", "a", "1"],
            [
                "C)Free and Open-Source Software",
                "Free and Open-Source Software",
                "c",
                "C",
                "3",
            ],
            ["D)VoIP", "VoIP", "D", "d", "4"],
            ["C)JavaScript", "JavaScript", "c", "C", "3"],
        ]

        questions_L_video_games = [
            "Who is the Most Famous Video Game Character of all Time?",
            "The playstation prototype was designed by sony in collaboration with which company?",
            'The classic arcade game "pong" was manufactured by which company',
            " Pokemon was originally released on which videogame console?",
            " What is the name of circular object that is used to collect a pokemon?",
            'How much money does the average player spend on the game "Fortnite"?',
            'What company developed the survival horror video game "The Last of Us Remastered"?',
            "Who is on the cover of the video game FIFA 18?",
            "Who is on the cover of the video game NBA 2K18?",
            'What state does "Far Cry 5" take place in?',
            'The video game "Assassins Creed Unity" is set primarily in what city during the French Revolution?',
            'Who is the last boss in "Street Fighter III"?',
            'What is the cult in "Far Cry 5" called?',
            'What decade does "A Way Out" take place?',
            "What is the best-selling video game of all time?",
        ]
        options_L_video_games = [
            ["A)Mario", "B)Franklin", "C)Lara Croft", "D)Kratos"],
            ["A)Sony", "B)Nintendo", "C)Atari", "Sega)"],
            ["A)Atari", "B)Microsoft", "C)Gameloft", "D)Rockstar Games"],
            ["A)WII", "B)XBOX", "C)PSP", "D)Gameboy"],
            ["A)Ball", "B)Pokeball", "C)Pokecatcher", "D)Grabber"],
            ["A)20$", "B)30$", "C)60$", "D)50$"],
            ["A)Sony", "B)Naughty Dog", "C)Gameloft", "D)UBISOFT"],
            ["A)Harry Kane", "B)Cristiano Ronaldo", "C)Neymar", "D)Benzema"],
            ["A)LeBron James", "B)JR Smith", "C)Paul George", "D)Kyrie Irving"],
            ["A)Oregon", "B)Colarado", "C)Montana", "D)Nevada"],
            ["A)Paris", "B)Nice", "C)Mareseille", "D)Lyon"],
            ["A)John", "B)Doughlas", "C)Gill", "D)Bill"],
            [
                "A)Project at Edens Gate",
                "B)Heavens Gate",
                "C)Manson Family",
                "D)Tree of Life",
            ],
            ["A)80s", "B)70s", "C)60s", "D)90s"],
            ["A)Halo", "B)Mario", "C)Flappy Bird", "D)Minecraft"],
        ]
        answers_L_video_games = [
            ["Mario", "mario", "A", "1"],
            ["Nintendo", "nintendo", "B", "2"],
            ["atari", "Atari", "A", "1"],
            ["Gameboy", "gameboy", "D", "4"],
            ["B", "Pokeball", "2", "pokeball"],
            ["C", "60", "c", "3"],
            ["Naughty Dog", "B", "2", "naughty dog"],
            ["B", "Cristiano Ronaldo", "ronaldo", "2"],
            ["D", "4", "Kyrie Irving", "kyrie irving"],
            ["C", "Montana", "montana", "3"],
            ["A", "Paris", "paris", "1"],
            ["C", "Gill", "3", "gill"],
            ["Project at Eden's Gate", "1", "a", "A"],
            ["B", "70s", "2", "b"],
            ["D", "d", "Minecraft", "4"],
        ]
        questions_L_sports = [
            "What are the five colours of the Olympic rings?",
            "In football,which team has won the Champions League (formerly the European Cup) the most?",
            "How many players are there in a rugby league team?",
            "When was the first recorded Olympics held?",
            "Which of the following country won Football world Cup maximum times?",
            "Which famous Uruguayan footballer has bitten his opponents 3 times while playing?",
            "What is the highest batting average in test Cricket?",
            "Which team has won the most world cups in cricket?",
            "Who has scored the most pts in basketball(NBA)?",
            "Which country in the world has won the hockey world cup most times?",
            "Which currently active footballer has received the most number of red cards?",
            "How many people are there in an official tug of war team?",
            "What is Usain Bolt's 100m world record time?",
            "Who has scored the most Premier League hat-tricks?",
        ]

        options_L_sports = [
            ["A)1", "B)2", "C)Blue,yellow,black,green and red", "D)4"],
            ["A)1", "B)Real Madrid", "C)3", "D)4"],
            ["A)1", "B)2", "C)3", "D)13"],
            ["A)1", "B)776 BC", "C)3", "D)4"],
            ["A)Germany", "B)Italy", "C)Argentina", "D)Brazil"],
            ["A)Luis Suarez", "B)2", "C)3", "D)4"],
            ["A)115.63", "B)99.94", "C)75.89", "D)66.14"],
            ["A)West Indies", "B)Sri Lanka", "C)Australia", "D)India"],
            [
                "A)Kobe Bryant",
                "B)Michael Jordan",
                "C)Kareem Abdul Jabbar",
                "D)LeBron James",
            ],
            ["A)India", "B)Australia", "C)Belgium", "D)Pakistan"],
            [
                "A)Zlatan Ibrahimovic",
                "B)Sergio Ramos",
                "C)Mario Balotelli",
                "D)Cristiano Ronaldo",
            ],
            ["A)6", "B)7", "C)8", "D)10"],
            ["A)10.05", "B)9.47", "C)9.58", "D)9.86"],
            ["A)Harry Kane", "B)Thierry Henry", "C)Sergio Aguero", "D)Wayne Rooney"],
        ]

        answers_L_sports = [
            [
                "C)Blue,yellow,black,green and red",
                "Blue,yellow,black,green and red",
                "C",
                "c",
                "3",
            ],
            ["B)Real Madrid", "Real Madrid", "B", "b", "2"],
            ["D)13", "13", "D", "d", "4"],
            ["B)776 BC", "776 BC", "B", "b", "2"],
            ["D)Brazil", "Brazil", "D", "d", "4"],
            ["A)Luis Suarez", "Luis Suarez", "A", "a", "1"],
            ["B)99.94", "99.94", "B", "b", "2"],
            ["C)Australia", "Australia", "C", "c", "3"],
            ["C)Kareem Abdul Jabbar", "Kareem Abdul Jabbar", "C", "c", "3"],
            ["D)Pakistan", "Pakistan", "D", "d", "4"],
            ["B)Sergio Ramos", "Sergio Ramos", "B", "b", "2"],
            ["C)8", "8", "C", "c", "3"],
            ["C)9.58", "9.58", "C", "c", "3"],
            ["C)Sergio Aguero", "Sergio Aguero", "C", "c", "3"],
        ]

        questions_L_entertainment = [
            "Who has the most Oscars for acting?",
            "Who is the richest actor in the world?",
            "Who is the richest female actor in the world?",
            "What actor/actress has acted in the most number of movies?",
            "What is the maximum number of songs in a movie?",
            "Aishwarya Rai was crowned Miss World in which year?",
            "Who is known as the father of Indian Cinema?",
            "Which is the Highest-grossing film as of 2020?",
            "Which is the most watched tv show of all time?",
            "Which among these TV shows has the most number of episodes?",
            "Who is the first indian movie star to be featured on the cover of Time magazine?",
            "Which is the most sold non-religious book in the world?",
            "Which is the most liked Indian song on Youtube?",
        ]

        options_L_entertainment = [
            [
                "A)Joaquin Phoenix",
                "B)Sean Penn",
                "C)Katharine Hepburn",
                "D)Jeff Bridges",
            ],
            ["A)Paul Rudd", "B)SRK", "C)Tom Cruise", "D)Joaquin Phoenix"],
            ["A)", "B)", "C)Oprah Winfrey", "D)Jessica Alba"],
            [
                "A)Kanneganti Brahmanandam",
                "B)Keerthy Suresh",
                "C)Nithya Menen",
                "D)Anushka Shetty",
            ],
            ["A)32", "B)76", "C)34", "D)72"],
            ["A)1989", "B)1994", "C)1999", "D)2003"],
            [
                "A)Dadasaheb Phalke",
                "B)V. Shantaram",
                "C)Dadasaheb Torne",
                "D)Satyajit Ray",
            ],
            [
                "A)Avatar",
                "B)Titanic",
                "C)Avengers: Endgame",
                "D)Baahubali : The Conclusion",
            ],
            [
                "A)Stranger Things",
                "B)F.R.I.E.N.D.S",
                "C)Game Of Thrones",
                "D)13 Reasons Why",
            ],
            [
                "A)CID",
                "B)Crime Patrol",
                "C)Taarak Mehta Ka Ooltah Chashmah",
                "D)Yeh Rishta Kya Kehlata Hai",
            ],
            ["A)Amir Khan", "B)Zeenat Aman", "C)Aishwarya Rai", "D)Parveen Babi"],
            [
                "A)A Tale of Two Cities",
                "B)The Hobbit",
                "C)Harry Potter and the Philosopher's Stone",
                "D)The Da Vinci Code",
            ],
            ["A)Vaaste", "B)Filhall", "C)Yalgaar", "D)Lehanga"],
        ]

        answers_L_entertainment = [
            [
                "C)Katharine Hepburn",
                "ckatharinehepburn",
                "katharinehepburn",
                "c",
                "3",
                "3katharinehepburn",
            ],
            ["B)SRK", "bsrk", "srk", "b", "2", "2srk"],
            [
                "C)Oprah Winfrey",
                "coprahwinfrey",
                "oprahwinfrey",
                "c",
                "3",
                "3oprahwinfrey",
            ],
            [
                "A)Kanneganti Brahmanandam",
                "akannegantibrahmanandam",
                "kannegantibrahmanandam",
                "a",
                "1",
                "1kannegantibrahmanandam",
            ],
            ["D)72", "d72", "72", "d", "4", "472"],
            ["B)1994", "b1994", "B", "b", "2", "21994"],
            [
                "A)Dadasaheb Phalke",
                "adadasahebphalke",
                "dadasahebphalke",
                "a",
                "1",
                "1dadasahebphalke",
            ],
            [
                "A)Avengers: Endgame",
                "cavengersendgame",
                "avengersendgame",
                "c",
                "3",
                "3avengersendgame",
            ],
            [
                "C)Game Of Thrones",
                "cgameofthrones",
                "gameofthrones",
                "c",
                "3",
                "3gameofthrones",
            ],
            [
                "D)Yeh Rishta Kya Kehlata Hai",
                "dyehrishtakyakehlatahai",
                "yehrishtakyakehlatahai",
                "d",
                "4",
                "4yehrishtakyakehlatahai",
            ],
            ["D)Parveen Babi", "dparveenbabi", "parveenbabi", "d", "4", "4parveenbabi"],
            [
                "A)A Tale of Two Cities",
                "aataleoftwocities",
                "ataleoftwocities",
                "a",
                "1",
                "1",
                "1ataleoftwocities",
            ],
            ["C)Yalgaar", "cyalgaar", "yalgaar", "c", "3", "3yalgaar"],
        ]

        questions_L_custom_1p = []

        answers_L_custom_1p = []

        options_L_custom_1p = []

        # except index 0 make all lower case and see the possibilities of symbols and a/1,b/2, i.e. nos. also

        questions_quiz = [
            questions_L_tech,
            questions_L_video_games,
            questions_L_sports,
            questions_L_entertainment,
        ]

        options_quiz = [
            options_L_tech,
            options_L_video_games,
            options_L_sports,
            options_L_entertainment,
        ]

        answers_quiz = [
            answers_L_tech,
            answers_L_video_games,
            answers_L_sports,
            answers_L_entertainment,
        ]

        fun_facts_quiz = []

        expert_advice_quiz = []

        seconds = 3

        def prequestion_timer():
            for i in range(seconds):
                print("Question Coming in  " + str(seconds - i) + "  seconds.")
                time.sleep(1)

        L_lifeline_name = ["lifeline", "lifelines", "hint", "hints", "help"]

        L_lifeline = [
            ["1)50-50", "50-50", "1", "1.", "1)", "50 50"],
            ["2)Double Dip", "double dip", "2", "2.", "2)", "doubledip"],
            ["3)Switch The Question", "switch the question", "3", "3.", "3)"],
            ["Dl"],
        ]

        L_lifelines_left = ["1)50-50", "2)Double Dip", "3)Switch The Question"]

        playagain_quiz = "yes"
        while playagain_quiz == "yes":
            print()

            L_1p = ["1", "1p", "1 player", "one", "one p", "one player"]
            #            L_2p = ['2', '2p', '2 player', 'two', 'two p', 'two player']
            #            no_of_players_quiz = input("Choose the number of Players:   1 Player     or     2 Player :  ").lower()
            no_of_players_quiz = "1"
            print()
            print()
            quiz_start = "yes"

            while quiz_start in yes:

                """One Player Modes Startes               One Player Modes Startes               One Player Modes Startes               One Player Modes Startes               One Player Modes Startes
                One Player Modes Startes               One Player Modes Startes               One Player Modes Startes               One Player Modes Startes               One Player Modes Startes
                One Player Modes Startes               One Player Modes Startes               One Player Modes Startes               One Player Modes Startes               One Player Modes Startes
                One Player Modes Startes               One Player Modes Startes               One Player Modes Startes               One Player Modes Startes               One Player Modes Startes"""

                if no_of_players_quiz in L_1p:

                    quiz_1p_modes_user_input = input(
                        """You can choose any mode from the following : 

                                            1)Normal Mode(Questions Based on your preferred Topic)
                                            2)Master Mode(Random Questions from any topic
                                            3)Custom Mode(Customize the topics, no. of questions, etc)
                                            4)KBC Mode

What Would You Like To Choose :   """
                    )

                    L_quiz_1p_mode_1 = [
                        "1)Normal Mode",
                        "1",
                        "1) Normal",
                        "1) Normal Mode",
                        "Normal Mode",
                        "1 Normal Mode",
                    ]
                    L_quiz_1p_mode_2 = [
                        "2)Master Mode",
                        "2",
                        "2) Master",
                        "2) Master Mode",
                        "Master Mode",
                        "1 Master Mode",
                    ]
                    L_quiz_1p_mode_3 = [
                        "3)Custom Mode",
                        "3",
                        "3) Custom",
                        "3) Custom Mode",
                        "Custom Mode",
                        "3 Custom Mode",
                    ]
                    L_quiz_1p_mode_4 = [
                        "4)KBC Mode",
                        "4",
                        "4) KBC",
                        "4) KBC Mode",
                        "KBC Mode",
                        "4 KBC Mode",
                    ]

                    quiz_1p_mode_3_topic_indexes = []

                    if quiz_1p_modes_user_input in L_quiz_1p_mode_1:

                        print()
                        quiz_1p_modes_user_input_mode1_rules = """
                                                You Chose Normal Mode(1 Player)

                                                INSTRUCTIONS : 

                                                1)You will get 5/10 questions based On your Choice.
                                                2)You will also get few Lifelines which you can use when stuck at any question
                                                3)To use Lifeline Type Lifeline, or Help"""

                        print()
                        quiz_1p_modes_user_input_mode1_run = "yes"
                        while quiz_1p_modes_user_input_mode1_run in yes:
                            print()

                            print(
                                """You can choose from these topics:

                                                                        1. Tech
                                                                        2. Video games
                                                                        3. Sports
                                                                        4. Current Affairs
                                                                        5. Entertainment
                                                                    """
                            )
                            print()
                            quiz_topic_input = input("Enter your preferred topic: ")

                            print()

                            quiz_topic_input_final = ""
                            for remove_extra_1 in quiz_topic_input:
                                if remove_extra_1.isalnum():
                                    quiz_topic_input_final = (
                                        quiz_topic_input_final + remove_extra_1
                                    ).lower()

                            quiz_topic_index = ""
                            for i in range(5):
                                if quiz_topic_input_final in L_topics[i]:
                                    quiz_topic_index = int(i)

                            if quiz_topic_index == "":
                                quiz_topic_index = -1
                                print("Topic Not Found")
                                print()

                            else:
                                quiz_1p_modes_user_input_mode1_run = "no"

                        quiz_1p_modes_user_input_mode1_run = "yes"
                        while quiz_1p_modes_user_input_mode1_run in yes:

                            L_short_quiz = ["Short Quiz(5 Q)", "short", "5"]
                            L_long_quiz = ["Long Quiz(10 Q)", "long", "10"]
                            print(quiz_1p_modes_user_input_mode1_rules)
                            print()
                            quiz_1p_mode_1_length_input = input(
                                """Would you like to play Short Quiz(5 questions) Or Long Quiz(10 Questions) :  """
                            ).lower()
                            print()

                            if quiz_1p_mode_1_length_input in L_short_quiz:

                                quiz_1p_mode_1_length = 5
                                print(f"You Chose {L_short_quiz[0]}")
                                quiz_1p_modes_user_input_mode1_run = "no"
                            elif quiz_1p_mode_1_length_input in L_long_quiz:
                                quiz_1p_mode_1_length = 10
                                print(f"You Chose {L_long_quiz[0]}")
                                quiz_1p_modes_user_input_mode1_run = "no"
                            else:
                                print("Wrong input")
                                quiz_1p_mode_1_length = 0

                    elif quiz_1p_modes_user_input in L_quiz_1p_mode_2:
                        # anything except 0, reason below few lines in condition of while loop
                        quiz_1p_mode_1_length = -2
                        print()
                        print(
                            """
                                                You Chose Master Mode(1 Player)

                                                INSTRUCTIONS : 

                                                1)You will get 5/10 questions based On your Choice.
                                                2)You will also get few Lifelines which you can use when stuck at any question
                                                3)To use Lifeline Type Lifeline, or Help"""
                        )

                        print()
                        # any values except the ones present(0-5)
                        quiz_topic_index = -2

                        quiz_1p_modes_user_input_mode2_run = "yes"
                        while quiz_1p_modes_user_input_mode2_run in yes:
                            quiz_1p_mode_2_length_input = input(
                                "How many questions Do you want(Write any number upto 25 :  "
                            )
                            print()

                            quiz_1p_mode_2_length_input_isalpha = ""

                            for remove_extra_5 in quiz_1p_mode_2_length_input:
                                if remove_extra_5.isalpha():
                                    quiz_1p_mode_2_length_input_isalpha = (
                                        quiz_1p_mode_2_length_input_isalpha
                                        + remove_extra_5
                                    ).lower()

                            quiz_1p_mode_2_length_input_isspace = ""
                            for remove_extra_5 in quiz_1p_mode_2_length_input:
                                if remove_extra_5.isspace():
                                    quiz_1p_mode_2_length_input_isspace = (
                                        quiz_1p_mode_2_length_input_isspace
                                        + remove_extra_5
                                    ).lower()

                            quiz_1p_mode_2_length_input_final = ""
                            for remove_extra_5 in quiz_1p_mode_2_length_input:
                                if remove_extra_5.isdigit():
                                    quiz_1p_mode_2_length_input_final = int(
                                        (
                                            quiz_1p_mode_2_length_input_final
                                            + remove_extra_5
                                        ).lower()
                                    )
                                # add str in len statements in case of error
                                if (
                                    len(quiz_1p_mode_2_length_input)
                                    - len(str(quiz_1p_mode_2_length_input_final))
                                    - len(quiz_1p_mode_2_length_input_isspace)
                                    > 0
                                ):
                                    quiz_topic_input_custom_mode2_final_confirm = input(
                                        f"Do you mean {quiz_1p_mode_2_length_input_final} Questions?"
                                    )
                                    if (
                                        quiz_topic_input_custom_mode2_final_confirm
                                        in yes
                                    ):
                                        quiz_1p_modes_user_input_mode2_run = "no"
                                else:
                                    print(
                                        f"You Chose {quiz_1p_mode_2_length_input_final} Questions"
                                    )
                                    print("yfhgvhjgjh")
                                    quiz_1p_modes_user_input_mode2_run = "no"
                                    print()

                    elif quiz_1p_modes_user_input in L_quiz_1p_mode_3:
                        # anything except 0, reason below few lines in condition of while loop
                        quiz_1p_mode_1_length = -2

                        print()
                        print(
                            """
                                                You Chose Custom Mode(1 Player)

                                                INSTRUCTIONS : 

                                                1)You can choose any number of topics from the list
                                                2)You can choose upto 10 questions per topic, so if you chose 2 topics, you can get upto 20 Questions, as per your selection
                                                2)You will also get few Lifelines which you can use when stuck at any question
                                                3)To use Lifeline Type Lifeline, or Help"""
                        )

                        print()
                        quiz_1p_modes_user_input_mode3_run = "yes"
                        while quiz_1p_modes_user_input_mode3_run in yes:
                            print(
                                """Choose any number of topics from the list provided : 
                                                                                    1. Tech
                                                                                    2. Video games
                                                                                    3. Sports
                                                                                    4. Current Affairs
                                                                                    5. Entertainment
                                            """
                            )

                            quiz_1p_mode_3_topic_input_yesno = "yes"

                            quiz_1p_modes_user_input_mode3_run = "yes"
                            while quiz_1p_modes_user_input_mode3_run in yes:

                                if quiz_1p_mode_3_topic_input_yesno in yes:
                                    quiz_topic_input_custom_mode3 = input(
                                        "Which one would you like to choose :  "
                                    )

                                    print()
                                    print()

                                    quiz_topic_input_custom_mode3_final = ""
                                    for remove_extra_4 in quiz_topic_input_custom_mode3:
                                        if remove_extra_4.isalnum():
                                            quiz_topic_input_custom_mode3_final = (
                                                quiz_topic_input_custom_mode3_final
                                                + remove_extra_4
                                            ).lower()

                                    quiz_topic_index = ""
                                    for i in range(5):
                                        if (
                                            quiz_topic_input_custom_mode3_final
                                            in L_topics[i]
                                        ):
                                            quiz_topic_index = int(i)
                                            quiz_1p_mode_3_topic_indexes.append(
                                                quiz_topic_index
                                            )
                                            break

                                    if quiz_topic_index == "":
                                        print("Topic Not Found")
                                    """else:
                                        #print(f'You Chose {L_topics[quiz_topic_index]}')"""
                                    print()
                                    quiz_1p_mode_3_topic_input_yesno = input(
                                        "Do you want to Choose another topic? :  "
                                    )
                                    print()

                                else:
                                    if len(quiz_1p_mode_3_topic_indexes) == 0:
                                        print(
                                            "You have Chosen no topic. Do you want to quit the game? Choose again."
                                        )
                                    else:
                                        quiz_1p_modes_user_input_mode3_run = "no"
                                    print()

                        quiz_1p_modes_user_input_mode3_run = "yes"
                        quiz_1p_mode_3_length_input_isspace = 0
                        while quiz_1p_modes_user_input_mode3_run in yes:
                            quiz_1p_mode_3_length_input = input(
                                f"How many questions Do you want(Write any number upto {len(quiz_1p_mode_3_topic_indexes) * 10}) :  "
                            )
                            quiz_1p_mode_3_length_input_final = ""
                            while quiz_1p_modes_user_input_mode3_run in yes:
                                for remove_extra_6 in quiz_1p_mode_3_length_input:
                                    if remove_extra_6.isalpha():
                                        quiz_1p_mode_3_length_input_isalpha = (
                                            quiz_1p_mode_3_length_input_final
                                            + remove_extra_6
                                        ).lower()

                                for remove_extra_6 in quiz_1p_mode_3_length_input:
                                    if remove_extra_6.isspace():
                                        quiz_1p_mode_3_length_input_isspace = (
                                            quiz_1p_mode_3_length_input_final
                                            + remove_extra_6
                                        ).lower()

                                for remove_extra_6 in quiz_1p_mode_3_length_input:
                                    if remove_extra_6.isdigit():
                                        quiz_1p_mode_3_length_input_final = int(
                                            (
                                                str(quiz_1p_mode_3_length_input_final)
                                                + str(remove_extra_6)
                                            ).lower()
                                        )

                                if (
                                    len(str(quiz_1p_mode_3_length_input))
                                    - len(str(quiz_1p_mode_3_length_input_final))
                                    - len(str(quiz_1p_mode_3_length_input_isspace))
                                    > 0
                                ):
                                    quiz_topic_input_custom_mode3_final_confirm = input(
                                        f"Do you mean {quiz_topic_input_custom_mode3_final} Questions?"
                                    )
                                    if (
                                        quiz_topic_input_custom_mode3_final_confirm
                                        in yes
                                    ):
                                        quiz_1p_modes_user_input_mode3_run = "no"
                                        break
                                else:
                                    print(
                                        f"You Chose {quiz_1p_mode_3_length_input_final} Questions"
                                    )
                                    quiz_1p_modes_user_input_mode3_run = "no"

                    elif quiz_1p_modes_user_input in L_quiz_1p_mode_4:

                        if quiz_1p_modes_user_input not in L_quiz_1p_mode_3:
                            quiz_1p_mode_3_topic_indexes = [-5]
                    while (
                        quiz_topic_index != -1
                        and quiz_1p_mode_1_length != 0
                        and len(quiz_1p_mode_3_topic_indexes) != 0
                    ):

                        print()
                        print()

                        if quiz_1p_modes_user_input in L_quiz_1p_mode_2:
                            quiz_topic_index = random.randint(0, 4)
                            while len(questions_quiz[quiz_topic_index]) == 0:
                                quiz_topic_index = random.randint(0, 4)
                        elif quiz_1p_modes_user_input in L_quiz_1p_mode_3:
                            quiz_topic_index = random.choice(
                                quiz_1p_mode_3_topic_indexes
                            )

                        question_random_choice = random.choice(
                            questions_quiz[quiz_topic_index]
                        )
                        question_index = questions_quiz[quiz_topic_index].index(
                            question_random_choice
                        )

                        print()
                        print()

                        prequestion_timer()

                        print()
                        print()

                        question_number += 1
                        print(f"Q{question_number}) {question_random_choice}")
                        print()
                        print(*options_quiz[quiz_topic_index][question_index], sep="\t")
                        print()
                        answer_input = input("Enter your answer: ")
                        answer_input_final = ""

                        for remove_extra_2 in answer_input:
                            if remove_extra_2.isalnum():
                                answer_input_final = (
                                    answer_input_final + remove_extra_2
                                ).lower()

                        if (
                            answer_input_final
                            in answers_quiz[quiz_topic_index][question_index]
                        ):  # .lower() problem in list
                            print()
                            print("Good Your Answer is correct")
                            time.sleep(0.5)
                            correct_quiz += 1

                        elif answer_input_final in L_lifeline_name:

                            print("You have the following Lifelines  :  ")
                            print()
                            print(*L_lifelines_left, sep="\n")

                            print()

                            lifeline_input = input(
                                "Which one would you like to choose :  "
                            )

                            print()

                            lifeline_input_final = ""

                            for remove_extra_3 in lifeline_input:
                                if remove_extra_3.isalnum():
                                    lifeline_input_final = (
                                        lifeline_input_final + remove_extra_3
                                    ).lower()

                            if lifeline_input_final in L_lifeline[0]:
                                print(
                                    "You have chosen 50-50. 2 options would be removed. Choose One from the remaining"
                                )
                                i = 0

                                L_lifelines_left.remove(
                                    L_lifelines_left[L_lifelines_left.index("1)50-50")]
                                )
                                L_lifeline[0] = []

                                while i < 2:
                                    remove_option_index = options_quiz[
                                        quiz_topic_index
                                    ][question_index].index(
                                        random.choice(
                                            options_quiz[quiz_topic_index][
                                                question_index
                                            ]
                                        )
                                    )

                                    if (
                                        options_quiz[quiz_topic_index][question_index][
                                            remove_option_index
                                        ]
                                        not in answers_quiz[quiz_topic_index][
                                            question_index
                                        ]
                                    ):
                                        options_quiz[quiz_topic_index][
                                            question_index
                                        ].remove(
                                            options_quiz[quiz_topic_index][
                                                question_index
                                            ][remove_option_index]
                                        )
                                        i = i + 1

                                print(f"Q{question_number}) {question_random_choice}")
                                print()
                                print(
                                    *options_quiz[quiz_topic_index][question_index],
                                    sep="\t",
                                )
                                print()
                                answer_input = input("Enter your answer: ")
                                answer_input_final = ""
                                for remove in answer_input:
                                    if remove.isalnum():
                                        answer_input_final = (
                                            answer_input_final + remove
                                        ).lower()

                                if (
                                    answer_input_final
                                    in answers_quiz[quiz_topic_index][question_index]
                                ):
                                    print()
                                    print("Good Your Answer is correct")
                                    time.sleep(0.5)
                                    correct_quiz += 1
                                else:
                                    print()
                                    print("Wrong Answer")
                                    time.sleep(0.5)
                                    wrong_quiz += 1
                                    print(
                                        f"Correct answer was : {answers_quiz[quiz_topic_index][question_index][0]}"
                                    )
                            #                        lifeline_left+=1

                            elif lifeline_input_final in L_lifeline[1]:
                                L_lifelines_left.remove(
                                    L_lifelines_left[
                                        L_lifelines_left.index("2)Double Dip")
                                    ]
                                )
                                L_lifeline[1] = []
                                print("You have chosen Double Dip")
                                y = 0
                                tries_left = 2
                                while y < 2:
                                    print(
                                        f"Q{question_number}) {question_random_choice}"
                                    )
                                    print()
                                    print(
                                        *options_quiz[quiz_topic_index][question_index],
                                        sep="\t",
                                    )
                                    print()
                                    answer_input = input(
                                        f"Enter your answer (Tries left = {tries_left}) :  "
                                    )
                                    answer_input_final = ""
                                    for remove in answer_input:
                                        if remove.isalnum():
                                            answer_input_final = (
                                                answer_input_final + remove
                                            ).lower()

                                    if (
                                        answer_input_final
                                        in answers_quiz[quiz_topic_index][
                                            question_index
                                        ]
                                    ):
                                        print()
                                        print("Good Your Answer is correct")
                                        time.sleep(0.5)

                                        y = 2

                                    else:
                                        print()
                                        print("Wrong Answer")
                                        time.sleep(0.5)
                                        y += 1
                                    tries_left -= 1

                                    # Remove wrong option                                wrong_answer_remove_index_double_dip=options_quiz[quiz_topic_index][question_index].index(answer_input)
                                    #                                options_quiz[quiz_topic_index][question_index].remove(options_quiz[quiz_topic_index][question_index][wrong_answer_remove_index_double_dip])

                                    if y == 2:
                                        print(
                                            f"Correct answer was : {answers_quiz[quiz_topic_index][question_index][0]}"
                                        )
                                        wrong_quiz += 1

                            elif lifeline_input_final in L_lifeline[2]:
                                L_lifelines_left.remove(
                                    L_lifelines_left[
                                        L_lifelines_left.index("3)Switch The Question")
                                    ]
                                )
                                L_lifeline[2] = []
                                print("You chose Switch the questiom")
                                question_number -= 1

                            else:
                                print("Wrong input, No such LIFELINE FOUND ")
                                question_number -= 1

                        else:
                            print()

                            print("Wrong Answer")
                            time.sleep(0.5)
                            wrong_quiz += 1
                            print(
                                f"Correct answer was : {answers_quiz[quiz_topic_index][question_index][0]}"
                            )

                        questions_quiz[quiz_topic_index].remove(question_random_choice)
                        answers_quiz[quiz_topic_index].remove(
                            answers_quiz[quiz_topic_index][question_index]
                        )
                        options_quiz[quiz_topic_index].remove(
                            options_quiz[quiz_topic_index][question_index]
                        )

                        if (
                            quiz_1p_modes_user_input in L_quiz_1p_mode_1
                            and question_number == quiz_1p_mode_1_length
                        ):
                            print()

                            print("Thanks for playing")
                            print(
                                f"You had {correct_quiz} answers correct and {wrong_quiz} answers wrong."
                            )

                            break

                        elif (
                            quiz_1p_modes_user_input in L_quiz_1p_mode_2
                            and question_number == quiz_1p_mode_2_length_input_final
                        ):
                            print()

                            print("Thanks for playing")
                            print(
                                f"You had {correct_quiz} answers correct and {wrong_quiz} answers wrong."
                            )

                            break

                        elif (
                            quiz_1p_modes_user_input in L_quiz_1p_mode_3
                            and question_number == quiz_1p_mode_3_length_input_final
                        ):
                            print()

                            print("Thanks for playing")
                            print(
                                f"You had {correct_quiz} answers correct and {wrong_quiz} answers wrong."
                            )

                            break

                else:
                    break
            #   if quiz_1p_modes_user_input in L_quiz_1p_mode_2:    mode 3 also done in 1st only              #  done in 1st one only

            #   if quiz_1p_modes_user_input in L_quiz_1p_mode_4:
