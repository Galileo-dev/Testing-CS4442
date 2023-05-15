// import { expect, test } from '@playwright/test';
// import { fireEvent } from '@testing-library/svelte';
// import { rest } from 'msw';
// import { setupServer } from 'msw/node';
// import { addBooking } from '../src/lib/Booking.ts';
// test('booking form shows', async ({ page }) => {
// 	await page.goto('/book');
// 	const bookingForm = await page.
// });

// const server = setupServer(
// 	rest.post('http://127.0.0.1:8000/add_booking/', (req, res, ctx) => {
// 		return res(ctx.json({ message: 'Booking added successfully' }));
// 	})
// );

// describe('addBooking', () => {
// 	it('should call the add_booking API endpoint with the correct parameters', async () => {
// 		const data = {
// 			room_preference: '123',
// 			checkin: '2022-01-01T00:00:00.000Z',
// 			lengthofstay: 60
// 		};
// 		const userToken = 'abc123';

// 		await addBooking(data, userToken);

// 		expect((server as any).requests[0].method).toBe('POST');
// 		expect((server as any).requests[0].url.href).toBe('http://127.0.0.1:8000/add_booking/');
// 		expect((server as any).requests[0].headers.get('Content-Type')).toBe('application/json');
// 		expect((server as any).requests[0].headers.get('Authorization')).toBe(`Bearer ${userToken}`);
// 		expect(JSON.parse((server as any).requests[0].body)).toEqual(data);
// 	});
// });

// test('booking form shows', async ({ page }) => {
