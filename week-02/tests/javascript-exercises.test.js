import { describe, expect, it } from 'vitest'
import { dayFromNumber } from '../01-numeric-switch/app.js'
import { actionFromString } from '../02-string-switch/app.js'
import { classifyAge } from '../03-age-classifier/app.js'
import { fullName, countVowels, isFoodLover, isPetLover } from '../04-team-member-functions/team-members.js'
import { TeamMember, clearPetsRecursively } from '../05-programming-paradigms/team-member.js'
import { foodLovers, namesByHobby } from '../05-programming-paradigms/queries.js'
import { loadProfiles } from '../05-programming-paradigms/async-profile.js'

describe('switch exercises', () => {
  it('maps weekdays and groups Saturday and Sunday as Weekend', () => {
    expect(dayFromNumber(1)).toBe('Monday')
    expect(dayFromNumber(5)).toBe('Friday')
    expect(dayFromNumber(6)).toBe('Weekend')
    expect(dayFromNumber(7)).toBe('Weekend')
    expect(dayFromNumber(0)).toBe('Invalid day')
    expect(dayFromNumber('1')).toBe('Invalid day')
  })

  it('normalises supported command strings and rejects unexpected input', () => {
    expect(actionFromString(' START ')).toBe('System started')
    expect(actionFromString('pause')).toBe('System paused')
    expect(actionFromString('stop')).toBe('System stopped')
    expect(actionFromString('delete')).toBe('Unknown action')
    expect(actionFromString(null)).toBe('Unknown action')
  })
})

describe('age and profile functions', () => {
  it.each([[0, 'Child'], [12, 'Child'], [13, 'Teenager'], [19, 'Teenager'], [20, 'Adult'], [64, 'Adult'], [65, 'Senior']])('classifies age %s', (age, expected) => {
    expect(classifyAge(age)).toBe(expected)
  })

  it('rejects impossible or non-numeric ages', () => {
    expect(classifyAge(-1)).toBe('Invalid age')
    expect(classifyAge('20')).toBe('Invalid age')
  })

  it('derives profile facts without mutating the member', () => {
    const member = { firstName: 'Nasrul', lastName: 'Sharuddin', favouriteFoods: ['Soup', 'Rice', 'Fruit'], pets: ['Milo', 'Oyen'] }
    const copy = structuredClone(member)
    expect(fullName(member)).toBe('Nasrul Sharuddin')
    expect(countVowels(fullName(member))).toBe(5)
    expect(isFoodLover(member)).toBe(true)
    expect(isPetLover(member)).toBe(true)
    expect(member).toEqual(copy)
  })
})

describe('programming paradigms', () => {
  const records = [
    { firstName: 'Aina', lastName: 'Ali', hobbies: ['Hiking'], favouriteFoods: ['Laksa', 'Sushi', 'Curry'], pets: ['Milo'] },
    { firstName: 'Ben', lastName: 'Bakar', hobbies: ['Reading'], favouriteFoods: ['Rice'], pets: [] },
  ]

  it('uses class methods and recursive pet clearing with a terminating base case', () => {
    const member = new TeamMember(records[0])
    expect(member.getFullName()).toBe('Aina Ali')
    expect(member.likesHobby('hiking')).toBe(true)
    expect(clearPetsRecursively(['Milo', 'Oyen', 'Tom'])).toEqual([])
    expect(clearPetsRecursively([])).toEqual([])
  })

  it('runs immutable functional queries', () => {
    const original = structuredClone(records)
    expect(foodLovers(records).map((member) => member.firstName)).toEqual(['Aina'])
    expect(namesByHobby(records, 'hiking')).toEqual(['Aina Ali'])
    expect(records).toEqual(original)
  })

  it('loads and validates asynchronous profile data', async () => {
    await expect(loadProfiles(async () => ({ ok: true, json: async () => records }))).resolves.toHaveLength(2)
    await expect(loadProfiles(async () => ({ ok: false, status: 503 }))).rejects.toThrow('Unable to load profiles (503)')
    await expect(loadProfiles(async () => ({ ok: true, json: async () => ({ bad: true }) }))).rejects.toThrow('Profile response must be an array')
  })
})
