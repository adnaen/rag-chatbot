import InferenceForm from "../forms/InferenceForm";
import ChatInterface from "../shared/ChatInterface";

const ActiveChatLayout = () => {
	return (
		<div className="max-h-[calc(100vh-80px)] mt-20 flex flex-col">
			<section className="flex-1 justify-center overflow-y-auto px-10">
				<div className="w-full max-w-3xl py-10 mx-auto">
					<ChatInterface />
				</div>
			</section>
			<div className="w-full px-10 py-5">
				<div className="w-full max-w-3xl mx-auto">
					<InferenceForm />
				</div>
			</div>
		</div>
	)
}

export default ActiveChatLayout;
