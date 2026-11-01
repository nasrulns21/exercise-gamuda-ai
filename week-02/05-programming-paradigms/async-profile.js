export async function loadProfiles(fetchProfiles) {
  const response = await fetchProfiles()
  if (!response.ok) throw new Error(`Unable to load profiles (${response.status})`)
  const profiles = await response.json()
  if (!Array.isArray(profiles)) throw new TypeError('Profile response must be an array')
  return profiles
}
