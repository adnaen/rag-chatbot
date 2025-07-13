import { useEffect, useState } from "react";
import InferenceForm from "../forms/InferenceForm";
import ChatInterface from "../shared/ChatInterface";
import { TChat, TChatCreate } from "@/types/common";
import { ChatService } from "@/services/chat.service";

const ActiveChatLayout = () => {
	const [chats, setChats] = useState<TChat[]>([]);
	const [pendingChat, setPendingChat] = useState<TChatCreate | null>(null);

	useEffect(() => {
		const fetchChats = async () => {
			const result = await ChatService.getAllChats()
			if (result !== null) {
				setChats(result)
			}
		}
		fetchChats()
	}, [])

	const onSubmit = (chat: TChatCreate | null, allChats: TChat[] | null) => {
		console.log(`active chat onsubmit called with : chat = ${chat} , allchat = ${allChats}`)
		if (chat !== null) {
			console.log(`pending chat setted as : ${chat}`)
			setPendingChat(chat)

		}
		if (allChats !== null) {
			setPendingChat(null)
			setChats(allChats)
		}
	}

	return (
		<div className="max-h-screen flex flex-col">
			<section className="flex-1 justify-center overflow-y-auto px-10 mt-24">
				<div className="w-full max-w-3xl py-10 mx-auto">
					{chats.map((each) => (
						<ChatInterface key={each.id} chat={each} />
					))}

					{pendingChat && (
						<ChatInterface chat={{ prompt: pendingChat.prompt }} />
					)}
				</div>
			</section>
			<div className="w-full px-10 py-5">
				<div className="w-full max-w-3xl mx-auto">
					<InferenceForm onSubmit={onSubmit} />
				</div>
			</div>
		</div>
	)
}

export default ActiveChatLayout;
