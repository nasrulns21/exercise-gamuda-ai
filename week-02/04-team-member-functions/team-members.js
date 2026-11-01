export const fullName = ({ firstName = '', lastName = '' }) => `${firstName} ${lastName}`.trim()

export function countVowels(value) {
  return (String(value).match(/[aeiou]/gi) ?? []).length
}

export const isFoodLover = ({ favouriteFoods = [] }) => favouriteFoods.length >= 3
export const isPetLover = ({ pets = [] }) => pets.length >= 2
