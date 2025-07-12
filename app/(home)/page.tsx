"use client"
import ActiveChatLayout from "@/components/layouts/ActiveChatLayout";
import LandingChatLayout from "@/components/layouts/LandingChatLayout";
import Header from "@/components/shared/Header";
import { useState } from "react";

export default function Home() {
  const [hasInteracted, setHasInteracted] = useState<boolean>(false);
  const onSubmit = () => {
    setHasInteracted(true);
  }
  return (
    <div className="w-full h-screen">
      {!hasInteracted ? (
        <div className="flex w-full h-full justify-center items-center flex-col">
          <LandingChatLayout onSubmit={onSubmit} />
        </div>
      ) : (
        <div>
          <Header />
          <ActiveChatLayout />
        </div>
      )}
    </div >
  );
}
