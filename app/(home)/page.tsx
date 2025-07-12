"use client"
import ActiveChatLayout from "@/components/layouts/ActiveChatLayout";
import LandingChatLayout from "@/components/layouts/LandingChatLayout";

export default function Home() {
  return (
    <div className="">
      <LandingChatLayout />
      <ActiveChatLayout />
    </div>
  );
}
