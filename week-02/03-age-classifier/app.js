export function classifyAge(age) {
  if (!Number.isFinite(age) || age < 0) return 'Invalid age'
  if (age <= 12) return 'Child'
  if (age <= 19) return 'Teenager'
  if (age <= 64) return 'Adult'
  return 'Senior'
}
