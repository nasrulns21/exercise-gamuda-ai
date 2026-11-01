export class TeamMember {
  constructor({ firstName, lastName, hobbies = [], favouriteFoods = [], pets = [] }) {
    this.firstName = firstName
    this.lastName = lastName
    this.hobbies = [...hobbies]
    this.favouriteFoods = [...favouriteFoods]
    this.pets = [...pets]
  }

  getFullName() {
    return `${this.firstName} ${this.lastName}`
  }

  likesHobby(hobby) {
    return this.hobbies.some((item) => item.toLowerCase() === String(hobby).toLowerCase())
  }
}

export function clearPetsRecursively(pets) {
  if (pets.length === 0) return []
  return clearPetsRecursively(pets.slice(1))
}
