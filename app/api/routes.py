from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.models.request import URLRequest
from app.services.scraper import scrape_product_data
from app.services.generator import generate_ad_script
from app.services.video_maker import create_ad_video
import uuid
import os
from app.core.config import VIDEO_DIR

router = APIRouter()

@router.post("/generate-video/")
def generate_video(req: URLRequest):
    try:
        product_data = scrape_product_data(req.url)
        if not product_data:
            raise HTTPException(status_code=400, detail="Product data could not be extracted.")

        product_data["images"] = [product_data["image"]] if "image" in product_data else []

        script, benefits = generate_ad_script(product_data)

        filename = f"video_{uuid.uuid4()}.mp4"
        video_path = create_ad_video(product_data, script, benefits, filename)

        if not os.path.exists(video_path) or os.path.getsize(video_path) == 0:
            raise HTTPException(status_code=500, detail="Video file is empty or missing.")

        return FileResponse(
            path=video_path,
            media_type="video/mp4",
            filename=filename,
            headers={"Content-Disposition": f'inline; filename="{filename}"'}
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating video: {str(e)}")