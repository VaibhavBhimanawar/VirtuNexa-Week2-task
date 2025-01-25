from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(input_folder, output_folder, watermark_text, transparency=128, font_size=36):
 
    os.makedirs(output_folder, exist_ok=True)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except OSError:
        print("Default font not found. Ensure arial.ttf is installed or specify another font file.")
        return
    
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            
           
            with Image.open(input_path).convert("RGBA") as base_image:
               
                overlay = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
                draw = ImageDraw.Draw(overlay)
                
                text_width, text_height = draw.textsize(watermark_text, font=font)
                position = (base_image.size[0] - text_width - 10, base_image.size[1] - text_height - 10)
               
                draw.text(position, watermark_text, fill=(255, 255, 255, transparency), font=font)
                
                watermarked_image = Image.alpha_composite(base_image, overlay)
                
                watermarked_image.convert("RGB").save(output_path)
                print(f"Watermarked image saved to: {output_path}")

input_folder = "input_images"
output_folder = "output_images"
watermark_text = "Sample Watermark"
transparency = 128  
font_size = 36
add_watermark(input_folder, output_folder, watermark_text, transparency, font_size)
