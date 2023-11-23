while True:
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")

    comb_name = name1 + name2

    t_occur = comb_name.count("t")
    r_occur = comb_name.count("r")
    u_occur = comb_name.count("u")
    e_occur = comb_name.count("e")

    true_occur = t_occur + r_occur + u_occur + e_occur

    l_occur = comb_name.count("l")
    o_occur = comb_name.count("o")
    v_occur = comb_name.count("v")
    e_occur = comb_name.count("e")

    love_occur = l_occur + o_occur + v_occur + e_occur

    lv_final = true_occur + love_occur

    final_score = int(str(true_occur) + str(love_occur))

    if final_score < 10 or final_score > 90:
        print(f"Your score is {final_score},you go together like coke and mentos.")
    elif 40 < final_score < 50:
        print(f"Your score is {final_score}, you are alright together.")
    else:
        print(f"Your score is {final_score}")

    out = input("If you want to continue please enter any key or 'q' for exit.")
    if out == 'q':
        break
    else:
        continue
