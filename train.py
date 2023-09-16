#!/usr/bin/python3

import replicate

training = replicate.trainings.create(
    version="stability-ai/sdxl:d830ba5dabf8090ec0db6c10fc862c6eb1c929e1a194a5411852d25fd954ac82",
    input={
        "input_images": "https://raw.githubusercontent.com/exezbcz/Woho/main/train.zip",
	"caption_prefix": 'In the style of retro,',
    },
    destination="exezbcz/sdxl-retro"
)
print(training)
