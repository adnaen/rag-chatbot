import { useState } from "react";
import { Button } from "../ui/button";
import { Textarea } from "../ui/textarea";
import { CircleArrowRight } from "lucide-react";

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
				variant={"ghost"}
				className="hover:cursor-pointer absolute top-5 right-4">
				<CircleArrowRight />
			</Button>
		</form >
	)
}

export default InferenceForm;
