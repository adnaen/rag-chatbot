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
		<form className="w-full" onSubmit={handleInferenceFormSubmittion}>
			<div className="mb-10 text-center">
				<h1 className="font-bold text-3xl">Ask me about <code className="bg-white/20 p-1 px-3 rounded-md font-mono font-normal">Empire College Of Science</code></h1>
			</div>
			<div className="relative">
				<Textarea placeholder="Ask about Empire College :)" className="w-full p-5 flex justify-center items-center pr-20 rounded-3xl text-4xl" value={prompt} onChange={(e) => { setPrompt(e.target.value); }} />
				<Button className="bg-white text-black hover:bg-white/80 hover:text-black hover:cursor-pointer absolute top-3 right-4">Ask</Button>
			</div>
		</form >

	)
}

export default InferenceForm;
