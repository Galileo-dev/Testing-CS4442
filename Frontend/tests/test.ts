import { expect, test } from '@playwright/test';

test('index page gets redirected to login page', async ({ page }) => {
	await page.goto('http://localhost:3000');
	expect(page.url()).toBe('http://localhost:3000/get_token');
});
