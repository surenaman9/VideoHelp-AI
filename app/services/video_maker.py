from moviepy.editor import TextClip, ImageClip, concatenate_videoclips
from moviepy.video.fx.all import resize
from PIL import Image
from io import BytesIO
import requests
import numpy as np
import os
from app.core.config import VIDEO_DIR

def create_ad_video(product, script, benefits, output_filename):
    try:
        image_url = product["images"][0] if product["images"] else None
        if not image_url:
            raise ValueError("No product image found.")

        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        img_array = np.array(img)

        img_clip = resize(ImageClip(img_array).set_duration(5), width=720)

        text_clips = [
            TextClip(product["title"], fontsize=40, color='white', bg_color='black', size=(720, 100)).set_duration(3),
            TextClip(script[:80], fontsize=30, color='white', bg_color='black', size=(720, 100)).set_duration(5)
        ]

        for b in benefits[:2]:
            text_clips.append(TextClip(b, fontsize=28, color='white', bg_color='black', size=(720, 80)).set_duration(2))

        final = concatenate_videoclips([img_clip] + text_clips, method="compose")

        os.makedirs(VIDEO_DIR, exist_ok=True)
        output_path = os.path.join(VIDEO_DIR, output_filename)
        final.write_videofile(output_path, fps=24, verbose=False, logger=None)

        return output_path

    except Exception as e:
        raise RuntimeError(f"Video creation failed: {str(e)}")