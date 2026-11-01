import { test, expect } from '@playwright/test'
import { pathToFileURL } from 'node:url'
import fs from 'node:fs/promises'
import path from 'node:path'

const root = path.resolve(import.meta.dirname, '..')

for (const [folder, minimumRows] of [['01-html-table-one', 4], ['02-html-table-two', 5]]) {
  test(`${folder} uses a caption, column headers, and complete rows`, async ({ page }) => {
    await page.goto(pathToFileURL(path.join(root, folder, 'index.html')).href)
    await expect(page.locator('table caption')).toBeVisible()
    await expect(page.locator('thead th')).not.toHaveCount(0)
    expect(await page.locator('tbody tr').count()).toBeGreaterThanOrEqual(minimumRows)
    const width = await page.locator('table').evaluate((element) => element.getBoundingClientRect().width)
    expect(width).toBeGreaterThan(0)
  })
}

test('team member module exports five complete records', async () => {
  const modulePath = pathToFileURL(path.join(root, '03-team-member-data', 'team-members.js')).href
  const { teamMembers } = await import(modulePath)
  expect(teamMembers).toHaveLength(5)
  for (const member of teamMembers) {
    expect(member).toEqual(expect.objectContaining({
      firstName: expect.any(String),
      lastName: expect.any(String),
      hobbies: expect.any(Array),
      favouriteFoods: expect.any(Array),
      pets: expect.any(Array),
    }))
    expect(member.hobbies.length).toBeGreaterThan(0)
    expect(member.favouriteFoods.length).toBeGreaterThan(0)
  }
})

test('capstone report contains at least five estimable prioritised user stories', async () => {
  const report = await fs.readFile(path.join(root, '04-user-stories', 'user-stories.md'), 'utf8')
  expect((report.match(/^## US-\d+/gm) ?? []).length).toBeGreaterThanOrEqual(5)
  expect((report.match(/\*\*Acceptance criteria:\*\*/g) ?? []).length).toBeGreaterThanOrEqual(5)
  expect((report.match(/\*\*Estimate:\*\*/g) ?? []).length).toBeGreaterThanOrEqual(5)
  expect((report.match(/\*\*Priority:\*\*/g) ?? []).length).toBeGreaterThanOrEqual(5)
})
