import { expect, test } from '@playwright/test';

test('index page gets redirected to login page', async ({ page }) => {
	await page.goto('/');
	expect(page.url()).toBe('/get_token');
});
