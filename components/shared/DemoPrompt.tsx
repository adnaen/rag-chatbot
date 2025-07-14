import { Lightbulb } from "lucide-react";

const DemoPrompt = ({ prompt }: { prompt: string }) => {
	return (
		<div className="bg-white/10 border hover:cursor-pointer hover:bg-white/20 hover:border-white/80 border-transparent text-white p-3 rounded-lg transition-colors flex">
			<div className="mr-2">
				<Lightbulb />
			</div>
			<div className="text-start">
				{prompt}
			</div>
		</div>
	)
}

export default DemoPrompt;

