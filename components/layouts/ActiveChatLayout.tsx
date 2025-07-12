import InferenceForm from "../forms/InferenceForm";
import ChatInterface from "../shared/ChatInterface";

const ActiveChatLayout = () => {

	const onSubmit = () => {
		console.log("from ladning layout")
	}

	return (
		<div className="max-h-screen flex flex-col">
			<section className="flex-1 justify-center overflow-y-auto px-10 mt-24">
				<div className="w-full max-w-3xl py-10 mx-auto">
					<ChatInterface />
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
