
is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall man")
elif not(is_male) and is_tall:
    print("You are a tall woman")
elif is_male and not(is_tall):
    print("You are a short man")
else:
    print("You are short woman")