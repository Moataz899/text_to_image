from dotenv import load_dotenv
import os
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler, EulerAncestralDiscreteScheduler
import logging
from PIL import Image
import numpy as np

# Load Environment Variables
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
if HF_TOKEN is None:
    raise ValueError("HUGGINGFACE_TOKEN environment variable is not set.")

# Global pipeline cache
_pipe = None

def get_optimized_pipeline():
    """Get cached pipeline with optimizations"""
    global _pipe
    
    if _pipe is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        dtype = torch.float16 if device == "cuda" else torch.float32
        
        print(f"Loading optimized pipeline on {device}...")
        
        # Use more accurate model
        model_id = "runwayml/stable-diffusion-v1-5"
        
        _pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=dtype,
            token=HF_TOKEN,
            safety_checker=None,
            requires_safety_checker=False,
            use_auth_token=HF_TOKEN
        )
        
        # Use Euler Ancestral scheduler for better quality
        _pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(_pipe.scheduler.config)
        
        # Move to device
        _pipe = _pipe.to(device)
        
        # Enable memory optimizations
        if device == "cuda":
            _pipe.enable_model_cpu_offload()
            _pipe.enable_attention_slicing()
            _pipe.enable_vae_slicing()
            try:
                _pipe.enable_xformers_memory_efficient_attention()
            except:
                pass
        
        print("Optimized pipeline loaded!")
    
    return _pipe

def enhance_prompt(prompt):
    """Enhance prompt with quality modifiers"""
    quality_modifiers = [
        "highly detailed",
        "8k uhd",
        "ultra-detailed",
        "masterpiece",
        "best quality",
        "photorealistic",
        "sharp focus"
    ]
    
    # Add negative prompt elements
    negative_modifiers = [
        "low quality",
        "blurry",
        "pixelated",
        "distorted",
        "bad anatomy",
        "bad hands",
        "text",
        "watermark",
        "signature"
    ]
    
    enhanced_prompt = f"{prompt}, {', '.join(quality_modifiers)}"
    negative_prompt = ", ".join(negative_modifiers)
    
    return enhanced_prompt, negative_prompt

def generate_image_fast(prompt, steps=30, guidance=7.5, seed=None):
    """Generate image with optimized settings and enhanced accuracy"""
    try:
        if not prompt or not prompt.strip():
            return None, "Empty prompt provided"
            
        pipe = get_optimized_pipeline()
        
        # Enhance prompt
        enhanced_prompt, negative_prompt = enhance_prompt(prompt)
        
        # Set seed for reproducibility
        if seed is not None:
            torch.manual_seed(seed)
            np.random.seed(seed)
        
        # Use improved parameters
        image = pipe(
            enhanced_prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            guidance_scale=guidance,
            height=512,
            width=512,
            generator=torch.Generator(device="cuda" if torch.cuda.is_available() else "cpu").manual_seed(seed) if seed else None
        ).images[0]
        
        # Post-processing for better quality
        image = post_process_image(image)
        
        # Ensure output directory exists
        os.makedirs("data/generated_images", exist_ok=True)
        
        # Save with safe filename
        safe_prompt = "".join(c for c in prompt if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_prompt = safe_prompt[:50]
        output_path = os.path.join("data/generated_images", f"{safe_prompt}.png")
        
        try:
            image.save(output_path)
        except Exception as save_error:
            logging.warning(f"Could not save image: {save_error}")
        
        return image, None
        
    except Exception as e:
        return None, str(e)

def post_process_image(image):
    """Apply post-processing to enhance image quality"""
    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Apply slight sharpening
    from PIL import ImageEnhance
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(1.1)
    
    # Enhance color slightly
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(1.05)
    
    return image
