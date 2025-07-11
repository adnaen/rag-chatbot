"use client"
import InferenceForm from "@/components/forms/InferenceForm";

export default function Home() {
  return (
    <div className="flex items-center h-screen flex-col w-screen justify-center gap-16">
      <div>
        <img src={"/empire_logo.svg"} />
      </div>

      <div className="min-w-2/4 max-w-3/4">
        <InferenceForm />
      </div>
    </div>
  );
}
