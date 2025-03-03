import {HfInference} from "@huggingface/inference";
import fs from 'fs';
const HF_TOKEN = 'xxxx';
const inference = new HfInference(HF_TOKEN);

for (let i = 0; i < 63; i++) {
    let image = `thumb_${i+1}.jpg`;
    let start = i * 10;
    let end = (i + 1) * 10;
    let desc = await describe(image);
    console.log(`${start} --> ${end}\n${desc}`);
}

async function describe(path) {
    console.log(`Describing ${path}...`);
    const description = await inference.imageToText({
        model: 'nlpconnect/vit-gpt2-image-captioning',
        data: fs.readFileSync(path)
    });
    return description.generated_text;
}