import {HfInference} from "@huggingface/inference";
import fs from 'fs';
const HF_TOKEN = 'xx';
const inference = new HfInference(HF_TOKEN);

console.log(JSON.stringify(await transcribe('audio2.mp3')));

async function transcribe(path) {
    const response = await inference.automaticSpeechRecognition({
        model: 'openai/whisper-large-v3',
        data: JSON.stringify({
            inputs: fs.readFileSync(path, {encoding: 'base64'}).toString(),
            parameters: {
                return_timestamps: true
            }
        })
    });
    return response;
}
