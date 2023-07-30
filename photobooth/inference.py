import torch
from diffusers import DiffusionPipeline

model_dir_a = "output"
pipe = DiffusionPipeline.from_pretrained(model_dir_a, torch_dtype=torch.float16).to(
    "cuda"
)

while True:
    prompt = input("Prompt: ")
    pipe(prompt, num_inference_steps=50, guidance_scale=7.5).images[0].save(
        "sample.png"
    )
