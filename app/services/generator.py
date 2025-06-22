from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_ad_script(product):
    try:
        prompt = f"""
        Write a 20-second ad script for the following product:
        Title: {product['title']}
        Description: {product['description']}
        Features: {', '.join(product.get('features', []))}

        Also provide 3 short catchy benefits as bullet points.
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        output = response.choices[0].message.content.strip()
        parts = output.split("Benefits:")
        script = parts[0].strip()
        benefits = [b.strip("-• ") for b in parts[1].strip().split("\n") if b.strip()] if len(parts) > 1 else []
        return script, benefits

    except Exception as e:
        raise RuntimeError(f"OpenAI error: {str(e)}")