export type TChat = {
  id: string,
  prompt: string | null,
  assistant?: string | null,
  created_at: Date,
}

export type TChatCreate = Omit<TChat, 'id' | 'created_at'>

