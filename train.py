import replicate

training = replicate.trainings.create(
    version="stability-ai/sdxl:d830ba5dabf8090ec0db6c10fc862c6eb1c929e1a194a5411852d25fd954ac82",
    input={
        "input_images": "https://my-domain/my-input-images.zip",
    },
    destination="my-name/my-model"
)
print(training)
