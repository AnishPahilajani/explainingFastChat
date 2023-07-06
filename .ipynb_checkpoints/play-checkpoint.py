from fastchat.serve.mychat import interact_with_model

# Call the function and pass in the prompt
prompt = "Hello, how are you?"
response = interact_with_model(prompt)

# Print the generated response
print(response)
