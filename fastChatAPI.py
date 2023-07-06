import subprocess

# Run the command
command = 'python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.3 --num-gpus 2'
print("Running command:", command)

# Start the process
process = subprocess.Popen(
    command,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE
)

# Function to send input and capture response
def send_input(input_data):
    process.stdin.write(input_data.encode())
    process.stdin.flush()
    response = process.stdout.readline().decode()
    print(response)

# Send initial input
send_input('hello\n')
send_input('who are you?\n')
send_input('can you tell me the sentiment of this text, "today is a good day" respond as a single word"\n')

# input_list = ['what can you do?\n', 'who are you?']

# # Continue sending input based on output
# for prompt in input_list:
#     # Provide more input based on previous output
#     send_input(prompt)

# # Wait for the process to finish
process.wait()
exit()






# WORKING
# import subprocess

# # Run the command
# command = 'python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.3 --num-gpus 2'
# print("Running command:", command)

# # Start the process
# process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

# # Function to send input to the process and capture output
# def send_input(input_data):
#     output, _ = process.communicate(input_data.encode())
#     output = output.decode()
#     print(output)

# # Send initial input
# input_data = 'hello\n'
# output = send_input(input_data)

# input_list = ['what can you do?\n', 'who are you?']

# # Continue sending input based on output
# for prompt in input_list:
#     # Provide more input based on previous output
#     print("YESSS")
#     send_input(prompt)

# Continue executing rest of the code
# ...



# import subprocess

# # Run the command
# command = 'python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.3 --num-gpus 2'
# print("Running command:", command)

# # Start the process
# process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

# # Send input to the process
# input_data = 'hello\n'
# output, _ = process.communicate(input_data.encode())

# # Decode and print the output
# output = output.decode()
# print(output)

# Continue executing rest of the code
# ...


# import openai
# openai.api_key = "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" # Not support yet
# openai.api_base = "http://localhost:8000/v1"

# model = "vicuna-7b-v1.3"
# prompt = "Once upon a time"

# # create a completion
# completion = openai.Completion.create(model=model, prompt=prompt, max_tokens=64)
# # print the completion
# print(prompt + completion.choices[0].text)

# # create a chat completion
# completion = openai.ChatCompletion.create(
#   model=model,
#   messages=[{"role": "user", "content": "Hello! What is your name?"}]
# )
# # print the completion
# print(completion.choices[0].message.content)