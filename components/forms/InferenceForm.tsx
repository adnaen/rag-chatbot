import { useState } from "react";
import { Button } from "../ui/button";
import { Textarea } from "../ui/textarea";

const InferenceForm = () => {
	const [prompt, setPrompt] = useState<string>("");
	const handleInferenceFormSubmittion = (e: React.FormEvent) => {
		e.preventDefault()
		console.log(prompt)
	}

	return (
		<form className="w-full relative" onSubmit={handleInferenceFormSubmittion}>
			<Textarea
				placeholder="Ask..."
				className="w-full p-5 pr-20 text-xl rounded-3xl overflow-y-auto h-20 resize-none"
				value={prompt}
				onChange={(e) => { setPrompt(e.target.value); }}
			/>
			<Button
				className="bg-white text-black hover:bg-white/80 hover:text-black hover:cursor-pointer absolute top-5 right-4">
				Ask
			</Button>
		</form >
	)
}

export default InferenceForm;
