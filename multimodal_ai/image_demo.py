import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("segmind/tiny-sd", torch_dtype=torch.float32)
image = pipe("A dog wearing sunglasses", num_inference_steps=8).images[0]

image.save("demo.png")
print("image generated and saved as demo.png")