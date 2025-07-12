import { Github } from "lucide-react";
import Image from "next/image";
import Link from "next/link";
import { Button } from "../ui/button";
import InferenceForm from "../forms/InferenceForm";

const ActiveChatLayout = () => {
	return (
		<>
			<header className="fixed w-full px-10 items-center h-20 flex justify-between bg-white/10 rounded-xl">
				<Link href={"https://empirecollege.in/"}>
					<Image src={"/empire_logo.svg"} alt="empire logo" width={150} height={100} />
				</Link>

				<div>
					<Link href={"https://github.com/adnaen/rag-chatbot"}>
						<Button variant={"link"} size={"icon"} className="bg-white/10 text-white hover:bg-white/60 hover:text-black/80">
							<Github />
						</Button>
					</Link>

				</div>
			</header>
			<div className="h-20" />

			<section className="min-h-[calc(100vh-90px)] flex justify-center">
				<div className="w-3/4 max-w-3/4 h-100vh p-20">

				</div>
				<div className="absolute bottom-5 w-2/4">
					<InferenceForm />
				</div>
			</section>
		</ >
	)
}

export default ActiveChatLayout;
