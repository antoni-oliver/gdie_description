import fs from 'fs';
//import fetch from 'fetch';
const HF_TOKEN = 'xx';

try {
console.log(JSON.stringify(await transcribe('audio2.mp3')));
} catch (e) {
    console.error(e);
}

async function transcribe(path) {
    const data = fs.readFileSync(path, {encoding: 'base64'}).toString();
    const response = await fetch(
        "https://api-inference.huggingface.co/models/openai/whisper-large-v3",
		{
			headers: {
				Authorization: "Bearer " + HF_TOKEN,
				"Content-Type": "application/json",
			},
			method: "POST",
			body: JSON.stringify({
                inputs: data,
                parameters: {
                    return_timestamps: true
                }
            }),
		});
    return await response.json();
}
