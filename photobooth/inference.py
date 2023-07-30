import torch
from diffusers import DiffusionPipeline

model_dir = "output"
pipe = DiffusionPipeline.from_pretrained(model_dir)

prompt = "A photo of jung in a bucket"
image = pipe(prompt, num_inference_steps=50, guidance_scale=7.5).images[0]

image.save("test.png")
