import { expect, test } from '@playwright/test';
import { fireEvent } from '@testing-library/svelte';

test('index page has expected login button', async ({ page }) => {
	await page.goto('/');
	const loginButton = await page.$('text=Login');
	if (loginButton) {
		expect(await loginButton.textContent()).toBe('Login with Google');
	} else {
		throw new Error('Login button not found');
	}
});

test('login button should open popup', async ({ page }) => {
	await page.goto('/');
	const loginButton = await page.$('text=Login');
	if (loginButton) {
		await loginButton.click();
	} else {
		throw new Error('Login with Google button not found');
	}

	// expect a popup to open
	const popup = await page.waitForEvent('popup');
	expect(popup).toBeTruthy();
});
