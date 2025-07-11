"use client"
import InferenceForm from "@/components/forms/InferenceForm";
import { getGreetings } from "@/utils/getGreetings";

export default function Home() {
  const greet = getGreetings();
  return (
    <div className="flex items-center h-screen flex-col w-screen justify-center gap-16">
      <div>
        <img src={"/empire_logo.svg"} />
      </div>

      <div className="mb-10 text-center">
        <h1 className="font-normal text-7xl text-white/70 mb-5">👋{greet}</h1>
        <p className="mb-10 bg-white/20 p-1 px-3 rounded-md font-mono font-normal">
          Context Aware Chat Assistant for Empire College Of Science
        </p>
        <InferenceForm />
      </div>
    </div>
  );
}
