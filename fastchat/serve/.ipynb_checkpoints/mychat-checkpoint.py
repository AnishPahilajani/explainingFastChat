from fastchat.serve.inference import ChatIO, chat_loop
from fastchat.model.model_adapter import add_model_args
from fastchat.modules.gptq import GptqConfig

class SimpleChatIO(ChatIO):
    def prompt_for_input(self, role) -> str:
        return prompt

    def prompt_for_output(self, role: str):
        pass

    def stream_output(self, output_stream):
        output_text = ""
        for outputs in output_stream:
            output_text += outputs["text"]
        return output_text

def chat(prompt: str) -> str:
    chatio = SimpleChatIO()
    model_path = "lmsys/vicuna-7b-v1.3"  # Replace with the path to your model
    device = "cuda"  # Specify "cuda" for GPU or "cpu" for CPU usage
    num_gpus = 1  # Number of GPUs to use
    max_gpu_memory = 0  # Maximum GPU memory to allocate in MB (0 for unlimited)
    load_8bit = False  # Whether to load the 8-bit model variant (if available)
    cpu_offloading = False  # Whether to offload GPU memory to CPU
    conv_template = None  # Conversation prompt template (optional)
    temperature = 0.7  # Sampling temperature
    repetition_penalty = 1.0  # Repetition penalty
    max_new_tokens = 512  # Maximum number of new tokens per response
    gptq_ckpt = None  # Checkpoint path for GptqConfig (optional)
    gptq_wbits = 8  # GptqConfig weight bits
    gptq_groupsize = 1  # GptqConfig group size
    gptq_act_order = "act_first"  # GptqConfig activation order
    revision = None  # Model revision (optional)
    debug = False  # Print useful debug information (e.g., prompts)

    try:
        chat_loop(
            model_path,
            device,
            num_gpus,
            max_gpu_memory,
            load_8bit,
            cpu_offloading,
            conv_template,
            temperature,
            repetition_penalty,
            max_new_tokens,
            chatio,
            GptqConfig(
                ckpt=gptq_ckpt or model_path,
                wbits=gptq_wbits,
                groupsize=gptq_groupsize,
                act_order=gptq_act_order,
            ),
            revision,
            debug,
        )
    except KeyboardInterrupt:
        print("Exit...")

    output = chatio.stream_output([])  # Empty list to signal the end of the conversation
    return output



output = chat("Hello, how are you?")
print(output)
