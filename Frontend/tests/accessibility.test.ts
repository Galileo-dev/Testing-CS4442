import { chromium, expect, test,  } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Accessibility Tests', () => {
  let browser: any;
  let page: any;

  test.beforeAll(async () => {
    browser = await chromium.launch();
  });

  test.beforeEach(async () => {
    page = await browser.newPage();
    await page.goto('/book');
  });

  test.afterEach(async () => {
    await page.close();
  });

  test.afterAll(async () => {
    await browser.close();
  });

  test('should pass accessibility tests', async () => {
    // Wait for the form to load
    await page.waitForSelector('form');

    // Check accessibility
    const results = await page.accessibility.check();

    // Check for any violations
    const violations = results.filter(
      (result) =>
        result.severity === 'critical' || result.severity === 'serious'
    );

    // Log any violations found
    if (violations.length > 0) {
      console.error('Accessibility violations:', violations);
    }

    // Assert that there are no critical or serious violations
    expect(violations.length).toBe(0);
  });

  test('should not have any automatically detectable WCAG A or AA violations', async ({ page }) => {
    await page.goto('/book');
  
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();
  
    expect(accessibilityScanResults.violations).toEqual([]);
  });
  
});
