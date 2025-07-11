export const getGreetings = (): string => {
  const currentTime = new Date()
  const hour = currentTime.getHours()

  if (hour >= 4 && hour < 12) {
    return "Good Morning"
  } else if (hour >= 12 && hour < 16) {
    return "Good Afternoon"
  } else if (hour >= 16 && hour < 22) {
    return "Good Evening"
  } else {
    return "Hello Night Owl"
  }
}

