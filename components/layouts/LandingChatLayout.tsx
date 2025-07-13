import { getGreetings } from "@/utils/getGreetings";
import InferenceForm from "../forms/InferenceForm";
import { TChat, TChatCreate } from "@/types/common";
import DemoPrompt from "../shared/DemoPrompt";
import { demoPrompts } from "@/lib/data";
import Image from "next/image";

const LandingChatLayout = ({ onSubmit }: { onSubmit: (chat: TChatCreate | null, allChats: TChat[] | null) => void }) => {
	const greet = getGreetings();
	return (
		<>
			<div className="mb-15">
				<Image src={"/empire_logo.svg"} alt="empire logo" width={200} height={200} />
			</div>

			<div className="mb-10 text-center w-1/2">
				<h1 className="font-semibold text-5xl text-white/70 mb-5">👋{greet}</h1>
				<p className="mb-10 text-xl">
					Context Aware Chat Assistant for
					<span className="bg-white/20 p-1 px-2 ml-2 rounded-md font-mono font-normal">
						Empire College Of Science
					</span>
				</p>
				<InferenceForm onSubmit={onSubmit} />
				<div className="grid grid-cols-4 gap-5 my-10">
					{demoPrompts.map((each, idx) => (
						<DemoPrompt key={idx} prompt={each} />
					))

					}
				</div>
			</div>
		</>
	)
}

export default LandingChatLayout;
