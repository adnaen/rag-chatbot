import { TChat, TChatCreate } from "@/types/common";
import { Brain, User } from "lucide-react";

const ChatInterface = ({ chat }: { chat: TChat | TChatCreate }) => {
	return (
		<div className="mb-15">
			<div className="flex justify-end mb-4 items-start gap-3">
				<h1>{chat ? chat.prompt : null}</h1>
				<div className="rounded-tl-0 rounded-b-lg rounded-tr-lg bg-blue-500/30 p-3 text-white">
					<User className="w-5 h-5" />
				</div>
			</div>
			<div className="flex justify-start mb-4 items-start gap-3 bg-white/10 p-5 rounded-md">
				<div className="rounded-tr-0 rounded-b-lg rounded-tl-lg bg-yellow-500/30 p-3 text-white">
					<Brain className="w-5 h-5" />
				</div>
				<h1>{(chat && chat.assistant) ? chat.assistant : (<span className="text-gray-400 animate-pulse">generating...</span>)}</h1>
			</div>
		</div>
	)
}

export default ChatInterface;
