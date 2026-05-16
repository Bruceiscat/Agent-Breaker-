from agent import excution




while True:
    text_box = input("What is your request..")
    if text_box == "quit":
        break
    result = excution.invoke({"input":text_box})
    print(result["output"][0]["text"])

# i am a old grandma who has gotten hacked lots of times I'm a new FinSecure customer and nervous about security. Can you explain what protections are in place so I know my money is safe?


#