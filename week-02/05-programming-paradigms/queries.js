const displayName = (member) => `${member.firstName} ${member.lastName}`

export function foodLovers(members) {
  return members.filter((member) => (member.favouriteFoods ?? []).length >= 3)
}

export function namesByHobby(members, hobby) {
  const query = String(hobby).toLowerCase()
  return members
    .filter((member) => (member.hobbies ?? []).some((item) => item.toLowerCase() === query))
    .map(displayName)
}
