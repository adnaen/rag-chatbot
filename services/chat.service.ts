import { TChat, TChatCreate } from "@/types/common";

export class ChatService {
  static readonly API_URL = process.env.NEXT_PUBLIC_API_URL

  static async getAllChats(): Promise<TChat[] | null> {
    try {
      const response = await fetch(`${this.API_URL}/chats`)
      if (response.ok) {
        const data: TChat[] = await response.json()
        return data;
      }
      throw Error(`Error occur in fetch all chats as '${response.status}'`)
    } catch (err) {
      console.error(err)
      return null;
    }
  }

  static async addChat(newChat: TChatCreate): Promise<TChat | null> {
    try {
      const response = await fetch(`${this.API_URL}/chat`, {
        method: "POST",
        body: JSON.stringify(newChat),
        headers: {
          "Content-Type": "application/json"
        },
        credentials: "include",
      })

      if (response.ok) {
        const data: TChat = await response.json()
        return data;
      }
      throw Error(`Error occur in fetch all chats as '${response.status}'`)

    } catch (err) {
      console.error(err)
      return null;
    }

  }
}
