import InferenceForm from "../forms/InferenceForm";
import ChatInterface from "../shared/ChatInterface";
import { TChat, TChatCreate } from "@/types/common";

const ActiveChatLayout = ({ chats, pendingChat, onSubmit }: { chats: TChat[], pendingChat: TChatCreate | null, onSubmit: (chat: TChatCreate | null, allChats: TChat[] | null) => void }) => {

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
