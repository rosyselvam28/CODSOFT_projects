# CODSOFT AI Internship
# Task 3 - Image Captioning

from transformers import BlipProcessor

from PIL import Image
import os


class ImageCaptionGenerator:

    def __init__(self):

        print("\nLoading AI model...")

        self.processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

        self.model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

    def generate_caption(self, image_path):

        image = Image.open(
            image_path
        ).convert("RGB")

        inputs = self.processor(
            image,
            return_tensors="pt"
        )

        output = self.model.generate(
            **inputs,
            max_new_tokens=30
        )

        caption = self.processor.decode(
            output[0],
            skip_special_tokens=True
        )

        return caption


def main():

    print("\n========== IMAGE CAPTIONING AI ==========")

    image_path = input(
        "\nEnter image file name: "
    ).strip()

    if not os.path.exists(image_path):

        print("\nImage not found.")

        return

    try:

        generator = ImageCaptionGenerator()

        print("\nGenerating caption...")

        caption = generator.generate_caption(
            image_path
        )

        print("\nGenerated Caption:")

        print(caption)

    except Exception as error:

        print("\nError:")

        print(error)


main()