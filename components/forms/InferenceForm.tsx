import { useState } from "react";
import { Button } from "../ui/button";
import { Textarea } from "../ui/textarea";
import { CircleArrowRight, Loader } from "lucide-react";
import { TChat, TChatCreate } from "@/types/common";
import { ChatService } from "@/services/chat.service";

const InferenceForm = ({ onSubmit }: { onSubmit: (chat: TChatCreate | null, allChats: TChat[] | null) => void }) => {
	const [prompt, setPrompt] = useState<string>("");
	const [isGenerating, setIsGenerating] = useState<boolean>(false);
	const handleInferenceFormSubmittion = async (e: React.FormEvent) => {
		e.preventDefault()

		setPrompt("")
		setIsGenerating(true);
		console.log("pending task state called")
		onSubmit({ "prompt": prompt }, null)

		console.log("before the add chat calling ")
		await ChatService.addChat({ prompt: prompt, assistant: null })
		console.log("after the add chat calling ")

		console.log("before the all chat calling ")
		const allChats = await ChatService.getAllChats()
		console.log("after the all chat calling ")
		onSubmit(null, allChats)
		setIsGenerating(false)
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
				variant={"secondary"}
				disabled={isGenerating ? true : prompt === "" ? true : false}
				className="hover:cursor-pointer absolute top-5 right-4">

				{isGenerating ?
					<Loader className="animate-spin" />
					: <CircleArrowRight />
				}
			</Button>
		</form >
	)
}

export default InferenceForm;
