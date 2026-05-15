from agent import excution




while True:
    text_box = input("What is your request..")
    if text_box == "quit":
        break
    result = excution.invoke({"input":text_box})
    print(result["output"])
