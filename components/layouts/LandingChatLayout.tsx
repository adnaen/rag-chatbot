import { getGreetings } from "@/utils/getGreetings";
import InferenceForm from "../forms/InferenceForm";

const LandingChatLayout = () => {
	const greet = getGreetings();
	return (
		<>
			<div>
				<img src={"/empire_logo.svg"} />
			</div>

			<div className="mb-10 text-center w-1/2">
				<h1 className="font-normal text-7xl text-white/70 mb-5">👋{greet}</h1>
				<p className="mb-10">
					Context Aware Chat Assistant for
					<span className="bg-white/20 p-1 px-2 ml-2 rounded-md font-mono font-normal">
						Empire College Of Science
					</span>
				</p>
				<InferenceForm />
			</div>
		</>
	)
}

export default LandingChatLayout;
