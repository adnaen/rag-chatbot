import Link from "next/link"
import { Button } from "../ui/button"
import Image from "next/image"
import { Github } from "lucide-react"

const Header = () => {
	return (
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

	)
}
export default Header;
