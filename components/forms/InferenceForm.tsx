import { useState } from "react";
import { Button } from "../ui/button";
import { Textarea } from "../ui/textarea";
import { CircleArrowRight } from "lucide-react";
import { TChat } from "@/types/common";

const InferenceForm = ({ onSubmit }: { onSubmit: (chat: TChat) => void }) => {
	const [prompt, setPrompt] = useState<string>("");
	const handleInferenceFormSubmittion = (e: React.FormEvent) => {
		e.preventDefault()
		console.log(prompt)
		onSubmit({ "prompt": prompt })
	}

	return (
		<form className="w-full relative" onSubmit={handleInferenceFormSubmittion}>
			<Textarea
				placeholder="Ask..."
				className="w-full p-5 backdrop-blur-lg pr-20 text-xl rounded-3xl overflow-y-auto h-20 resize-none"
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
