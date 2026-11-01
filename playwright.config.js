import { defineConfig, devices } from '@playwright/test'

export default defineConfig({
  testDir: '.',
  testMatch: ['week-*/tests/**/*.spec.js'],
  fullyParallel: false,
  reporter: 'line',
  use: {
    headless: true,
    launchOptions: {
      executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
      args: ['--allow-file-access-from-files'],
    },
    trace: 'retain-on-failure',
  },
  projects: [
    { name: 'desktop', use: { ...devices['Desktop Chrome'] } },
    { name: 'mobile-320', use: { viewport: { width: 320, height: 800 } } },
  ],
})
