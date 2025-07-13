"use client"
import ActiveChatLayout from "@/components/layouts/ActiveChatLayout";
import LandingChatLayout from "@/components/layouts/LandingChatLayout";
import Header from "@/components/shared/Header";
import { ChatService } from "@/services/chat.service";
import { TChat, TChatCreate } from "@/types/common";
import { useEffect, useState } from "react";

export default function Home() {
  const [hasInteracted, setHasInteracted] = useState<boolean>(false);
  const [chats, setChats] = useState<TChat[]>([]);
  const [pendingChat, setPendingChat] = useState<TChatCreate | null>(null);


  useEffect(() => {
    setHasInteracted(localStorage.getItem("isInteracted") === "true")
    const fetchChats = async () => {
      const result = await ChatService.getAllChats()
      if (result !== null) {
        setChats(result)
      }
    }
    fetchChats()
  }, [])

  const onSubmit = (chat: TChatCreate | null, allChats: TChat[] | null) => {

    if (!hasInteracted) {
      localStorage.setItem("isInteracted", "true")
    }
    setHasInteracted(true);
    console.log(`active chat onsubmit called with : chat = ${chat} , allchat = ${allChats}`)
    if (chat !== null) {
      console.log(`pending chat setted as : ${chat}`)
      setPendingChat(chat)

    }
    if (allChats !== null) {
      setPendingChat(null)
      setChats(allChats)
    }
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
          <ActiveChatLayout chats={chats} pendingChat={pendingChat} onSubmit={onSubmit} />
        </div>
      )}
    </div >
  );
}
