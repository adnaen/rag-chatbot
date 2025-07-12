import { Brain, User } from "lucide-react";

const ChatInterface = () => {
	const demoData = [
		{
			user: "what is the capital of India?",
			assistant: "The capital of India is New Delhi."
		},
		{
			user: "Tell me about python programming language.",
			assistant: "Python is an General purpose programming language. Created by Guido Van Rossum. It is an Open Source scripting language have a large active community. Python mainly used for scientific computing and web development"
		},
		{
			user: "What is hot job in curretn IT market?",
			assistant: "From the big tech companies relying mostly in AI we can say that AI relate job oppertunities will blow minds in future."
		},
		{
			user: "What is Lorum ipsum",
			assistant: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
		},
	]
	return (
		<div>
			{demoData.map((each) => (
				<div>
					<div className="flex justify-end mb-4 items-start gap-3">
						<h1>{each.user}</h1>
						<div className="rounded-tl-0 rounded-b-lg rounded-tr-lg bg-blue-500/30 p-3 text-white">
							<User className="w-5 h-5" />
						</div>
					</div>
					<div className="flex justify-start mb-4 items-start gap-3 bg-white/10 p-5 rounded-md">
						<div className="rounded-tr-0 rounded-b-lg rounded-tl-lg bg-yellow-500/30 p-3 text-white">
							<Brain className="w-5 h-5" />
						</div>
						<h1>{each.assistant}</h1>
					</div>
				</div>
			))}
		</div>
	)
}

export default ChatInterface;
